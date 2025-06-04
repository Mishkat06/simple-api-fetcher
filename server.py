import requests
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.route('/')
def serve_frontend():
    return send_file('index.html')

@app.route('/fetch-api', methods=['GET'])
def fetch_api():
    try:
        # Get the API URL from query parameter
        api_url = request.args.get('url')
        if not api_url:
            return jsonify({"error": "No API URL provided"}), 400

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

        return jsonify(formatted_data), 200

    except requests.exceptions.RequestException as e:
        error_message = f"Error fetching data: {str(e)}"
        if hasattr(e, 'response') and e.response is not None:
            error_message = f"Error: Received status code {e.response.status_code}"
        return jsonify({"error": error_message}), 500
    except (KeyError, ValueError) as e:
        return jsonify({"error": f"Error parsing data: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)