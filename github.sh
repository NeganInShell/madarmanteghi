#!/bin/bash

echo "🚀 Checking git status..."
git status

echo
echo "📦 Adding all project files..."
git add .

e "✅ Committing changes..."
git commit -m "Add encoder Verilog, testbench, GUI simulator and wave files"

echo
echo "☁️  Pushing to GitHub (main)..."
git push origin main

echo
echo "🎉 Done! Everything is now on GitHub."
