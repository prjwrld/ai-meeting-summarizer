import os, requests

headers = {"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"}
response = requests.get("https://api-inference.huggingface.co/models/facebook/bart-large-cnn", headers=headers)
print("Status Code:", response.status_code)
print("Response:", response.json())
