################################################################################
# Learning Objective:
# This tutorial will teach you how to generate unique abstract art using
# Python's Turtle graphics library and the `random` module. We will focus on
# using random numbers to control various aspects of drawing, such as color,
# shape, size, and movement, to create unpredictable and visually interesting patterns.
# By the end of this tutorial, you will be able to:
# 1. Understand how to import and use the `turtle` and `random` modules.
# 2. Control the turtle's pen color and speed.
# 3. Draw basic geometric shapes (lines, circles, squares) with random properties.
# 4. Implement loops to create complex patterns.
# 5. Experiment with different random parameters to generate diverse art styles.
################################################################################

# Import necessary libraries
import turtle
import random

# --- Setup the Turtle Screen ---
# This section initializes the drawing canvas and sets up the environment.

# Get the screen object. This allows us to control the overall window.
screen = turtle.Screen()
# Set the background color of the drawing window.
# We use a random hex color code for variety.
screen.bgcolor(random.choice(['#f0f8ff', '#faebd7', '#e0ffff', '#f5f5dc', '#fff0f5']))
# Set the title of the window.
screen.title("Unique Abstract Art Generator")

# --- Setup the Turtle ---
# This section creates our drawing "pen" and configures its initial state.

# Create a Turtle object, which is our drawing tool.
artist = turtle.Turtle()
# Set the drawing speed. 0 is the fastest, 1 is slowest, 10 is fast.
# We set it to 0 for quicker art generation.
artist.speed(0)
# Hide the turtle cursor (the arrow) while it's drawing.
# This makes the art appear more cleanly.
artist.hideturtle()
# Set the pen to be up initially. This means when we move the turtle,
# it won't draw anything until we put the pen down.
artist.penup()

# --- Define Drawing Functions ---
# We'll create reusable functions to draw different elements of our art.
# This makes our code organized and easier to understand.

def draw_random_line(t, max_length=100):
    """
    Draws a line of a random length and color.

    Args:
        t (turtle.Turtle): The turtle object to use for drawing.
        max_length (int): The maximum length the line can be.
    """
    # Set the pen color to a random RGB tuple.
    # Each component (red, green, blue) is a random integer between 0 and 255.
    t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # Set the line width to a random value for variation.
    t.pensize(random.randint(1, 5))

    # Choose a random direction for the line.
    # `random.choice` picks one item from a list.
    direction = random.choice(['forward', 'backward', 'left', 'right'])

    # Calculate a random length for the line.
    length = random.randint(10, max_length)

    # Move the turtle to a random position on the screen.
    # `random.randint` ensures the coordinates are integers.
    # The screen's width and height can be accessed via `screen.window_width()`
    # and `screen.window_height()`, but for simplicity, we'll use fixed bounds.
    t.goto(random.randint(-300, 300), random.randint(-300, 300))
    # Put the pen down to start drawing.
    t.pendown()

    # Draw the line based on the chosen direction.
    if direction == 'forward':
        t.forward(length)
    elif direction == 'backward':
        t.backward(length)
    elif direction == 'left':
        # Turn left by a random angle between 0 and 360 degrees.
        t.left(random.randint(0, 360))
        t.forward(length)
    elif direction == 'right':
        # Turn right by a random angle between 0 and 360 degrees.
        t.right(random.randint(0, 360))
        t.forward(length)

    # Lift the pen up after drawing.
    t.penup()

def draw_random_circle(t, max_radius=50):
    """
    Draws a circle of a random radius and color at a random position.

    Args:
        t (turtle.Turtle): The turtle object to use for drawing.
        max_radius (int): The maximum radius the circle can have.
    """
    # Set fill color to a random RGB tuple.
    t.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # Set pen color to a random RGB tuple.
    t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # Set pen width.
    t.pensize(random.randint(1, 3))

    # Move to a random position.
    t.goto(random.randint(-300, 300), random.randint(-300, 300))
    # Put pen down to start drawing.
    t.pendown()

    # Start filling the shape with color.
    t.begin_fill()
    # Draw a circle with a random radius.
    radius = random.randint(10, max_radius)
    t.circle(radius)
    # Stop filling the shape.
    t.end_fill()
    # Lift pen up.
    t.penup()

def draw_random_square(t, max_side=100):
    """
    Draws a square of a random side length and color at a random position.

    Args:
        t (turtle.Turtle): The turtle object to use for drawing.
        max_side (int): The maximum side length the square can have.
    """
    # Set fill color.
    t.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # Set pen color.
    t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # Set pen width.
    t.pensize(random.randint(1, 4))

    # Move to a random position.
    t.goto(random.randint(-300, 300), random.randint(-300, 300))
    # Put pen down.
    t.pendown()

    # Start filling the square.
    t.begin_fill()
    # Calculate the side length.
    side_length = random.randint(20, max_side)
    # Draw the square by repeating 4 times: move forward and turn 90 degrees.
    for _ in range(4):
        t.forward(side_length)
        t.right(90)
    # Stop filling.
    t.end_fill()
    # Lift pen up.
    t.penup()


# --- Main Art Generation Loop ---
# This is where we call our drawing functions multiple times to create the art.

# We'll draw a combination of shapes and lines.
# The number of elements to draw can be adjusted.
num_elements = 50 # How many shapes/lines to draw

for _ in range(num_elements):
    # Choose a random drawing function to call.
    # This adds more unpredictability to the art.
    drawing_choice = random.choice([
        draw_random_line,
        draw_random_circle,
        draw_random_square
    ])
    # Call the chosen drawing function.
    drawing_choice(artist)

# --- Finalization ---
# This section cleans up the drawing process.

# Hide the turtle after all drawing is complete.
artist.hideturtle()
# Keep the window open until it's manually closed by the user.
screen.mainloop()

# --- Example Usage ---
# To run this code:
# 1. Save it as a Python file (e.g., abstract_art.py).
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the command: python abstract_art.py
# A window will pop up displaying your unique abstract art!
# You can re-run the script to generate a new piece of art.
# Experiment by changing `num_elements` or the `max_` parameters in the functions.