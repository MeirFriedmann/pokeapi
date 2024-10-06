#ability, move, back_default
import requests, json, random

def get_pokemon() -> json:
    try:
        with open("pokemon.txt", 'r') as file:
            pokemon_ids = {line.strip() for line in file}
            file.close()
    except FileNotFoundError:
        pokemon_ids = set()
    while True:
        pokemon_id = random.randint(1, 1025)
        if pokemon_id not in pokemon_ids:
            with open("pokemon.txt", 'a') as file:
                file.write(str(pokemon_id) + "\n")
                file.close()
            break
    request = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    pokemon = json.loads(request.content)
    return pokemon



def main():

    while True:
        asnwer = input("Do you want to draw a pokemon? (y/n)\n")
        if asnwer == "yes" or asnwer == "y":
            pokemon_json = get_pokemon()
            print("Detailes for" + pokemon_json["name"] + " :")
            print("Ability: " + pokemon_json["abilities"][0]["ability"]["name"])
            print("Move: " + pokemon_json['moves'][0]['move']['name'])
            if pokemon_json['sprites']['back_default'] is None:
                print("No picture of back was found.")
            else:
                print("Picture of back: " + pokemon_json['sprites']['back_default'])
        elif asnwer == "no" or asnwer == "n":
            exit("Farewell!")
        else:
            print("I didn't get that, try again")

if __name__ == "__main__":
    main()