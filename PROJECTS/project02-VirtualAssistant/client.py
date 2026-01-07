import requests
import os
from dotenv import load_dotenv

load_dotenv("../../env/.env")

def ask_ai(prompt):
    api = os.getenv("OPENROUTER_API_KEY")
    if not api:
        return "API key missing!"

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api}",
        "HTTP-Referer": "http://localhost",
        "X-Title": "VirtualAssistant",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful voice assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        res = requests.post(url, headers=headers, json=data, timeout=30)
        res.raise_for_status()  # raise error if not 200
        return res.json()["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError as e:
        return f"HTTP error: {res.status_code} - {res.text}"
    except Exception as e:
        return f"Error: {e}"
