# Learning Objective:
# This tutorial teaches how to build an interactive story in Python
# where data visualizations dynamically update based on user choices.
# We will focus on using the 'pandas' library for data manipulation
# and 'matplotlib' for basic plotting, combined with simple 'if/elif/else'
# logic to control the narrative and visualizations.

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# --- Data Setup ---
# We'll create a simple dataset representing different scenarios
# and their associated "impacts" which we'll visualize.
# This DataFrame will hold our story's data.
data = {
    'scenario_id': [1, 2, 3, 4, 5, 6],
    'scenario_name': [
        "A Mysterious Forest",
        "A Bustling City Market",
        "A Quiet Mountain Village",
        "A Futuristic Laboratory",
        "An Ancient Ruin",
        "A Starship Bridge"
    ],
    'resource_gain': [10, 15, 5, 25, 12, 30], # Points gained from the scenario
    'risk_level': [3, 5, 2, 7, 4, 8]        # A measure of danger or challenge
}
story_df = pd.DataFrame(data)

# --- Story Logic Functions ---

def present_scenario(scenario_id, current_stats):
    """
    Displays the current scenario and its details.
    Also presents user choices.
    """
    # Find the row in our DataFrame corresponding to the scenario_id
    scenario_info = story_df[story_df['scenario_id'] == scenario_id].iloc[0]

    print("\n" + "="*40)
    print(f"You are in: {scenario_info['scenario_name']}")
    print(f"Current Stats: Resources = {current_stats['resources']}, Risk = {current_stats['risk']}")
    print("="*40)

    # Basic story branching based on scenario_id
    if scenario_id == 1: # Mysterious Forest
        print("You hear rustling in the bushes. What do you do?")
        print("1. Investigate cautiously.")
        print("2. Move away quietly.")
        choice = input("Enter your choice (1 or 2): ")
        return choice, scenario_info # Return choice and the scenario data
    elif scenario_id == 2: # Bustling City Market
        print("A merchant offers you a rare artifact. Do you buy it?")
        print("1. Investigate its authenticity.")
        print("2. Walk away, it's too expensive.")
        choice = input("Enter your choice (1 or 2): ")
        return choice, scenario_info
    elif scenario_id == 3: # Quiet Mountain Village
        print("The villagers seem wary of outsiders. How do you approach them?")
        print("1. Offer a small gift.")
        print("2. Observe from a distance.")
        choice = input("Enter your choice (1 or 2): ")
        return choice, scenario_info
    elif scenario_id == 4: # Futuristic Laboratory
        print("A strange device hums ominously. Do you interact with it?")
        print("1. Press a button.")
        print("2. Leave it alone.")
        choice = input("Enter your choice (1 or 2): ")
        return choice, scenario_info
    elif scenario_id == 5: # Ancient Ruin
        print("You find a hidden inscription. Do you try to decipher it?")
        print("1. Spend time studying it.")
        print("2. Move on, time is short.")
        choice = input("Enter your choice (1 or 2): ")
        return choice, scenario_info
    elif scenario_id == 6: # Starship Bridge
        print("An alert flashes on the main console. What is your command?")
        print("1. Initiate evasive maneuvers.")
        print("2. Analyze the alert data.")
        choice = input("Enter your choice (1 or 2): ")
        return choice, scenario_info
    else:
        print("You've reached an unexpected path!")
        return "exit", None # Signal to end the story

def update_stats(current_stats, scenario_info, choice):
    """
    Updates the player's resources and risk level based on their choice.
    This is where the core logic of how choices affect the game state happens.
    """
    # We'll use simple modifiers for demonstration.
    # In a real game, this could be much more complex.
    if choice == '1': # Often the more adventurous or direct choice
        current_stats['resources'] += scenario_info['resource_gain'] // 2 # Get some resources
        current_stats['risk'] += scenario_info['risk_level'] // 3        # Minor risk increase
        print("Your choice led to a small gain and minor risk.")
    elif choice == '2': # Often the more cautious or indirect choice
        current_stats['resources'] += scenario_info['resource_gain'] // 4 # Get fewer resources
        current_stats['risk'] += scenario_info['risk_level'] // 5        # Minimal risk increase
        print("Your choice was safe but yielded fewer rewards.")
    else:
        print("Invalid choice, stats remain unchanged.")
        # If it's an invalid choice, we don't update stats.

    # Ensure stats don't go below zero or become excessively high (simple clamping)
    current_stats['resources'] = max(0, current_stats['resources'])
    current_stats['risk'] = max(0, current_stats['risk'])
    return current_stats

def visualize_stats(current_stats):
    """
    Generates a simple bar chart showing the player's current resources and risk level.
    This visualization will update each time the player makes a choice.
    """
    # Clear previous plots to avoid overlap
    plt.clf()

    # Data for the plot
    labels = ['Resources', 'Risk Level']
    values = [current_stats['resources'], current_stats['risk']]

    # Create the bar chart
    plt.figure(figsize=(8, 5)) # Set the figure size for better readability
    bars = plt.bar(labels, values, color=['green', 'red'])

    # Add titles and labels for clarity
    plt.title("Player Status")
    plt.ylabel("Value")

    # Add the value on top of each bar for easier reading
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval), ha='center', va='bottom')

    # Display the plot
    plt.show(block=False) # block=False allows the story to continue while the plot is shown
    plt.pause(0.1) # Pause briefly to allow the plot to render

# --- Game Loop ---
def play_story():
    """
    The main function to run the interactive story.
    It initializes player stats, loops through scenarios,
    and manages player interaction and visualization updates.
    """
    print("Welcome to the Interactive Story Adventure!")

    # Initialize player's starting statistics
    # 'resources' can be thought of as points, items, or currency.
    # 'risk' is a measure of how dangerous the player's situation is.
    current_stats = {'resources': 50, 'risk': 10}
    current_scenario_id = 1 # Start with the first scenario

    # We'll limit the story to a few steps for this example
    max_steps = 6
    step_count = 0

    while step_count < max_steps and current_scenario_id != "exit":
        # Present the current scenario and get user's choice
        choice, scenario_info = present_scenario(current_scenario_id, current_stats)

        # If the player chooses to exit, break the loop
        if choice == "exit":
            break

        # If we got valid scenario info (not None)
        if scenario_info is not None:
            # Update player's stats based on their choice
            current_stats = update_stats(current_stats, scenario_info, choice)

            # Visualize the updated stats
            visualize_stats(current_stats)

            # Determine the next scenario based on the choice (simple linear progression for now)
            # In a more complex story, this would involve more sophisticated logic.
            if choice == '1':
                current_scenario_id += 1
            elif choice == '2':
                current_scenario_id += 1 # For simplicity, both choices lead to the next scenario
            else:
                print("Invalid input, returning to the previous scenario.")
                # No change in current_scenario_id, loop will re-present

        step_count += 1 # Increment step count to eventually end the story

        # Check for game over conditions (example)
        if current_stats['risk'] > 50:
            print("\nYour risk has become too high! Game Over!")
            break
        if current_stats['resources'] < 0:
            print("\nYou've run out of resources! Game Over!")
            break

    print("\n" + "="*40)
    print("Thank you for playing the story!")
    print(f"Final Stats: Resources = {current_stats['resources']}, Risk = {current_stats['risk']}")
    print("="*40)
    plt.close('all') # Close all matplotlib figures at the end

# --- Example Usage ---
# This block ensures the play_story() function runs only when the script is executed directly.
if __name__ == "__main__":
    play_story()