# Geometric Art with Python Turtle and Randomness

# Learning Objective:
# This tutorial will teach you how to create captivating geometric art
# using Python's built-in 'turtle' module and the 'random' module.
# We will explore how to:
# 1. Initialize the Turtle graphics environment.
# 2. Draw basic geometric shapes like lines and squares.
# 3. Use random number generation to control shape properties
#    (e.g., color, size, position).
# 4. Create dynamic and visually interesting patterns.
#
# By the end of this tutorial, you will be able to generate your own
# unique geometric artwork and understand the fundamental principles
# of procedural art generation with code.

import turtle
import random

# --- 1. Setting up the Turtle Environment ---

# Get the screen object. This is our drawing canvas.
screen = turtle.Screen()
# Set the background color of the screen for a better visual.
screen.bgcolor("black")
# Set the title of the window for identification.
screen.title("Random Geometric Art Generator")

# Create a turtle object. This is our "pen" that will draw on the screen.
artist = turtle.Turtle()
# Speed up the drawing process. 0 is the fastest.
artist.speed(0)
# Hide the turtle icon so it doesn't obstruct the drawing.
artist.hideturtle()
# Increase the drawing pen's thickness for bolder lines.
artist.pensize(2)

# --- 2. Defining Functions for Drawing ---

def draw_random_square(x, y, size, color):
    """
    Draws a square at a specified location with a given size and color.

    Args:
        x (int): The x-coordinate for the center of the square.
        y (int): The y-coordinate for the center of the square.
        size (int): The side length of the square.
        color (str): The color of the square (e.g., "red", "#FF0000").
    """
    # Move the turtle to the starting position without drawing.
    artist.penup() # Lift the pen
    artist.goto(x - size / 2, y - size / 2) # Move to bottom-left corner
    artist.pendown() # Put the pen down to start drawing

    # Set the fill color and the pen color for the square.
    artist.fillcolor(color)
    artist.pencolor(color)

    # Begin filling the shape. This ensures the inside of the square is colored.
    artist.begin_fill()
    # Draw the four sides of the square.
    for _ in range(4):
        artist.forward(size)
        artist.left(90) # Turn 90 degrees to draw the next side
    # End the filling process.
    artist.end_fill()

def draw_random_circle(x, y, radius, color):
    """
    Draws a circle at a specified location with a given radius and color.

    Args:
        x (int): The x-coordinate for the center of the circle.
        y (int): The y-coordinate for the center of the circle.
        radius (int): The radius of the circle.
        color (str): The color of the circle.
    """
    # Move to the starting position.
    artist.penup()
    artist.goto(x, y - radius) # Move to the bottom of the circle
    artist.pendown()

    # Set the colors.
    artist.fillcolor(color)
    artist.pencolor(color)

    # Begin and end filling the circle.
    artist.begin_fill()
    # Draw the circle. The 'circle()' method takes the radius as an argument.
    artist.circle(radius)
    artist.end_fill()

# --- 3. Generating Random Colors ---

def get_random_color():
    """
    Generates a random hexadecimal color string (e.g., "#AABBCC").

    Returns:
        str: A random color string.
    """
    # Generate three random integers between 0 and 255 for R, G, B components.
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # Format these integers into a hexadecimal color string.
    # The '#{:02x}{:02x}{:02x}' format converts each integer to a 2-digit
    # hexadecimal number (e.g., 10 becomes "0a", 255 becomes "ff").
    return f"#{r:02x}{g:02x}{b:02x}"

# --- 4. Creating the Geometric Art ---

# Define the number of shapes we want to draw.
num_shapes = 100

# Loop to create multiple shapes with random properties.
for _ in range(num_shapes):
    # Generate random coordinates within the screen bounds.
    # The screen dimensions are typically -300 to 300 for x and y.
    random_x = random.randint(-300, 300)
    random_y = random.randint(-300, 300)

    # Generate a random size for the shape.
    random_size = random.randint(20, 100)

    # Get a random color for the shape.
    random_color = get_random_color()

    # Randomly decide whether to draw a square or a circle.
    shape_type = random.choice(["square", "circle"])

    if shape_type == "square":
        # Call the function to draw a square with random properties.
        draw_random_square(random_x, random_y, random_size, random_color)
    else: # shape_type == "circle"
        # Call the function to draw a circle with random properties.
        # We'll use a radius that's half of the random_size for visual balance.
        draw_random_circle(random_x, random_y, random_size / 2, random_color)

# --- 5. Keeping the Window Open ---

# This line is crucial! It keeps the turtle graphics window open
# until you manually close it. Without it, the window would disappear
# immediately after the drawing is complete.
screen.mainloop()

# --- Example Usage ---
#
# To run this code:
# 1. Save it as a Python file (e.g., geometric_art.py).
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the command: python geometric_art.py
#
# You will see a window pop up with a black background and a
# randomized collection of colorful squares and circles appearing
# on the screen, creating a unique piece of geometric art each time.
#
# Experiment by changing:
# - num_shapes: To draw more or fewer shapes.
# - The ranges for random_x, random_y, and random_size: To control
#   where and how large the shapes can be.
# - The speed of the turtle (artist.speed()): To see the drawing
#   process or finish instantly.
# - The background color (screen.bgcolor()): To change the overall mood.