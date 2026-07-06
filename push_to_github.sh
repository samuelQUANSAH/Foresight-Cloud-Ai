#!/bin/bash
# Push to GitHub Helper Script

if [ -z "$1" ]; then
  echo "Error: GitHub repository URL not provided."
  echo "Usage: ./push_to_github.sh <github_repository_url>"
  echo "Example: ./push_to_github.sh https://github.com/username/afrophysiques-store.git"
  exit 1
fi

REPO_URL=$1

# Load .env file if it exists
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

# If GITHUB_PAT is set and REPO_URL is HTTPS, inject it
if [ -n "$GITHUB_PAT" ] && [[ "$REPO_URL" =~ ^https:// ]]; then
  echo "GitHub Personal Access Token detected in .env. Injecting credentials..."
  # Strip https:// prefix
  CLEAN_URL=${REPO_URL#https://}
  AUTH_URL="https://${GITHUB_PAT}@${CLEAN_URL}"
else
  AUTH_URL="$REPO_URL"
fi

# Set remote origin
git remote remove origin 2>/dev/null
git remote add origin "$AUTH_URL"

# Push main branch
echo "Pushing main branch to remote repository..."
git push -u origin main

if [ $? -eq 0 ]; then
  echo "Repository successfully pushed to GitHub!"
else
  echo "Error: Failed to push to remote. Ensure repository exists and token is valid."
fi
