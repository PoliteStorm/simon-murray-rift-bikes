#!/bin/bash

# Script to push RIFT project to GitHub private repository

REPO_NAME="rift-bikes"
GITHUB_USER="politestorm"

echo "Setting up GitHub repository..."

# Check if remote already exists
if git remote get-url origin &>/dev/null; then
    echo "Remote 'origin' already exists. Removing it..."
    git remote remove origin
fi

# Add remote repository
echo "Adding remote repository..."
git remote add origin https://github.com/${GITHUB_USER}/${REPO_NAME}.git

# Push to GitHub
echo "Pushing to GitHub..."
echo ""
echo "NOTE: You'll need to:"
echo "1. Create a private repository named '${REPO_NAME}' at https://github.com/new"
echo "2. Then run: git push -u origin main"
echo ""
echo "Or if you have GitHub CLI (gh) installed, run:"
echo "gh repo create ${REPO_NAME} --private --source=. --remote=origin --push"

