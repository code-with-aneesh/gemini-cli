#!/usr/bin/env python3
import os
import sys
import subprocess
import argparse
from google.generativeai import configure, GenerativeModel

# 🔑 Load API key from env
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("❌ Please set the GEMINI_API_KEY environment variable.")
    sys.exit(1)

# 🧩 Argument parser
parser = argparse.ArgumentParser(description="Gemini CLI")
parser.add_argument("-l", "--long", action="store_true", help="Get long markdown output and view via glow")
parser.add_argument("prompt", nargs=argparse.REMAINDER, help="Prompt to send to Gemini")

args = parser.parse_args()

if not args.prompt:
    print("Usage: gemini [-l] your prompt here")
    sys.exit(1)

# 📝 Build prompt
prompt = " ".join(args.prompt)
if not args.long:
    prompt += " (Respond in one line without markdown or formatting.)"
else:
    prompt += " (Respond in markdown with proper higlighting and formatting, but only answer in 6 bullet points.)"

# 🧠 Generate
try:
    configure(api_key=api_key)
    model = GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    output = response.text.strip()

    if args.long:
        subprocess.run(["glow", "-"], input=output.encode(), check=True)
    else:
        print("🧠 Gemini:", output.replace('\n', ' ').replace('\r', ' '))
except Exception as e:
    print("❌ Error:", e)
