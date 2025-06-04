# Simple API Fetcher

## Project Overview
This project, `simple-api-fetcher`, is a Python-based application designed to interact with the Pokémon API (`https://pokeapi.co/api/v2/pokemon/`). The program takes a Pokémon name as user input, fetches data from the API, and displays formatted information about the Pokémon, including its name, ID, height, weight, types, and abilities. It includes error handling for invalid inputs (e.g., unknown Pokémon names or network issues) and is structured to be easily extendable for additional features.

The project was developed as part of an internship assignment to demonstrate skills in API integration, Python programming, Git version control, and documentation. The repository includes the main script (`api_fetcher.py`), a dependency list (`requirements.txt`), and this README for setup and usage instructions.

## Setup Instructions
To run this project on your local machine, follow these steps:

1. **Prerequisites**:
   - Ensure you have Python 3.x installed. Verify with:
     ```bash
     python --version
     ```
   - Install the required `requests` library, which is used to make API calls:
     ```bash
     pip install requests
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
   - This ensures the `requests` library is available.

## Running the Program
1. **Execute the Script**:
   - In your terminal, navigate to the project folder (if not already there):
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

## Project Structure
- `api_fetcher.py`: The main Python script that handles API requests, data parsing, and output formatting.
- `requirements.txt`: Lists the required Python library (`requests`).
- `README.md`: This file, providing project details and instructions.

## Error Handling
The program includes error handling for:
- Network issues (e.g., no internet connection).
- Invalid Pokémon names (e.g., returns a 404 error with an appropriate message).
- General exceptions during API requests.

## Future Improvements
- Add support for fetching multiple Pokémon in a single run.
- Include additional Pokémon details, such as moves or evolution chains.
- Implement a graphical user interface (GUI) for better user interaction.

## Notes
- The program was tested with various Pokémon names (e.g., Pikachu, Charizard, Bulbasaur) and handles errors gracefully.
- Ensure you have an active internet connection, as the program relies on the Pokémon API.



