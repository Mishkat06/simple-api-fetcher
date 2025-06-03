import requests
import json

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            pokemon_info = {
                "name": data["name"].capitalize(),
                "id": data["id"],
                "height": data["height"],
                "weight": data["weight"],
                "types": [t["type"]["name"] for t in data["types"]],
                "abilities": [a["ability"]["name"] for a in data["abilities"]]
            }
            
            print("\nPokémon Data:")
            print(f"Name: {pokemon_info['name']}")
            print(f"ID: {pokemon_info['id']}")
            print(f"Height: {pokemon_info['height']} decimetres")
            print(f"Weight: {pokemon_info['weight']} hectograms")
            print(f"Types: {', '.join(pokemon_info['types'])}")
            print(f"Abilities: {', '.join(pokemon_info['abilities'])}")
            
            return pokemon_info
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def main():
    pokemon_name = input("Enter a Pokémon name (e.g., Pikachu): ")
    fetch_pokemon_data(pokemon_name)

if __name__ == "__main__":
    main()