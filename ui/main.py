# Triggering Azure App Service deployment
import sys
import os
from flask import Flask, render_template, request

# Ensure root folder is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.transcriber import transcribe_audio
from app.summarizer import summarize_text

app = Flask(__name__, template_folder='templates', static_folder='static')
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'storage')

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    transcript = ""

    if request.method == 'POST':
        audio = request.files['audio']
        if audio:
            audio_path = os.path.join(UPLOAD_FOLDER, 'sample.wav')
            audio.save(audio_path)

            transcript = transcribe_audio(audio_path)
            summary = summarize_text(transcript)

    return render_template('index.html', transcript=transcript, summary=summary)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
