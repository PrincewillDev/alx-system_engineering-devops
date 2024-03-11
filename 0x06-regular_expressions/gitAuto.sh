#!/usr/bin/env bash

# Bash Script to automate Git operations

echo "Enter filename to be added"
read filename

echo "Enter Git Commit Message"
read message

git add "$filename"
git commit "$message"
git push

