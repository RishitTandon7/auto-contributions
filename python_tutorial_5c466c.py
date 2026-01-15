# Educational Python Tutorial: Building a Text-Based Adventure Game with Functions and User Input

# Learning Objective:
# This tutorial will teach beginners how to create an interactive text-based adventure game in Python.
# We will focus on using functions to organize code and user input to drive the narrative,
# making the game dynamic and responsive.

# --- Game Structure and Core Concepts ---

# Functions are like mini-programs within our larger program.
# They help us break down complex tasks into smaller, manageable pieces.
# This makes our code easier to read, understand, and reuse.

# User input allows our game to interact with the player.
# We can ask questions and use the player's answers to decide what happens next.

# --- Game Variables ---

# We'll use variables to keep track of the player's state.
# For example, their current location or whether they have a specific item.
current_location = "forest_entrance"
has_key = False

# --- Game Functions ---

# A function to display the current scene and describe the surroundings.
def display_scene(description):
    # The 'print()' function displays text on the console.
    print("\n" + "=" * 30)  # A separator line for better readability
    print(description)
    print("=" * 30 + "\n")

# A function to get player input and process their command.
def get_player_command():
    # 'input()' prompts the user for text and returns what they type.
    # '.lower()' converts the input to lowercase, making commands case-insensitive.
    command = input("What do you want to do? ").lower().strip()
    return command

# A function representing the starting point of the game.
def forest_entrance():
    global current_location, has_key # 'global' allows us to modify variables outside this function

    scene_description = "You are standing at the entrance of a dark, mysterious forest. To your north, a path leads deeper into the woods. To your east, you see a small, overgrown shack."
    display_scene(scene_description)

    while True: # This loop keeps asking for commands until a valid action is taken
        command = get_player_command()

        if "north" in command:
            current_location = "deep_woods"
            break # Exits the while loop, moving to the next scene
        elif "east" in command:
            current_location = "overgrown_shack"
            break
        else:
            print("You can't do that here.")

# A function representing a deeper part of the woods.
def deep_woods():
    global current_location, has_key

    scene_description = "You are now deep within the forest. The trees are tall and cast long shadows. You hear strange rustling noises. To your south, you can return to the forest entrance."
    display_scene(scene_description)

    while True:
        command = get_player_command()

        if "south" in command:
            current_location = "forest_entrance"
            break
        elif "examine" in command and "bush" in command:
            if not has_key:
                print("You find a rusty old key hidden beneath a bush!")
                has_key = True # Update the global variable
            else:
                print("You've already found the key here.")
        else:
            print("You can't do that here.")

# A function representing the overgrown shack.
def overgrown_shack():
    global current_location, has_key

    scene_description = "The shack is dilapidated and smells of damp earth. The door is locked. To your west, you can return to the forest entrance."
    display_scene(scene_description)

    while True:
        command = get_player_command()

        if "west" in command:
            current_location = "forest_entrance"
            break
        elif "unlock" in command and "door" in command:
            if has_key:
                print("You use the rusty key to unlock the shack door. Inside, you find a treasure chest!")
                current_location = "treasure_room" # Move to a new, winning location
                break
            else:
                print("The door is locked. You need a key.")
        else:
            print("You can't do that here.")

# A function for the winning condition.
def treasure_room():
    scene_description = "Congratulations! You've found the treasure chest! You win!"
    display_scene(scene_description)
    # In a real game, you might add an option to quit or restart here.

# --- Game Loop ---

# This is the main part of our program that keeps the game running.
def game_loop():
    global current_location # Access the global variable to know where we are

    print("Welcome to the Adventure Game!")

    # The game continues as long as the player hasn't reached the "treasure_room".
    while current_location != "treasure_room":
        if current_location == "forest_entrance":
            forest_entrance()
        elif current_location == "deep_woods":
            deep_woods()
        elif current_location == "overgrown_shack":
            overgrown_shack()
        # Add more elif statements here for new locations as you expand the game

    # Once the loop ends (because current_location is "treasure_room"), the game is over.
    treasure_room() # Display the winning message

# --- Example Usage ---

# This block ensures that the 'game_loop()' function is called only when the script is run directly.
# It's a standard Python practice.
if __name__ == "__main__":
    game_loop()