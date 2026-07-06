#!/bin/bash
# Push to GitHub Helper Script

if [ -z "$1" ]; then
  echo "Error: GitHub repository URL not provided."
  echo "Usage: ./push_to_github.sh <github_repository_url>"
  echo "Example: ./push_to_github.sh https://github.com/username/afrophysiques-store.git"
  exit 1
fi

REPO_URL=$1

# Add remote
git remote remove origin 2>/dev/null
git remote add origin "$REPO_URL"

# Push
echo "Pushing main branch to remote $REPO_URL..."
git push -u origin main

if [ $? -eq 0 ]; then
  echo "Repository successfully pushed to GitHub!"
else
  echo "Error: Failed to push to remote. Ensure you have created the repository on GitHub and configured your SSH/HTTPS credentials."
fi
