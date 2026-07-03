#!/bin/zsh
# Double-click to optimize images AND publish the site to Cloudflare.
# (First time only: run `wrangler login` in Terminal to connect your account.)

cd "$(dirname "$0")"
export PATH="$HOME/.local/bin:$HOME/.local/node/bin:$PATH"

echo "Step 1/2: optimizing images..."
python3 optimize-images.py || { echo "Optimize failed."; read; exit 1; }

echo ""
echo "Step 2/2: deploying to Cloudflare..."
# Wrangler only uploads files that changed, so this is fast after the first run.
# Deploys the static-assets Worker defined in wrangler.jsonc (patient-flower-2dca).
wrangler deploy

echo ""
echo "Done. Press Return to close."
read
