#!/bin/bash

set -e

echo "📦 Installing Gemini CLI..."

# Install dependencies
pip install --user google-generativeai

# Copy script to /usr/local/bin and make it executable
sudo cp gemini.py /usr/local/bin/gemini
sudo chmod +x /usr/local/bin/gemini

echo "✅ Installed 'gemini' command."

# Ask user to set API key
echo ""
echo "👉 Please add your GEMINI API key to ~/.bashrc or ~/.zshrc like this:"
echo 'export GEMINI_API_KEY="your-api-key-here"'
echo "Then run: source ~/.bashrc OR source ~/.zshrc"
