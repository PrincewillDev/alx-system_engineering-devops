#!/usr/bin/env bash

# Bash Script to automate Git operations

echo "Enter Commit Message"
read message

git add .
git commit -m "$message"
git push
