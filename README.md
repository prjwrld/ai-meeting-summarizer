# 🎙️ AI Meeting Summarizer

A production-ready AI-powered web app that transcribes `.wav` audio files and summarizes them into clean, readable text — powered by Azure Cloud, OpenAI Whisper, and Hugging Face Transformers.

<p align="center">
  <img src="https://img.shields.io/badge/Deployed%20on-Azure-0078D4?logo=azure&logoColor=white"/>
  <img src="https://img.shields.io/badge/CI/CD-Azure%20DevOps-blueviolet?logo=azure-devops"/>
  <img src="https://img.shields.io/badge/Tech%20Stack-Flask%2C%20Python%2C%20Azure%20Cloud-orange"/>
</p>

🔗 **Live Demo**: [meeting-summarizer-prajwal](https://meeting-summarizer-prajwal-f8ajetdub7etd0eb.centralindia-01.azurewebsites.net)

---

## 🚀 Features

- 🔊 Upload `.wav` meeting recordings
- 🧠 Transcribes audio using OpenAI Whisper
- ✍️ Summarizes using Hugging Face's `facebook/bart-large-cnn` model
- ⚡ Fast, responsive UI with Flask backend
- ☁️ Deployed on **Azure App Service** with CI/CD using **Azure DevOps**

---

## 🛠️ Tech Stack

| Layer        | Technology                        |
|--------------|------------------------------------|
| Frontend     | HTML, CSS (Bootstrap)              |
| Backend      | Python Flask                       |
| AI/ML APIs   | Hugging Face, OpenAI Whisper       |
| Hosting      | Azure App Services (Linux)         |
| DevOps       | Azure DevOps Git Repository        |

---

## 📂 Project Structure

```bash
├── app/                  # Summarization & transcription logic
│   ├── summarizer.py     # Summarization using Hugging Face
│   ├── transcriber.py    # Whisper transcription logic
├── ui/                   # Flask backend and HTML UI
│   └── main.py           # Entry point
├── storage/              # Uploaded .wav files
├── requirements.txt      # Python dependencies
├── startup.txt           # Startup command (used in Azure App Service)
├── test_hf.py            # API test for Hugging Face token
├── .gitignore
