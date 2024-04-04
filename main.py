import random
from colorama import Fore, Style

class Character:
    def __init__(self, name, health, strength, agility, intelligence, x, y):
        self.name = name
        self.health = health
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.level = 1
        self.experience = 0
        self.x = x
        self.y = y

    def __str__(self):
        return f"Name: {self.name}, Health: {self.health}, Strength: {self.strength}, Agility: {self.agility}, Intelligence: {self.intelligence}, Level: {self.level}, Experience: {self.experience}, Position: ({self.x}, {self.y})"

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

def generate_character(x, y):
    name = random.choice(["Larry", "Barry", "Gary", "Terry", "Jerry", "Harry"])
    health = random.randint(50, 100)
    strength = random.randint(5, 15)
    agility = random.randint(5, 15)
    intelligence = random.randint(5, 15)
    character = Character(name, health, strength, agility, intelligence, x, y)
    return character

def generate_dungeon():
    dungeon_names = [
        "Abandoned Mine",
        "Haunted Crypt",
        "Forgotten Ruins",
        "Ancient Tomb",
        "Forsaken Castle",
        "Misty Caverns",
        "Enchanted Grove",
        "Fiery Volcano",
        "Frozen Wasteland",
        "Sunken Temple"
    ]
    dungeon_descriptions = [
        "You enter a dark and eerie dungeon filled with danger and treasure.",
        "The air is thick with the stench of decay as you venture into the depths.",
        "Ancient ruins crumble around you, hiding secrets of a forgotten era.",
        "The tomb is filled with the restless spirits of the long-dead.",
        "A once-grand castle now lies in ruins, its halls echoing with ghostly whispers.",
        "Mist swirls around you as you navigate the twisting caverns.",
        "The grove pulses with an otherworldly energy, its flora both beautiful and deadly.",
        "The heat is oppressive as you descend into the heart of the volcano.",
        "Icy winds howl through the desolate landscape, chilling you to the bone.",
        "The temple, long lost beneath the waves, holds ancient secrets and forgotten treasures."
    ]
    dungeon_name = random.choice(dungeon_names)
    dungeon_description = random.choice(dungeon_descriptions)
    return dungeon_name, dungeon_description

def generate_item():
    item_names = [
        "Sword of Destiny",
        "Amulet of Power",
        "Enchanted Ring",
        "Staff of the Elements",
        "Cloak of Shadows",
        "Boots of Swiftness",
        "Helm of Insight",
        "Gauntlets of Strength",
        "Bow of Precision",
        "Shield of Protection"
    ]
    item_descriptions = [
        "A legendary sword imbued with the power to shape fate itself.",
        "An amulet that pulses with an ancient, mysterious energy.",
        "A ring that glimmers with enchanted light, enhancing the wearer's abilities.",
        "A staff that harnesses the raw power of the elements.",
        "A cloak that blends the wearer into the shadows, granting stealth and concealment.",
        "Boots that grant incredible speed and agility to the wearer.",
        "A helm that bestows enhanced wisdom and clarity of thought.",
        "Gauntlets that imbue the wearer with superhuman strength.",
        "A bow that never misses its mark, guided by an unseen force.",
        "A shield that emanates an aura of protection, warding off harm."
    ]
    item_name = random.choice(item_names)
    item_description = random.choice(item_descriptions)
    return item_name, item_description

def generate_npc():
    npc_names = [
        "Wise Old Sage",
        "Mysterious Stranger",
        "Friendly Merchant",
        "Eccentric Wizard",
        "Grizzled Warrior",
        "Mischievous Rogue",
        "Gentle Healer",
        "Cryptic Oracle",
        "Jovial Bard",
        "Stoic Paladin"
    ]
    npc_dialogues = [
        "Greetings, traveler. How may I assist you on your journey?",
        "Ah, another adventurer. Be cautious, for danger lurks in every corner.",
        "Welcome, friend! Take a look at my wares. I have something for every need.",
        "The stars align in curious ways. Your fate is intertwined with the destiny of this land.",
        "I've seen many battles, but the fight against evil is never-ending.",
        "Looking for trouble, or just passing through? Either way, watch your back.",
        "Welcome, weary traveler. Let me tend to your wounds and ease your burdens.",
        "The future is shrouded in mystery, but I sense great potential within you.",
        "Ah, a fellow adventurer! Let me regale you with tales of heroic deeds and epic sagas.",
        "Stand tall, champion of justice. The path ahead is fraught with peril, but your courage will light the way."
    ]
    npc_name = random.choice(npc_names)
    npc_dialogue = random.choice(npc_dialogues)
    return npc_name, npc_dialogue

def play_game(hero, scenario, world):
    print(f"Starting Scenario: {scenario.title}")
    print(scenario.description)

    # Set up initial game state based on the scenario
    location = f"({hero.x}, {hero.y})"  # Update location based on hero's initial position
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
            # Prompt the player for the direction to move
            direction = input("Enter the direction to move (up/down/left/right): ")
            if direction == "up":
                hero.y -= 1
            elif direction == "down":
                hero.y += 1
            elif direction == "left":
                hero.x -= 1
            elif direction == "right":
                hero.x += 1
            else:
                print("Invalid direction. Please try again.")
                continue

            location = f"({hero.x}, {hero.y})"  # Update location based on hero's new position

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
        characters = [generate_character(0, 0) for _ in range(3)]
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