#!/usr/bin/env python3
import os
import sys
from google.generativeai import configure, GenerativeModel

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("❌ Please set the GEMINI_API_KEY environment variable.")
    sys.exit(1)

if len(sys.argv) < 2:
    print("Usage: gemini your prompt here")
    sys.exit(1)

prompt = " ".join(sys.argv[1:]) + " (Respond in one line without markdown.)"

try:
    configure(api_key=api_key)
    response = GenerativeModel("gemini-2.5-flash").generate_content(prompt)
    print("🧠 Gemini:", response.text.replace('\n', ' ').replace('\r', ' ').strip())
except Exception as e:
    print("❌ Error:", e)
