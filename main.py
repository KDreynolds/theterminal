import random
from colorama import Fore, Style

class Character:
    def __init__(self, name, health, strength, agility, intelligence):
        self.name = name
        self.health = health
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.level = 1
        self.experience = 0

    def __str__(self):
        return f"Name: {self.name}, Health: {self.health}, Strength: {self.strength}, Agility: {self.agility}, Intelligence: {self.intelligence}, Level: {self.level}, Experience: {self.experience}"

def generate_character():
    name = random.choice(["Larry", "Barry", "Gary", "Terry", "Jerry", "Harry"])
    health = random.randint(50, 100)
    strength = random.randint(5, 15)
    agility = random.randint(5, 15)
    intelligence = random.randint(5, 15)
    character = Character(name, health, strength, agility, intelligence)
    return character

def start_game():
    print(Fore.YELLOW + "Welcome to the Adventure Game!" + Style.RESET_ALL)
    print("1. Start New Game")
    print("2. Exit")
    choice = input(Fore.BLUE + "Enter your choice (1/2): " + Style.RESET_ALL)

    if choice == "1":
        print("Generating characters...")
        characters = [generate_character() for _ in range(3)]
        print("Choose your character:")
        for i, character in enumerate(characters, start=1):
            print(f"{i}. {character}")

        while True:
            choice = input("Enter the number of your chosen character (1-3): ")
            if choice in ["1", "2", "3"]:
                hero = characters[int(choice) - 1]
                print(f"You have chosen: {hero}")
                break
            else:
                print("Invalid choice. Please try again.")

        # Start the game with the chosen character
        # TODO: Implement the game logic here

    elif choice == "2":
        print("Thank you for playing. Goodbye!")
    else:
        print("Invalid choice. Please try again.")

# Run the game
start_game()