'''
'''
from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.route("/")
def home():
    return send_from_directory("static", "index.html")

#Ollama API endpoint for generating responses from the Llama 3 model or other models you have set up. Adjust the URL and payload as needed based on your Ollama configuration.
@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "")

    payload = {
        "model": "phi3", #Change this to the name of your model if it's different
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    result = response.json()

    return jsonify({
        "response": result.get("response", "")
    })

if __name__ == "__main__":
    app.run(debug=True)
