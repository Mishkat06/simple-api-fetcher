import requests
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

HISTORY_FILE = "fetch_history.json"

# Load and reset history only once when the app starts
history = []
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=4)
else:
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=4)

def load_history():
    global history
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            history = json.load(f)
    return history

def save_history(history):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=4)

@app.route('/')
def serve_frontend():
    return send_file('index.html')

@app.route('/fetch-api', methods=['GET'])
def fetch_api():
    api_url = request.args.get('url')
    if not api_url:
        return jsonify({"error": "No API URL provided"}), 400

    history = load_history()
    log_entry = {
        "url": api_url,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "success"
    }

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        formatted_data = {
            "name": data["name"],
            "id": data["id"],
            "height": data["height"],
            "weight": data["weight"],
            "types": [t["type"]["name"] for t in data["types"]],
            "abilities": [a["ability"]["name"] for a in data["abilities"]]
        }
        history.append(log_entry)
        save_history(history)
        return jsonify(formatted_data), 200
    except requests.exceptions.RequestException as e:
        error_message = f"Error fetching data: {str(e)}"
        if hasattr(e, 'response') and e.response is not None:
            error_message = f"Error: Received status code {e.response.status_code}"
        log_entry["status"] = error_message
        history.append(log_entry)
        save_history(history)
        return jsonify({"error": error_message}), 500
    except (KeyError, ValueError) as e:
        error_message = f"Error parsing data: {str(e)}"
        log_entry["status"] = error_message
        history.append(log_entry)
        save_history(history)
        return jsonify({"error": error_message}), 500

@app.route('/fetch-history', methods=['GET'])
def fetch_history():
    history = load_history()
    return jsonify(history), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)