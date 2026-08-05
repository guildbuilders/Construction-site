#!/bin/zsh
# ============================================================
#  Double-click this file to publish your website.
#
#  It does three things:
#    1. Saves your changes to your project history
#    2. Backs them up to GitHub
#    3. Puts them live on guildbuildersgroup.com
#
#  You never need to type any commands. Just double-click,
#  type a short note about what you changed, and press Return.
# ============================================================

cd "$(dirname "$0")"
export PATH="$HOME/.local/bin:$HOME/.local/node/bin:$PATH"

echo "============================================"
echo "  Publishing guildbuildersgroup.com"
echo "============================================"
echo ""

# ---------- 1. What changed? ----------
if [ -z "$(git status --porcelain)" ]; then
  echo "No changes to save. Skipping to deploy..."
  echo ""
  CHANGES_TO_COMMIT=0
else
  echo "These files changed:"
  git status --short | sed 's/^/   /'
  echo ""
  CHANGES_TO_COMMIT=1

  echo "Type a short note about what you changed, then press Return."
  echo "(Or just press Return to use today's date.)"
  echo ""
  printf "Note: "
  read MESSAGE

  if [ -z "$MESSAGE" ]; then
    MESSAGE="Website update $(date '+%B %d, %Y')"
  fi

  echo ""
  echo "Step 1/3: saving your changes..."
  git add -A
  git commit -q -m "$MESSAGE" || { echo "  Could not save changes."; read; exit 1; }
  echo "  Saved: $MESSAGE"
fi

# ---------- 2. Back up to GitHub ----------
echo ""
echo "Step 2/3: backing up to GitHub..."

# The stored GitHub token has a stray space in it, which breaks a normal
# `git push`. Trimming it here so this works without any setup.
TOKEN=$(gh auth token 2>/dev/null | tr -d '[:space:]')

if [ -n "$TOKEN" ]; then
  git push "https://x-access-token:${TOKEN}@github.com/guildbuilders/Construction-site.git" main 2>&1 \
    | sed -E "s#${TOKEN}#***#g" | sed 's/^/  /'
else
  git push 2>&1 | sed 's/^/  /'
fi

if [ $? -eq 0 ]; then
  echo "  Backed up."
else
  echo ""
  echo "  Backup did not complete. Your changes are still saved on this Mac."
  echo "  The site can still go live below."
fi

# ---------- 3. Go live ----------
echo ""
echo "Step 3/3: putting the site live..."
wrangler deploy 2>&1 | sed 's/^/  /'

if [ $? -ne 0 ]; then
  echo ""
  echo "  Deploy failed. The site was NOT updated."
  echo "  Press Return to close."
  read
  exit 1
fi

echo ""
echo "============================================"
echo "  Done. Your site is live."
echo "  https://guildbuildersgroup.com"
echo ""
echo "  Note: changes can take a minute or two to"
echo "  appear. If you still see the old version,"
echo "  hard-refresh with Command+Shift+R."
echo "============================================"
echo ""
echo "Press Return to close."
read
