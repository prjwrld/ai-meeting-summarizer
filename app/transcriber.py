# app/transcriber.py

import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
from app.summarizer import summarize_text

# Load credentials from .env file
load_dotenv()

SPEECH_KEY = os.getenv("SPEECH_KEY")
SPEECH_REGION = os.getenv("SPEECH_REGION")

def transcribe_audio(file_path):
    """Convert audio to text using Azure Speech-to-Text"""
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    audio_input = speechsdk.AudioConfig(filename=file_path)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

    print(f"🔊 Transcribing file: {file_path}")
    result = speech_recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("✅ Transcription complete.")
        return result.text
    else:
        print(f"❌ Transcription failed: {result.reason}")
        if result.reason == speechsdk.ResultReason.NoMatch:
            print("🪵 Debug Info:", result.no_match_details)
        return ""

# Run full pipeline: Transcribe + Summarize
if __name__ == "__main__":
    file = "storage/sample.wav"
    text = transcribe_audio(file)
    print("🎤 Transcribed Text:", text)

    if text:
        print("\n🧠 Generating Summary with GPT...")
        summary = summarize_text(text)
        print("\n📄 Meeting Summary:\n", summary)
