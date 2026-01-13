# Fractal Art with Recursion in Python: A Beginner's Guide

# ## Learning Objective:
# This tutorial will teach you how to create mesmerizing fractal art
# using the power of recursion in Python. We will focus on the
# fundamental concept of recursion and how it's applied to draw
# self-similar geometric patterns.

# We'll use the 'turtle' module for simple graphics.
# It's great for beginners as it mimics drawing with a pen.
import turtle

# ## Core Concept: Recursion
# Recursion is a programming technique where a function calls itself
# to solve smaller, similar problems. Think of it like Russian nesting dolls;
# each doll contains a smaller version of itself.
#
# For fractals, this means drawing a pattern, and then telling the function
# to draw the same pattern again, but smaller and in specific places.

def draw_fractal(t, order, size):
    """
    Draws a recursive fractal pattern.

    Args:
        t: The turtle object used for drawing.
        order: The current depth of recursion. This determines how complex
               the fractal will be. A higher order means more detail.
        size: The length of the line segment to draw at the current step.
              This shrinks with each recursive call.
    """
    # ## Base Case: The Stopping Condition
    # Every recursive function needs a "base case" – a condition where
    # it stops calling itself. Without it, the function would run forever!
    # In our fractal, when the order reaches 0, we simply draw a straight line
    # of the current size and stop recursing.
    if order == 0:
        t.forward(size)  # Draw a line segment
        return  # Stop the recursion for this branch

    # ## Recursive Step: The Action
    # If we haven't reached the base case, we perform the recursive step.
    # This is where the magic happens! We break down the current task
    # into smaller, identical tasks.

    # Calculate the size for the next level of recursion.
    # We typically divide the size by a factor (e.g., 3 for a Koch snowflake-like structure).
    # This ensures the fractals get smaller at each step.
    new_size = size / 3

    # We perform a series of drawing actions and recursive calls.
    # The exact sequence defines the type of fractal.
    # For this example, we'll draw a simple fractal that branches out.

    # 1. Draw the first part of the fractal.
    draw_fractal(t, order - 1, new_size)

    # 2. Turn left and draw the next part.
    # The angle (e.g., 60 degrees) determines the shape of the branches.
    t.left(60)
    draw_fractal(t, order - 1, new_size)

    # 3. Turn right to face the original direction, then turn right again.
    # This sets up the next branch.
    t.right(120)
    draw_fractal(t, order - 1, new_size)

    # 4. Turn left to face the original direction, then turn left again.
    # This sets up the final branch.
    t.left(60)
    draw_fractal(t, order - 1, new_size)

    # 5. Move back to the starting point of this segment.
    # This is crucial for the turtle to return to its original position
    # before the next segment is drawn, ensuring the pattern connects correctly.
    # We need to move back by 'size' and then adjust direction.
    t.backward(size)

# ## Example Usage:
# Let's set up the turtle screen and call our fractal drawing function.

if __name__ == "__main__":
    # Create a screen for our drawing.
    screen = turtle.Screen()
    screen.setup(width=600, height=600) # Set screen dimensions
    screen.bgcolor("black")           # Set background color
    screen.title("Mesmerizing Fractal Art") # Set window title

    # Create a turtle object.
    my_turtle = turtle.Turtle()
    my_turtle.speed(0)       # Set speed to fastest (0) for quick drawing.
    my_turtle.color("cyan")  # Set the drawing color.
    my_turtle.penup()        # Lift the pen so we don't draw while moving to start.
    my_turtle.goto(-150, 100) # Move the turtle to a starting position.
    my_turtle.pendown()      # Put the pen down to start drawing.

    # Define the parameters for our fractal.
    fractal_order = 4  # How complex you want the fractal (try 2, 3, 4, 5)
    initial_size = 300 # The starting length of the main segment.

    # Call the recursive function to draw the fractal.
    print(f"Drawing fractal with order {fractal_order} and initial size {initial_size}...")
    draw_fractal(my_turtle, fractal_order, initial_size)
    print("Fractal drawing complete!")

    # Keep the window open until it's manually closed.
    screen.mainloop()