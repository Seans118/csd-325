# This script fetches and displays information about a Pokemon using the PokeAPI.
# Sean Summers Assignment 9.2

import json
import requests

while True:
    # Get the Pokedex ID from the user.
    pokemon_id = input("Enter the Pokemon ID: ")

    # Construct the URL for the PokeAPI request with provided ID.
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"

    # Create a request object with a User-Agent header to avoid potential issues with the API.
    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    
    print(response.status_code)

    # Check if request was successful.
    if response.status_code == 200:
        # Convert JSON to Python dictionary.
        result = response.json()

        # Display information about the Pokemon.
        print(f"Name: {result['name']}")
        print(f"Type(s): {', '.join([t['type']['name'] for t in result['types']])}")
        print(f"Height: {result['height']}")
        print(f"Weight: {result['weight']}")

    else:
        print(f"Error: Pokemon with ID {pokemon_id} was not found.")

    # Ask the user if they want to look up another Pokemon.
    again = input("Do you want to look up another Pokemon? (yes/no): ")
    if again.lower() != "yes":
        break
    else:
        print()  # Print a newline for better readability before the next lookup.

