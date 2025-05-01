import random
import json

professor_oaks_pokemon = ["Charmander", "Squirtle", "Bulbasaur"]

def load_save():
    """Load the user save file."""
    try:
        with open('user.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def delete_save():
    """Delete the save file."""
    try:
        with open("user.json", "w") as file:
            json.dump({}, file)
        print("Save file deleted successfully.")
    except FileNotFoundError:
        print("No save file found.")

def choose_pokemon():
    """Allow the user to choose their starter Pokemon."""
    input("Welcome to the POKESTARTER!!!!! Press Enter to start.")
    input("My name is Professor Oak, and I will be your guide in this world of Pokemon! Press Enter to continue.")
    input("I hear today you are going to choose your first Pokemon! Press Enter to continue.")
    input("There are three Pokemon to choose from: Charmander, Squirtle, and Bulbasaur. Press Enter to continue.")
    input("Here is a little bit of information about each Pokemon: Press Enter to continue.")
    input("Charmander is a fire type Pokemon. It is known for its fiery tail and its ability to breathe fire. Press Enter to continue.")
    input("Squirtle is a water type Pokemon. It is known for its ability to shoot water from its mouth and its hard shell. Press Enter to continue.")
    input("Bulbasaur is a grass type Pokemon. It is known for its ability to use vines and its ability to heal itself. Press Enter to continue.")
    input("Now, which Pokemon would you like to choose? Press Enter to continue.")
    
    while True:
        choice = input("Please choose a Pokemon: Charmander, Squirtle, or Bulbasaur: ").capitalize()
        if choice in professor_oaks_pokemon:
            print(f"You have chosen {choice}!")
            break
        else:
            print("Invalid choice. Please choose again.")
    
    name = input("What is your name? ")
    with open("user.json", "w") as file:
        json.dump({"name": name, "starter": choice}, file)

def encounter_action():
    """Handle the user's action during an encounter."""
    action = input("What do you want to do? (fight, run, catch, delete save, exit): ").lower()
    if action == "fight":
        print("You chose to fight!")
    elif action == "run":
        print("You chose to run!")
    elif action == "catch":
        print("You chose to catch!")
    elif action == "delete save":
        delete_save()
    elif action == "exit":
        print("Exiting the game.")
        exit()
    else:
        print("Invalid choice. Please choose again.")
        encounter_action()

def main():
    """Main function to start the game."""
    if input("Do you want to load a save? (yes/no): ").lower() == "yes":
        user = load_save()
        if not user:
            print("No save file found. Starting a new game.")
            choose_pokemon()
    else:
        print("Starting a new game.")
        delete_save()
        choose_pokemon()
    
    user = load_save()
    print(f"Welcome: {user['name']}")
    input("Oh no! A Wild Lechonk broke into the lab! Press Enter to continue.")
    input(f"It seems to not like your {user['starter']}! Press Enter to continue.")
    input("It's up to you to decide what to do! Press Enter to continue.")
    
    while True:
        encounter_action()

if __name__ == "__main__":
    main()