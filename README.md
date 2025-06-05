                                                                Simple API Fetcher
                                                                

Project Overview  

This project, simple-api-fetcher, is a Python-based application initially designed to interact with the Pokémon API (https://pokeapi.co/api/v2/pokemon/). It has been extended to include a backend API layer, a frontend UI, and persistence for logging API requests.  

-- Key Features:  
- Command-line script (api_fetcher.py) that fetches and displays Pokémon data  
- Flask server (server.py) with /fetch-api route for processing API requests  
- Frontend UI (index.html) with input field and response display  
- Persistent logging (fetch_history.json) and history tracking  

The project demonstrates API integration, Python programming, and full-stack development with an elegant frontend design using Bootstrap and animations.  

**Setup Instructions**  

-- 1. Prerequisites:  
- Python 3.x  
- Required libraries: requests and flask  

-- 2. Installation:  
- Clone the repository or download ZIP  
- Install dependencies using requirements.txt  

**Running the Program**  

-- Option 1: Command-Line Script  
- Run api_fetcher.py  
- Enter Pokémon name when prompted  
- View formatted output or error message  

-- Option 2: Web Interface  
- Start server.py  
- Access http://localhost:5000  
- Enter API URLs to fetch data  
- View fetch history  

Project Files: 
- api_fetcher.py: Original command-line script  
- server.py: Backend server with API routes  
- index.html: Frontend interface  
- requirements.txt: Dependency list  
- fetch_history.json: Request logs  

Error Handling:  
- Handles invalid URLs, network issues, and missing data  
- Logs all requests with timestamps and status  

Future Improvements:
- Dynamic response formatting  
- Database integration  
- Enhanced history filtering  

Notes:
- Requires internet connection  
- Tested with Pokémon API endpoints  
- Stop server with Ctrl+C when done  
