# Learning Objective: Generate Algorithmic Patterns with Python Turtle

# This tutorial will guide you through creating visually appealing generative art
# using Python's built-in Turtle module. We'll focus on a fundamental concept:
# algorithmic pattern generation. By understanding how to use loops and
# simple geometric transformations, you'll be able to create a variety of
# repeating and evolving designs.

import turtle
import random

# --- Setup the Turtle Environment ---

# Get the screen object to control the window.
screen = turtle.Screen()
# Set the background color of the drawing window.
screen.bgcolor("black")
# Set the title of the drawing window.
screen.title("Generative Art with Turtle")

# Create a turtle object. This is our "pen" that will draw on the screen.
artist = turtle.Turtle()
# Set the drawing speed. 0 is the fastest, 1 is slowest, 10 is fast.
artist.speed(0)
# Hide the turtle icon while drawing to make the art cleaner.
artist.hideturtle()
# Set the pen color. We'll use a list of colors for variety.
colors = ["red", "orange", "yellow", "green", "blue", "purple", "white"]

# --- Algorithmic Pattern Generation: The Spiral ---

# Our main concept for today is generating patterns algorithmically.
# We'll start with a simple, yet effective, pattern: a growing spiral.
# The "algorithm" here is to repeatedly move forward and turn a small amount,
# increasing the forward movement slightly each time.

def draw_spiral(t, initial_length, angle_increment, color_list):
    """
    Draws a colorful, growing spiral pattern.

    Args:
        t (turtle.Turtle): The turtle object to use for drawing.
        initial_length (int): The starting length of the first line segment.
        angle_increment (float): The amount to turn the turtle after drawing each segment.
        color_list (list): A list of strings representing valid color names.
    """
    current_length = initial_length
    num_segments = 100  # The total number of line segments in the spiral.
    color_index = 0     # To cycle through the available colors.

    # Loop to draw each segment of the spiral.
    for _ in range(num_segments):
        # Set the pen color. We use the modulo operator (%) to loop back to the
        # beginning of the color list when we reach the end.
        t.pencolor(color_list[color_index % len(color_list)])

        # Move the turtle forward by the current length.
        t.forward(current_length)
        # Turn the turtle by the specified angle increment.
        t.right(angle_increment)

        # Increase the length of the next segment. This makes the spiral grow.
        current_length += 5

        # Move to the next color in the list for the next segment.
        color_index += 1

# --- Example Usage ---

# Call the function to draw the spiral with specific parameters.
# initial_length: How long the first line segment will be.
# angle_increment: How much the turtle turns after each segment. A smaller angle
#                  creates a tighter spiral, a larger angle a more open one.
# colors: The list of colors to use.
draw_spiral(artist, 10, 91, colors)

# --- Keeping the Window Open ---

# This line keeps the turtle graphics window open until it's manually closed.
# Without it, the window would appear and disappear very quickly.
turtle.done()

# --- Further Exploration (Optional - for you to try!) ---
# 1. Experiment with different `initial_length` and `angle_increment` values.
#    What happens if you use an angle like 120 or 60?
# 2. Add more colors to the `colors` list.
# 3. Try changing the `num_segments`.
# 4. Can you think of another simple algorithm for generating a pattern?
#    (Hint: What if you changed direction randomly? Or moved forward by a
#     random amount?)
# 5. Look up other turtle commands like `circle()`, `dot()`, `penup()`, `pendown()`.
#    How could you incorporate them into your patterns?