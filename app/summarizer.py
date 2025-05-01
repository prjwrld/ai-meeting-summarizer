# app/summarizer.py

import requests
import os
from dotenv import load_dotenv

# Load your Hugging Face token from .env
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

def summarize_text(text):
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}

    payload = {
        "inputs": text,
        "options": {"wait_for_model": True}
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()[0]["summary_text"]
    else:
        return f"❌ Failed to summarize: {response.status_code} - {response.text}"
