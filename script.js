/* Phone-click conversion, mirroring the inline version on the landing
   pages so a tap from anywhere on the site is measured the same way.
   No value is sent - the conversion action in Google Ads owns it. */
function gb_callConversion() {
  if (typeof gtag === "function") {
    gtag("event", "phone_click");
    gtag("event", "conversion", { send_to: "AW-18096983407/4xQWCNa0wdwcEO-aqLVD" });
  }
  return true;
}


// Hero video: only load it on screens wide enough to benefit. On phones the
// poster image stands in, which saves 4-6MB of download on a cellular
// connection. The <video> carries no src until this runs, so nothing is
// fetched on mobile at all.
(function () {
  var v = document.querySelector(".hero-bg-video[data-src]");
  if (!v) return;
  if (!window.matchMedia("(min-width: 861px)").matches) return;
  v.preload = "auto";
  v.src = v.dataset.src;
  var play = v.play();
  if (play && play.catch) { play.catch(function () {}); }
})();

const menuToggle = document.getElementById("menu-toggle");
const siteNav = document.getElementById("site-nav");

if (menuToggle && siteNav) {
  menuToggle.addEventListener("click", () => {
    siteNav.classList.toggle("open");
  });

  const navLinks = siteNav.querySelectorAll("a");
  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      siteNav.classList.remove("open");
    });
  });
}

const lightbox = document.getElementById("lightbox");
const lightboxImg = document.getElementById("lightbox-img");
const lightboxClose = document.getElementById("lightbox-close");
const lightboxPrev = document.getElementById("lightbox-prev");
const lightboxNext = document.getElementById("lightbox-next");

const clickableImages = Array.from(
  document.querySelectorAll(".gallery-image, .home-photo")
);

let currentImageIndex = 0;

// Gallery thumbnails load a small -1000 copy for speed; the full-size
// original is stored in data-full so the lightbox can show it crisp on click.
function fullSrc(img) {
  return img.dataset.full || img.src;
}

function openLightbox(index) {
  if (!lightbox || !lightboxImg || clickableImages.length === 0) return;

  currentImageIndex = index;
  lightboxImg.src = fullSrc(clickableImages[currentImageIndex]);
  lightboxImg.alt = clickableImages[currentImageIndex].alt;
  lightbox.classList.add("active");
  document.body.style.overflow = "hidden";
}

function closeLightbox() {
  if (!lightbox) return;

  lightbox.classList.remove("active");
  document.body.style.overflow = "";
}

function showNextImage() {
  if (!lightboxImg || clickableImages.length === 0) return;

  currentImageIndex = (currentImageIndex + 1) % clickableImages.length;
  lightboxImg.src = fullSrc(clickableImages[currentImageIndex]);
  lightboxImg.alt = clickableImages[currentImageIndex].alt;
}

function showPrevImage() {
  if (!lightboxImg || clickableImages.length === 0) return;

  currentImageIndex = (currentImageIndex - 1 + clickableImages.length) % clickableImages.length;
  lightboxImg.src = fullSrc(clickableImages[currentImageIndex]);
  lightboxImg.alt = clickableImages[currentImageIndex].alt;
}

clickableImages.forEach((img, index) => {
  img.addEventListener("click", () => {
    openLightbox(index);
  });
});

if (lightboxClose) {
  lightboxClose.addEventListener("click", closeLightbox);
}

if (lightboxNext) {
  lightboxNext.addEventListener("click", (e) => {
    e.stopPropagation();
    showNextImage();
  });
}

if (lightboxPrev) {
  lightboxPrev.addEventListener("click", (e) => {
    e.stopPropagation();
    showPrevImage();
  });
}

if (lightbox) {
  lightbox.addEventListener("click", (e) => {
    if (e.target === lightbox) {
      closeLightbox();
    }
  });
}

document.addEventListener("keydown", (e) => {
  if (!lightbox || !lightbox.classList.contains("active")) return;

  if (e.key === "Escape") {
    closeLightbox();
  }

  if (e.key === "ArrowRight") {
    showNextImage();
  }

  if (e.key === "ArrowLeft") {
    showPrevImage();
  }
});

// Pages with a full-screen video hero (home + contact): the header is
// transparent over the video and turns solid once you scroll past it.
// On the homepage the logo also swaps bold -> regular over the ivory.
const overlayHeader = document.querySelector(
  "body.home .site-header, body.contact-page .site-header, body.gallery-page .site-header, body.about-page .site-header, body.services-page .site-header, body.faq-page .site-header, body.blog-page .site-header"
);
if (overlayHeader) {
  const heroVideo = document.querySelector(".hero-video");
  const logoImg = overlayHeader.querySelector(".logo-image");
  const updateHeader = () => {
    const heroHeight = heroVideo ? heroVideo.offsetHeight : window.innerHeight;
    const scrolled = window.scrollY > heroHeight - overlayHeader.offsetHeight;
    overlayHeader.classList.toggle("scrolled", scrolled);
    if (logoImg) {
      // Root-relative: the blog lives in /blog/, where a bare filename would
      // resolve to /blog/guild-logo-*.png and 404.
      logoImg.src = scrolled ? "/guild-logo-reg.png" : "/guild-logo-4.png";
    }
  };
  updateHeader();
  window.addEventListener("scroll", updateHeader, { passive: true });
  window.addEventListener("resize", updateHeader);
}

// Scroll-reveal: content sections gently fade + rise as they enter view.
if (
  "IntersectionObserver" in window &&
  window.matchMedia("(prefers-reduced-motion: no-preference)").matches
) {
  const blocks = document.querySelectorAll(
    ".section > .container, .projects-overview > .container, .project-section > .container"
  );
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.06, rootMargin: "0px 0px -30px 0px" }
  );
  blocks.forEach((block) => {
    block.classList.add("reveal");
    io.observe(block);
  });
}

// Sticky mobile Call / Quote bar (shown on phones; not on the contact page)
if (!document.body.classList.contains("contact-page")) {
  const bar = document.createElement("div");
  bar.className = "mobile-cta";
  bar.innerHTML =
    '<a class="call" href="tel:+16197632982">Call Us</a>' +
    '<a class="quote" href="contact.html">Request a Quote</a>';
  document.body.appendChild(bar);
}
