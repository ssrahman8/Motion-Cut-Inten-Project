import time

class Player:
    def __init__(self):
        self.progress = 0
        self.inventory = []

    def make_choice(self, choices):
        print("\nChoose an option:")
        for i, option in enumerate(choices, 1):
            print(f"{i}. {option}")

        while True:
            try:
                choice = int(input("Enter the number of your choice: "))
                if 1 <= choice <= len(choices):
                    return choice
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input. Enter a number.")

    def update_progress(self, points):
        self.progress += points

    def manage_inventory(self, item):
        self.inventory.append(item)

def introduction(player):
    print("Welcome to the Text-Based Adventure Game!")
    time.sleep(1)
    print("You, a brave adventurer, embark on a quest to find the legendary artifact, the Crystal of Power.")
    time.sleep(1)
    print("Your journey begins in the peaceful village of Eldoria.")
    time.sleep(1)

def village_scene(player):
    print("You arrive at the village square. The villagers speak of a hidden cave where the Crystal might be found.")
    time.sleep(1)
    
    choices = ["Visit the local tavern for information", "Explore the outskirts of the village"]
    player_choice = player.make_choice(choices)

    if player_choice == 1:
        print("In the tavern, you overhear a conversation about a cave in the Whispering Woods.")
        player.update_progress(10)
    else:
        print("You discover a hidden map in the outskirts that hints at the location of the cave.")
        player.manage_inventory("Map")
        player.update_progress(15)

def cave_scene(player):
    print("Armed with information, you enter the Whispering Woods and find the entrance to the mysterious cave.")
    time.sleep(1)
    
    choices = ["Enter the cave", "Wait and observe"]
    player_choice = player.make_choice(choices)

    if player_choice == 1:
        print("You enter the dark cave, ready for whatever challenges lie ahead.")
        time.sleep(1)
        player.update_progress(20)
        player.manage_inventory("Torch")
    else:
        print("You decide to observe. After a while, a guide appears and offers to lead you through the cave.")
        player.update_progress(15)

def ending(player):
    print("After overcoming various challenges, you reach the heart of the cave.")
    time.sleep(1)
    
    if "Torch" in player.inventory and "Map" in player.inventory:
        print("With the Torch and Map, you successfully locate the Crystal of Power!")
        player.update_progress(50)
    else:
        print("Unfortunately, without the necessary tools, you couldn't find the Crystal of Power.")

def main():
    player = Player()
    introduction(player)
    village_scene(player)
    cave_scene(player)
    ending(player)

    print(f"\nYour final progress: {player.progress}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
