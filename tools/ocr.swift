import Foundation
import Vision
import ImageIO

let path = CommandLine.arguments[1]
let url = URL(fileURLWithPath: path)
guard let src = CGImageSourceCreateWithURL(url as CFURL, nil),
      let cg = CGImageSourceCreateImageAtIndex(src, 0, nil) else {
    FileHandle.standardError.write("cannot decode: \(path)\n".data(using: .utf8)!); exit(1)
}
let req = VNRecognizeTextRequest { r, _ in
    guard let obs = r.results as? [VNRecognizedTextObservation] else { return }
    let lines = obs.compactMap { o -> (CGFloat, CGFloat, String)? in
        guard let t = o.topCandidates(1).first?.string else { return nil }
        return (o.boundingBox.midY, o.boundingBox.minX, t)
    }.sorted { abs($0.0 - $1.0) < 0.01 ? $0.1 < $1.1 : $0.0 > $1.0 }
    for l in lines { print(l.2) }
}
req.recognitionLevel = .accurate
req.usesLanguageCorrection = true
try? VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
