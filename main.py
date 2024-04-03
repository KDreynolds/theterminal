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
    
class Scenario:
    def __init__(self, title, description):
        self.title = title
        self.description = description

scenarios = [
    Scenario("Amnesia", "You wake up in a strange place with no memory of how you got there or who you are. You seem to be in a maze of twisty passages, all alike."),
    Scenario("Shipwrecked", "You find yourself washed up on the shore of an unknown island after a shipwreck. The island is inhabited by a tribe of pirates."),
    Scenario("Prisoner", "You are wrongfully imprisoned and must find a way to break out of jail."),
    Scenario("Treasure", "You are on a quest to find the legendary treasure of the ancient past. You are on a journey to the ancient ruins of the ancient past."),
    Scenario("Chosen One", "You have been chosen by an ancient ceremony to save your people. You are on a quest to find the right answers to the ancient questions."),
    Scenario("Darkness", "You are in a dark, mysterious place. You are on a quest to find the light.")
]

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

        # Select a random scenario
        scenario = random.choice(scenarios)
        print(f"\nStarting Scenario: {scenario.title}")
        print(scenario.description)

        # Start the game with the chosen character and scenario
        # TODO: Implement the game logic here

    elif choice == "2":
        print("Thank you for playing. Goodbye!")
    else:
        print("Invalid choice. Please try again.")

# Run the game
start_game()