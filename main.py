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
    

class Point:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

def generate_world(width, height):
    world = []

    # Generate points of interest
    num_dungeons = random.randint(3, 6)
    num_items = random.randint(5, 10)
    num_npcs = random.randint(4, 8)

    # Generate dungeon points
    for _ in range(num_dungeons):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        dungeon_point = Point(x, y, "dungeon")
        world.append(dungeon_point)

    # Generate item points
    for _ in range(num_items):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        item_point = Point(x, y, "item")
        world.append(item_point)

    # Generate NPC points
    for _ in range(num_npcs):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        npc_point = Point(x, y, "npc")
        world.append(npc_point)

    return world

# Example usage
world_width = 50
world_height = 50
generated_world = generate_world(world_width, world_height)

# Print the generated world points
for point in generated_world:
    print(f"Point: ({point.x}, {point.y}) - Type: {point.type}")


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

def generate_dungeon():
    # Placeholder implementation for generating a dungeon
    dungeon_name = random.choice(["Abandoned Mine", "Haunted Crypt", "Forgotten Ruins"])
    dungeon_description = "You enter a mysterious dungeon filled with danger and treasure."
    return dungeon_name, dungeon_description

def generate_item():
    # Placeholder implementation for generating an item
    item_name = random.choice(["Sword of Destiny", "Amulet of Power", "Enchanted Ring"])
    item_description = "You find a powerful item that can aid you in your quest."
    return item_name, item_description

def generate_npc():
    # Placeholder implementation for generating an NPC
    npc_name = random.choice(["Wise Old Sage", "Mysterious Stranger", "Friendly Merchant"])
    npc_dialogue = "Greetings, traveler. How may I assist you on your journey?"
    return npc_name, npc_dialogue

def play_game(hero, scenario, world):
    print(f"Starting Scenario: {scenario.title}")
    print(scenario.description)

    # Set up initial game state based on the scenario
    location = "Starting Location"
    inventory = []

    while True:
        print(f"\nCurrent Location: {location}")
        print("Available Actions:")
        print("1. Explore")
        print("2. Check Inventory")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            # Explore action
            print("You explore your surroundings...")
            # Check if the current location matches any points of interest in the world
            for point in world:
                if point.x == hero.x and point.y == hero.y:
                    if point.type == "dungeon":
                        dungeon_name, dungeon_description = generate_dungeon()
                        print(f"You have found a dungeon: {dungeon_name}")
                        print(dungeon_description)
                        # TODO: Implement dungeon exploration logic
                    elif point.type == "item":
                        item_name, item_description = generate_item()
                        print(f"You have found an item: {item_name}")
                        print(item_description)
                        inventory.append(item_name)
                    elif point.type == "npc":
                        npc_name, npc_dialogue = generate_npc()
                        print(f"You have encountered an NPC: {npc_name}")
                        print(npc_dialogue)
                        # TODO: Implement NPC interaction logic
            # TODO: Update game state, describe results, and prompt for next action
        elif choice == "2":
            # Check Inventory action
            if inventory:
                print("Your inventory:")
                for item in inventory:
                    print(item)
            else:
                print("Your inventory is empty.")
        elif choice == "3":
            # Quit action
            print("Thank you for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

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

        # Generate the game world
        world_width = 50
        world_height = 50
        world = generate_world(world_width, world_height)

        # Select a random scenario
        scenario = random.choice(scenarios)
        print(f"\nStarting Scenario: {scenario.title}")
        print(scenario.description)

        # Start the game with the chosen character, scenario, and world
        play_game(hero, scenario, world)

    elif choice == "2":
        print("Thank you for playing. Goodbye!")
    else:
        print("Invalid choice. Please try again.")

# Run the game
start_game()