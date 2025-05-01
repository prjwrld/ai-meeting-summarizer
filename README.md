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
```
| Layer        | Technology                         |
|--------------|------------------------------------|
| Frontend     | HTML, CSS (Bootstrap)              |
| Backend      | Python Flask                       |
| AI/ML APIs   | Hugging Face, OpenAI Whisper       |
| Hosting      | Azure App Services (Linux)         |
| DevOps       | Azure DevOps Git Repository        |
```
<table>
  <thead>
    <tr>
      <th>Layer</th>
      <th>Technology</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Frontend</td>
      <td>HTML, CSS (Bootstrap)</td>
    </tr>
    <tr>
      <td>Backend</td>
      <td>Python Flask</td>
    </tr>
    <tr>
      <td>AI/ML APIs</td>
      <td>Hugging Face, OpenAI Whisper</td>
    </tr>
    <tr>
      <td>Hosting</td>
      <td>Azure App Services (Linux)</td>
    </tr>
    <tr>
      <td>DevOps</td>
      <td>Azure DevOps Git Repository</td>
    </tr>
  </tbody>
</table>

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
```
⚙️ Environment Variables

Make sure to configure the following variables in Azure App Settings:
```
HF_TOKEN=<your_huggingface_api_token>
OPENAI_API_KEY=<your_openai_key>
```
And locally in your .env (not committed to GitHub):
```
HF_TOKEN=hf_XXXXXXXXXXXXXXXXXXXX
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXX
```
🚀 Run Locally
```
# Clone the project
git clone https://github.com/prjwrld/ai-meeting-summarizer.git
cd ai-meeting-summarizer

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add your .env with keys
touch .env

# Run the Flask app
python3 ui/main.py
```
<img width="385" alt="Screenshot 2025-05-01 at 4 42 21 PM" src="https://github.com/user-attachments/assets/19a0361a-d138-40d3-90e3-d4891e4abdd0" />

📦 Deployment Workflow
	1.	🧠 Build AI logic using Whisper and Hugging Face
	2.	🔨 Test locally with curl and sample .wav
	3.	🗂️ Push to Azure DevOps Git repo
	4.	☁️ Deployed to Azure App Services
	5.	🔁 Live updates using git push to DevOps or GitHub
 
📸 Preview
<img width="1392" alt="Screenshot 2025-05-01 at 4 43 05 PM" src="https://github.com/user-attachments/assets/18893d23-8e4a-4787-b3d9-9e95f8e8c0b8" />
<img width="1392" alt="Screenshot 2025-05-01 at 5 18 33 PM" src="https://github.com/user-attachments/assets/1c209af2-8fbb-44b7-9fcc-ba7c57fa8bef" />

🔐 Security
	•	✅ .env is gitignored
	•	✅ Secrets were scrubbed from commit history
	•	✅ GitHub Push Protection blocks exposed tokens

 🙋‍♂️ Author

Prajwal Prasad
Built with ❤️ and deployed on Azure
<p align="center">
  <a href="https://github.com/prjwrld" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-Visit%20Profile-black?logo=github&style=for-the-badge" alt="Visit My GitHub">
  </a>
</p>

📜 License

MIT License
---
```
✅ Let me know if you want a pre-formatted version uploaded directly to your repo or rendered for preview.
```

