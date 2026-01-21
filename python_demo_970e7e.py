# Learning Objective:
# This tutorial will teach you how to create mesmerizing fractal art
# using the power of recursion and Python's Turtle module.
# We will focus on understanding how recursion can be used to
# generate complex patterns from simple rules.

import turtle
import math # We might use math for more complex fractal variations later,
            # but for this simple example, Turtle handles most geometry.

# --- Function to draw a simple fractal (Sierpinski Triangle) ---
# This function uses recursion to draw a self-similar pattern.
# Recursion is when a function calls itself.
# Think of it like a set of Russian nesting dolls: each doll contains a smaller version of itself.

def draw_sierpinski(t, order, size):
    """
    Draws a Sierpinski triangle recursively.

    Args:
        t (turtle.Turtle): The turtle object to draw with.
        order (int): The depth of recursion. Higher order means more detail.
        size (float): The length of the side of the current triangle.
    """
    # Base case: This is crucial for recursion!
    # It's the condition that stops the recursion from going on forever.
    # If the order is 0, we just draw a single filled triangle.
    if order == 0:
        t.begin_fill() # Start filling the shape
        for _ in range(3): # A triangle has 3 sides
            t.forward(size) # Move forward by the 'size'
            t.left(120)     # Turn left by 120 degrees (for an equilateral triangle)
        t.end_fill()   # Stop filling the shape
        return # Stop this branch of recursion

    # Recursive step:
    # If the order is greater than 0, we break down the problem
    # into smaller, similar sub-problems.
    # We draw three smaller Sierpinski triangles.

    # 1. Draw the bottom-left smaller triangle:
    # We call draw_sierpinski again, but with a reduced order (order - 1)
    # and half the size (size / 2).
    draw_sierpinski(t, order - 1, size / 2)

    # Move the turtle to the starting position for the bottom-right triangle.
    # This involves moving half the size forward and then turning right.
    t.forward(size / 2)
    draw_sierpinski(t, order - 1, size / 2)

    # Move the turtle to the starting position for the top triangle.
    # This involves moving back half the size, turning left, and moving forward half the size.
    t.backward(size / 2) # Go back to the start of the current section
    t.left(60)           # Turn left to face the top vertex direction
    t.forward(size / 2)  # Move forward to the start of the top triangle
    t.right(60)          # Turn back to the original orientation
    draw_sierpinski(t, order - 1, size / 2)

    # After drawing the three smaller triangles, we need to reposition the turtle
    # back to where it started this recursive call to avoid drawing over previous parts
    # when returning from the recursive calls.
    t.left(60)           # Turn left again
    t.backward(size / 2) # Move back to the original starting point of this call
    t.right(60)          # Turn back to the original orientation

# --- Example Usage ---
if __name__ == "__main__":
    # This block of code runs only when the script is executed directly
    # (not when it's imported as a module).

    # Set up the screen
    screen = turtle.Screen()
    screen.setup(width=800, height=700) # Set the window size
    screen.bgcolor("black")             # Set background color to black for better contrast
    screen.title("Recursive Fractal Art: Sierpinski Triangle") # Set window title

    # Create a turtle object
    artist = turtle.Turtle()
    artist.speed(0)        # Set the speed to the fastest (0) for quick drawing
    artist.penup()         # Lift the pen so it doesn't draw while moving to the starting position
    artist.goto(-150, -100) # Move the turtle to a good starting position for the triangle
    artist.pendown()       # Put the pen down to start drawing
    artist.pencolor("cyan") # Set the pen color to cyan
    artist.fillcolor("deepskyblue") # Set the fill color

    # Define fractal parameters
    fractal_order = 5 # The depth of recursion. Try changing this value (e.g., 3, 4, 6)
    triangle_size = 300 # The initial size of the largest triangle

    # Call the recursive function to draw the fractal
    draw_sierpinski(artist, fractal_order, triangle_size)

    # Hide the turtle when drawing is finished
    artist.hideturtle()

    # Keep the window open until it's manually closed
    screen.mainloop()