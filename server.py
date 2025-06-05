import requests
from flask import Flask, request, jsonify, send_file
import json
import os
from datetime import datetime

app = Flask(__name__)

# File to store fetch history
HISTORY_FILE = "fetch_history.json"

# Helper function to load history from file
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return []

# Helper function to save history to file
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

    # Load existing history
    history = load_history()

    # Prepare log entry
    log_entry = {
        "url": api_url,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "success"  # Default status
    }

    try:
        # Fetch data from the provided URL
        response = requests.get(api_url)
        response.raise_for_status()

        # Parse the JSON data
        data = response.json()

        # Format the data (specific to Pokémon API for now)
        formatted_data = {
            "name": data["name"],
            "id": data["id"],
            "height": data["height"],
            "weight": data["weight"],
            "types": [t["type"]["name"] for t in data["types"]],
            "abilities": [a["ability"]["name"] for a in data["abilities"]]
        }

        # Log the successful fetch
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