# Simple API Fetcher

This project is a simple API fetcher that retrieves and formats data from the Pokémon API. It takes a Pokémon name as input and outputs formatted details such as the Pokémon's name, ID, height, weight, types, and abilities.

## What the Program Does
- Fetches data from the Pokémon API (`https://pokeapi.co/api/v2/pokemon/`).
- Parses the JSON response.
- Prints formatted Pokémon details, including:
  - Name
  - ID
  - Height (in decimetres)
  - Weight (in hectograms)
  - Types
  - Abilities

## How to Run
1. **Prerequisites**:
   - Python 3.x installed.
   - Install the required package:
     ```bash
     pip install requests