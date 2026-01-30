# Learning Objective:
# This tutorial will teach you how to generate unique, abstract visual art
# using Python's turtle graphics module and the power of random generation.
# We will explore how to control the turtle's movements, colors, and shapes
# in a randomized way to create unpredictable and artistic patterns.

import turtle
import random

# --- Setup the Turtle Environment ---
# This section initializes the turtle screen and the turtle itself.
# It's like setting up a canvas and a drawing tool.

# Get the screen object. This is our drawing canvas.
screen = turtle.Screen()
# Set the background color of the canvas. 'lightblue' is just an example.
screen.bgcolor("lightblue")
# Set the title of the window that appears.
screen.title("Random Abstract Art Generator")

# Create a turtle object. This is our drawing pen.
artist = turtle.Turtle()
# Make the turtle invisible while it's drawing. We only want to see the art.
artist.hideturtle()
# Speed up the drawing process. 0 means fastest.
artist.speed(0)
# Set the initial pen size (thickness of the lines).
artist.pensize(2)

# --- Core Concept: Random Movement and Color ---
# This is where the magic happens! We'll use random choices
# to dictate the turtle's actions, creating unique art each time.

def draw_random_shape(turtle_obj, num_sides, side_length):
    """
    Draws a regular polygon with a random color.

    Args:
        turtle_obj: The turtle object to use for drawing.
        num_sides: The number of sides the polygon should have.
        side_length: The length of each side of the polygon.
    """
    # Generate a random color. Colors can be represented as RGB tuples (0.0 to 1.0).
    # random.random() generates a float between 0.0 and 1.0.
    r = random.random()
    g = random.random()
    b = random.random()
    turtle_obj.pencolor(r, g, b) # Set the pen color using RGB values

    # Calculate the angle to turn for each vertex of the polygon.
    # The sum of exterior angles of any polygon is 360 degrees.
    angle = 360 / num_sides

    # Draw the sides of the polygon.
    for _ in range(num_sides):
        turtle_obj.forward(side_length) # Move forward by the specified length
        turtle_obj.right(angle)        # Turn right by the calculated angle

def generate_art(turtle_obj, num_shapes, max_size, canvas_width, canvas_height):
    """
    Generates a piece of abstract art by drawing multiple random shapes.

    Args:
        turtle_obj: The turtle object to use for drawing.
        num_shapes: The total number of shapes to draw.
        max_size: The maximum possible side length for a shape.
        canvas_width: The width of the drawing canvas.
        canvas_height: The height of the drawing canvas.
    """
    # Loop to draw the specified number of shapes.
    for _ in range(num_shapes):
        # --- Randomly Position the Turtle ---
        # Before drawing each shape, we move the turtle to a random location
        # on the canvas to ensure variety in placement.
        x_pos = random.randint(-canvas_width // 2, canvas_width // 2)
        y_pos = random.randint(-canvas_height // 2, canvas_height // 2)
        turtle_obj.penup()      # Lift the pen so it doesn't draw while moving
        turtle_obj.goto(x_pos, y_pos) # Move to the random position
        turtle_obj.pendown()    # Put the pen down to start drawing

        # --- Randomize Shape Parameters ---
        # We want each shape to be unique, so we randomize its properties.
        # Number of sides: A polygon can have 3 or more sides.
        num_sides = random.randint(3, 10) # Between 3 (triangle) and 10 (decagon)
        # Side length: How big should this shape be?
        side_length = random.randint(20, max_size) # Between 20 and our max_size

        # Call the function to draw the shape with the randomized parameters.
        draw_random_shape(turtle_obj, num_sides, side_length)

# --- Example Usage ---
# This section demonstrates how to call the art generation function.
# You can modify these values to create different styles of art.

if __name__ == "__main__":
    # Get the dimensions of the screen for positioning.
    # screen.window_width() and screen.window_height() are often the screen dimensions.
    # We'll use these to ensure shapes are drawn within the visible area.
    screen_width = screen.window_width()
    screen_height = screen.window_height()

    # Call the function to generate the art.
    # Experiment with these numbers!
    generate_art(artist, num_shapes=100, max_size=150, canvas_width=screen_width, canvas_height=screen_height)

    # Keep the window open until it's manually closed by the user.
    # This is crucial so you can see the artwork.
    screen.mainloop()
# End of tutorial. Experiment and have fun!