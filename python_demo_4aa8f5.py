# Chatbot Learning with Keyword Recognition and Response Adaptation
#
# Learning Objective:
# This tutorial will guide you through building a simple Python chatbot.
# We'll focus on teaching the chatbot to:
# 1. Recognize keywords in user input.
# 2. Store and retrieve responses based on these keywords.
# 3. "Learn" by allowing the user to teach new responses.
# 4. Adapt its behavior based on what it learns.
#
# This will introduce fundamental programming concepts like:
# - Dictionaries for storing data.
# - String manipulation (lowercase, splitting).
# - Conditional statements (if/elif/else).
# - Loops for continuous interaction.
# - User input handling.

# --- Chatbot Core ---

# A dictionary to store our chatbot's knowledge.
# The keys will be keywords (or phrases), and the values will be the chatbot's responses.
# This is our chatbot's "memory".
knowledge_base = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What's on your mind?",
    "how are you": "I'm just a program, so I don't have feelings, but I'm ready to chat!",
    "what is your name": "I am a simple learning chatbot.",
    "bye": "Goodbye! Come back soon!",
    "thank you": "You're welcome!",
}

def process_user_input(user_input: str) -> str:
    """
    Analyzes the user's input to find a matching response in the knowledge base.
    If no direct match is found, it tries to identify a keyword and potentially
    "learn" a new response if the user provides one.

    Args:
        user_input: The string of text provided by the user.

    Returns:
        A string containing the chatbot's response.
    """
    # Convert the user's input to lowercase to make matching case-insensitive.
    # This is crucial for robust keyword recognition.
    processed_input = user_input.lower()

    # Iterate through the keywords in our knowledge base.
    # We check if any keyword is present *within* the user's input.
    for keyword, response in knowledge_base.items():
        if keyword in processed_input:
            # If a keyword is found, return the corresponding response immediately.
            return response

    # If no direct keyword match was found, we enter a "learning" phase.
    # This is where the chatbot can be taught new things.
    # We'll look for patterns like "teach me: <keyword> is <response>".
    teach_phrase = "teach me: "
    if teach_phrase in processed_input:
        try:
            # Extract the part of the input that comes after "teach me: ".
            teaching_content = processed_input.split(teach_phrase)[1].strip()

            # We expect the user to provide the information in the format: "keyword is response".
            if " is " in teaching_content:
                # Split the teaching content into the new keyword and its associated response.
                new_keyword, new_response = teaching_content.split(" is ", 1)

                # Add the newly learned information to our knowledge base.
                # This is the "learning" part!
                knowledge_base[new_keyword.strip()] = new_response.strip()
                return f"Okay, I've learned that '{new_keyword.strip()}' means '{new_response.strip()}'."
            else:
                return "I don't understand how to learn that. Please use the format: teach me: <keyword> is <response>"
        except IndexError:
            # Handle cases where "teach me: " is at the very end of the input or malformed.
            return "I need more information to learn. Please use the format: teach me: <keyword> is <response>"

    # If no keyword was found and it wasn't a learning command, provide a default response.
    return "I'm not sure how to respond to that. Can you teach me? Use 'teach me: <keyword> is <response>'."

# --- Main Chat Loop ---

def run_chatbot():
    """
    Starts the main loop for the chatbot, allowing continuous interaction with the user.
    """
    print("Welcome to the Learning Chatbot! Type 'quit' or 'exit' to end.")

    # This loop will continue indefinitely until the user decides to quit.
    while True:
        # Get input from the user.
        user_input = input("You: ")

        # Check if the user wants to exit the chatbot.
        if user_input.lower() in ["quit", "exit", "goodbye"]:
            print("Chatbot: Goodbye! It was nice chatting with you.")
            break  # Exit the while loop and end the program.

        # Process the user's input using our function and get the chatbot's response.
        chatbot_response = process_user_input(user_input)

        # Display the chatbot's response.
        print(f"Chatbot: {chatbot_response}")

# --- Example Usage ---

if __name__ == "__main__":
    # This block ensures that run_chatbot() is called only when the script is executed directly,
    # not when it's imported as a module into another script.
    run_chatbot()

# --- How to run this code ---
# 1. Save the code as a Python file (e.g., learning_chatbot.py).
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the command: python learning_chatbot.py
#
# --- Experiment with it! ---
# - Try saying "hello" or "how are you".
# - Try teaching it something new: "teach me: what is your favorite color is blue".
# - Then ask it: "what is your favorite color".
# - Try saying something it doesn't know, and then teach it.
# - Notice how it remembers what you teach it.