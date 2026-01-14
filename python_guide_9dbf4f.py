# Learning Objective:
# This tutorial will teach you how to use a simple AI language model
# to generate creative short stories in Python. We will focus on
# leveraging the `transformers` library by Hugging Face to access
# and utilize pre-trained text generation models. This will introduce
# you to the basics of Natural Language Generation (NLG) in a fun and
# accessible way.

# First, we need to install the necessary library.
# You can do this by opening your terminal or command prompt and typing:
# pip install transformers torch
#
# 'transformers' provides access to state-of-the-art pre-trained models
# for various NLP tasks, including text generation.
# 'torch' is a deep learning framework that 'transformers' relies on.

# --- Core Concepts ---
# 1. Pre-trained Language Models: These are AI models that have already
#    been trained on massive amounts of text data. They have learned
#    patterns, grammar, facts, and even some reasoning capabilities.
#    We'll be using one of these models to generate our stories.
#
# 2. Text Generation: This is the process of using an AI model to
#    produce new text that is coherent and relevant to a given prompt
#    or starting point.

# Import the necessary component from the transformers library.
# The 'pipeline' function is a high-level abstraction that makes it
# very easy to use pre-trained models for various tasks without
# needing to understand all the underlying complexities.
from transformers import pipeline

def generate_story(prompt: str, max_length: int = 150, num_return_sequences: int = 1) -> list[str]:
    """
    Generates one or more creative short stories based on a given prompt
    using a pre-trained AI language model.

    Args:
        prompt (str): The starting text or idea for the story.
                      This is what the AI will build upon.
        max_length (int): The maximum number of tokens (words/sub-words)
                          the generated story should have. This controls
                          the length of the output.
        num_return_sequences (int): The number of different story
                                    variations to generate.

    Returns:
        list[str]: A list of generated story strings.
    """

    # Initialize the text generation pipeline.
    # We specify 'text-generation' as the task.
    # The 'gpt2' model is a popular and capable choice for this task.
    # It's a good balance of performance and resource requirements.
    # For larger/more complex stories, you might explore 'gpt2-medium',
    # 'gpt2-large', or even models like 'gpt2-xl', but these require
    # more memory and processing power.
    generator = pipeline('text-generation', model='gpt2')

    # Generate the story(ies).
    # The 'generator' object is called like a function.
    # It takes the 'prompt' as input.
    # 'max_length' dictates how long the generated text can be.
    # 'num_return_sequences' allows us to get multiple different outputs
    # from the same prompt, giving us more creative options.
    # 'no_repeat_ngram_size' is a parameter to help prevent the model
    # from getting stuck in repetitive loops. It ensures that no
    # sequence of N words repeats within the generated text.
    # A common value for this is 2 or 3.
    generated_texts = generator(
        prompt,
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        no_repeat_ngram_size=2 # Helps prevent repetitive phrases
    )

    # Extract the generated story text from the output.
    # The 'generator' returns a list of dictionaries, where each dictionary
    # contains a 'generated_text' key holding the actual story.
    stories = [story['generated_text'] for story in generated_texts]

    return stories

# --- Example Usage ---
if __name__ == "__main__":
    # This block of code will only run when the script is executed directly,
    # not when it's imported as a module into another script.
    # This is a common Python best practice.

    print("Welcome to the AI Story Generator!\n")

    # Define a creative prompt to start our story.
    # The more descriptive your prompt, the more focused the story will be.
    story_idea = "In a hidden forest, a tiny dragon found a glowing mushroom. The mushroom whispered secrets of the ancient trees."

    # Set how long we want our stories to be.
    story_length = 100 # In tokens (roughly words)

    # Decide how many different versions of the story we want.
    number_of_stories = 3

    print(f"Generating {number_of_stories} stories based on the prompt:")
    print(f"'{story_idea}'\n")

    try:
        # Call our function to generate the stories.
        generated_stories = generate_story(
            prompt=story_idea,
            max_length=story_length,
            num_return_sequences=number_of_stories
        )

        # Print each generated story.
        for i, story in enumerate(generated_stories):
            print(f"--- Story {i + 1} ---")
            print(story)
            print("-" * (len(f"--- Story {i + 1} ---"))) # Separator for clarity
            print() # Blank line between stories

    except Exception as e:
        # Catch potential errors, like network issues during model download
        # or if the model itself has problems.
        print(f"An error occurred: {e}")
        print("Please ensure you have an internet connection and the 'transformers' and 'torch' libraries are installed correctly.")
        print("You can install them by running: pip install transformers torch")

    print("Happy storytelling with AI!")