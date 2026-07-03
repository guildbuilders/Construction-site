#!/bin/zsh
# Double-click this file in Finder to optimize images before uploading.
cd "$(dirname "$0")"
export PATH="$HOME/.local/bin:$PATH"
python3 optimize-images.py
echo ""
echo "Press Return to close this window."
read
