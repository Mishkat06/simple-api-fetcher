# Simple API Fetcher

## Project Overview
This project, `simple-api-fetcher`, is a Python-based application initially designed to interact with the Pokémon API (`https://pokeapi.co/api/v2/pokemon/`). It has been extended to include a backend API layer that allows fetching data from any public API URL via a `/fetch-api` route. The program now supports:

- **Day 2**: A command-line script (`api_fetcher.py`) that takes a Pokémon name as user input, fetches data from the Pokémon API, and displays formatted information (name, ID, height, weight, types, abilities).
- **Day 3**: A Flask-based backend server (`server.py`) with a `/fetch-api` route that accepts a public API URL as input and returns parsed and formatted JSON or an error message.

The project demonstrates skills in API integration, Python programming, Git version control, and backend development. The repository includes the main scripts (`api_fetcher.py`, `server.py`), a dependency list (`requirements.txt`), and this README for setup and usage instructions.

## Setup Instructions
To run this project on your local machine, follow these steps:

1. **Prerequisites**:
   - Ensure you have Python 3.x installed. Verify with:
     ```bash
     python --version
     ```
   - Install the required libraries (`requests` for API calls, `flask` for the backend server):
     ```bash
     pip install requests flask
     ```

2. **Clone the Repository**:
   - Clone this repository to your local machine:
     ```bash
     git clone https://github.com/Mishkat06/simple-api-fetcher.git
     cd simple-api-fetcher
     ```
   - Alternatively, download the ZIP file from GitHub and extract it.

3. **Verify Dependencies**:
   - The `requirements.txt` file lists the dependencies. Install them using:
     ```bash
     pip install -r requirements.txt
     ```
   - This ensures the `requests` and `flask` libraries are available.

## Running the Program

### Option 1: Command-Line Script (Day 2)
1. **Execute the Script**:
   - In your terminal, navigate to the project folder:
     ```bash
     cd path/to/simple-api-fetcher
     ```
   - Run the script:
     ```bash
     python api_fetcher.py
     ```

2. **Provide Input**:
   - The program will prompt you to enter a Pokémon name (e.g., `Pikachu`).
   - Enter a name and press Enter.

3. **View Output**:
   - If successful, the program will display formatted Pokémon details. For example:
     ```
     Enter a Pokémon name (e.g., Pikachu): Pikachu

     Pokémon Data:
     Name: Pikachu
     ID: 25
     Height: 4 decimetres
     Weight: 60 hectograms
     Types: electric
     Abilities: static, lightning-rod
     ```
   - If the Pokémon name is invalid, you’ll see an error message, such as:
     ```
     Error: Received status code 404
     ```

### Option 2: Backend Server 
1. **Start the Server**:
   - In your terminal, navigate to the project folder:
     ```bash
     cd path/to/simple-api-fetcher
     ```
   - Run the Flask server:
     ```bash
     python server.py
     ```
   - The server will start on `http://localhost:5000`.

2. **Test the `/fetch-api` Route**:
   - Open a browser or use a tool like `curl` or Postman to make a GET request to:
     ```
     http://localhost:5000/fetch-api?url=https://pokeapi.co/api/v2/pokemon/pikachu
     ```
   - **Example Response (Success)**:
     ```json
     {
       "name": "pikachu",
       "id": 25,
       "height": 4,
       "weight": 60,
       "types": ["electric"],
       "abilities": ["static", "lightning-rod"]
     }
     ```
   - **Example Response (Error)**:
     - For an invalid URL (e.g., `http://localhost:5000/fetch-api?url=https://pokeapi.co/api/v2/pokemon/xyz`):
       ```json
       {
         "error": "Error: Received status code 404"
       }
       ```
     - For a missing URL:
       ```json
       {
         "error": "No API URL provided"
       }
       ```

## Project Structure
- `api_fetcher.py`: The original command-line script that fetches and formats Pokémon API data (Day 2).
- `server.py`: The Flask server with the `/fetch-api` route to fetch data from any public API URL (Day 3).
- `requirements.txt`: Lists the required Python libraries (`requests`, `flask`).
- `README.md`: This file, providing project details and instructions.

## Error Handling
The `/fetch-api` route includes error handling for:
- Missing URL parameter (`400 Bad Request`).
- Network issues (e.g., no internet connection, `500 Internal Server Error`).
- Invalid API responses (e.g., `404 Not Found`, returned as `500` with error message).
- JSON parsing or missing keys (`500 Internal Server Error`).

## Future Improvements
- Generalize the response formatting to handle different API structures dynamically.
- Add support for fetching multiple URLs in a single request.
- Include additional API details based on the provided URL.

## Notes
- The program was tested with various Pokémon API URLs (e.g., `https://pokeapi.co/api/v2/pokemon/pikachu`, `https://pokeapi.co/api/v2/pokemon/charizard`) and handles errors gracefully.
- Ensure you have an active internet connection, as the program relies on external APIs.
- Stop the Flask server (Ctrl+C in the terminal) when done testing.

If you encounter any issues or have questions, feel free to reach out!

