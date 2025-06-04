import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/fetch-api', methods=['GET'])
def fetch_api():
    try:
        # Get the API URL from query parameter (e.g., /fetch-api?url=https://pokeapi.co/api/v2/pokemon/pikachu)
        api_url = request.args.get('url')
        if not api_url:
            return jsonify({"error": "No API URL provided"}), 400

        # Fetch data from the provided URL
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the JSON data
        data = response.json()

        # Format the data (specific to Pokémon API for now, but can be generalized later)
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
        # Handle network errors or bad status codes
        error_message = f"Error fetching data: {str(e)}"
        if hasattr(e, 'response') and e.response is not None:
            error_message = f"Error: Received status code {e.response.status_code}"
        return jsonify({"error": error_message}), 500
    except (KeyError, ValueError) as e:
        # Handle JSON parsing or missing keys
        return jsonify({"error": f"Error parsing data: {str(e)}"}), 500

@app.route('/favicon.ico')
def favicon():
    return '', 204  # Return an empty response with 204 No Content



if __name__ == "__main__":
    app.run(debug=True, port=5000)