# Simple API Fetcher

## Project Overview
This project, `simple-api-fetcher`, is a Python-based application initially designed to interact with the Pokémon API (`https://pokeapi.co/api/v2/pokemon/`). It has been extended to include a backend API layer, a frontend UI, and persistence for logging API requests. The program now supports:

- **Day 2**: A command-line script (`api_fetcher.py`) that takes a Pokémon name as user input, fetches data from the Pokémon API, and displays formatted information (name, ID, height, weight, types, abilities).
- **Day 3**: A Flask-based server (`server.py`) with a `/fetch-api` route that accepts a public API URL as input and returns parsed and formatted JSON or an error message.
- **Day 4**: A frontend UI (`index.html`) with an input field to enter an API URL and a button to fetch data via the `/fetch-api` route, with responses displayed on the page. Supports multiple URLs sequentially.
- **Day 5**: Persistence for logging API fetches (URL, timestamp, status) in a file (`fetch_history.json`), a `/fetch-history` route to retrieve past requests, and a frontend update to display the fetch history.

The project demonstrates skills in API integration, Python programming, Git version control, backend development, frontend development, and persistence. The repository includes the main scripts (`api_fetcher.py`, `server.py`, `index.html`), a dependency list (`requirements.txt`), a log file (`fetch_history.json`), and this README for setup and usage instructions.

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
   - If successful, the program will display formatted Pokémon data:
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

### Option 2: Backend Server and Frontend UI (Day 3, Day 4, and Day 5)
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

2. **Access the Frontend**:
   - Open a browser and navigate to:
     ```
     http://localhost:5000
     ```
   - You’ll see a simple UI with an input field, a "Fetch Data" button, and a "View Fetch History" button.

3. **Fetch Data**:
   - Enter an API URL (e.g., `https://pokeapi.co/api/v2/pokemon/pikachu`) in the input field.
   - Click "Fetch Data".
   - The response will be displayed below the input field, showing formatted Pokémon data or an error message.
   - Each fetch is logged with its URL, timestamp, and status in `fetch_history.json`.

4. **View Fetch History**:
   - Click the "View Fetch History" button.
   - The history of past fetches (URL, timestamp, status) will be displayed below the button.

5. **Optional: Test the `/fetch-api` and `/fetch-history` Routes Directly**:
   - **Fetch API**:
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
       ```json
       {
         "error": "Error: Received status code 404"
       }
       ```
   - **Fetch History**:
     ```
     http://localhost:5000/fetch-history
     ```
     - **Example Response**:
       ```json
       [
         {
           "url": "https://pokeapi.co/api/v2/pokemon/pikachu",
           "timestamp": "2025-06-04 13:15:23",
           "status": "success"
         },
         {
           "url": "https://pokeapi.co/api/v2/pokemon/xyz",
           "timestamp": "2025-06-04 13:15:30",
           "status": "Error: Received status code 404"
         }
       ]
       ```

## Project Structure
- `api_fetcher.py`: The original command-line script that fetches data from the Pokémon API (Day 2).
- `server.py`: The backend server with the `/fetch-api` route (Day 3), serves the frontend UI (Day 4), and includes persistence with `/fetch-history` (Day 5).
- `index.html`: The frontend UI for inputting API URLs, displaying responses (Day 4), and showing fetch history (Day 5).
- `requirements.txt`: A list of required Python libraries (`requests`, `flask`).
- `fetch_history.json`: A file storing the history of API fetches (Day 5).
- `README.md`: This file, providing project details and instructions.

## Error Handling
- The `/fetch-api` route handles:
  - Backend errors: Missing URLs (`400`), invalid URLs (`500` with status code), network issues, JSON parsing errors (`500`).
  - Logs all requests, including errors, with their status.
- The `/fetch-history` route handles:
  - Returns an empty list if no history exists.
- Frontend errors: Displays validation errors (e.g., empty URL) and backend errors in the UI.

## Future Improvements
- Generalize the backend response formatting to handle different API structures dynamically
- Use a database (e.g., SQLite) instead of a JSON file for better scalability
- Add filtering and sorting options for the fetch history in the frontend

## Notes
- The program was tested with various Pokémon API URLs (e.g., `https://pokeapi.co/api/v2/pokemon/pikachu`, `https://pokeapi.co/api/v2/pokemon/charizard`) and handles errors gracefully
- Ensure you have an active internet connection
- Stop the Flask server (Ctrl+C in the terminal) when done testing
- The `fetch_history.json` file is created automatically the first time you fetch data

