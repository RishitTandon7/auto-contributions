# Learning Objective:
# This tutorial demonstrates how to visualize and interactively explore
# fractal patterns using Python's turtle graphics and the concept of recursion.
# We will focus on creating a Sierpinski Triangle, a classic fractal,
# and highlight how recursive calls build increasingly complex shapes.

import turtle

# --- Configuration ---
# This section defines constants that control the appearance and behavior
# of our fractal generation. Modifying these values can lead to different
# visual outcomes and exploration of fractal properties.

SCREEN_WIDTH = 800   # Width of the turtle graphics window
SCREEN_HEIGHT = 800  # Height of the turtle graphics window
INITIAL_SIZE = 400   # The side length of the initial triangle
RECURSION_DEPTH = 4  # How many times the fractal pattern will repeat
PEN_COLOR = "blue"   # Color of the lines drawn by the turtle
FILL_COLOR_BASE = "yellow" # Color for the base-level triangles
FILL_COLOR_RECURSIVE = "red" # Color for recursively generated triangles
DRAW_SPEED = 0       # Turtle drawing speed (0 is fastest, 1-10 are slower)

# --- Recursive Fractal Function ---

def draw_sierpinski(t, order, size, fill_color):
    """
    Recursively draws a Sierpinski Triangle.

    Args:
        t (turtle.Turtle): The turtle object to draw with.
        order (int): The current recursion depth. Controls complexity.
        size (float): The length of the side of the current triangle.
        fill_color (str): The color to fill the current triangle with.
    """
    # Base Case: When the recursion order reaches 0, we stop drawing.
    # This is crucial for preventing infinite recursion.
    if order == 0:
        # For the smallest triangles, we fill them to make the pattern visible.
        t.fillcolor(fill_color)
        t.begin_fill()
        for _ in range(3): # Draw a triangle
            t.forward(size)
            t.left(120)
        t.end_fill()
        return # Exit the function, returning to the caller

    # Recursive Step: If order is greater than 0, we divide the problem
    # into smaller, similar sub-problems.
    else:
        # The key idea of Sierpinski is to draw three smaller Sierpinski
        # triangles, each at a corner of the current triangle.
        # The size of each sub-triangle is half the current size.

        # 1. Draw the bottom-left sub-triangle
        # We'll use a slightly different fill color for recursive levels
        # to visually distinguish them.
        draw_sierpinski(t, order - 1, size / 2, FILL_COLOR_RECURSIVE)

        # After drawing the first sub-triangle, we need to move the turtle
        # to the starting position for the next one.
        t.forward(size / 2)

        # 2. Draw the bottom-right sub-triangle
        draw_sierpinski(t, order - 1, size / 2, FILL_COLOR_RECURSIVE)

        # Move the turtle to the correct position for the top sub-triangle.
        # This involves moving back to the original corner, then forward
        # by half the size, and then turning to face upwards.
        t.backward(size / 2)
        t.left(60)
        t.forward(size / 2)
        t.right(60)

        # 3. Draw the top sub-triangle
        draw_sierpinski(t, order - 1, size / 2, FILL_COLOR_RECURSIVE)

        # Finally, move the turtle back to the original starting point
        # and orientation for the current level, ready for the caller.
        t.left(60)
        t.backward(size / 2)
        t.right(60)


# --- Main Execution Block ---

if __name__ == "__main__":
    # Set up the screen for drawing
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor("white") # Background color of the window
    screen.title("Sierpinski Triangle Fractal Explorer")

    # Create a turtle object
    fractal_turtle = turtle.Turtle()
    fractal_turtle.speed(DRAW_SPEED) # Set the drawing speed
    fractal_turtle.color(PEN_COLOR)   # Set the pen color

    # Position the turtle to start drawing the initial triangle.
    # We want the triangle to be centered and pointing upwards.
    fractal_turtle.penup() # Lift the pen so we don't draw while moving
    fractal_turtle.goto(-INITIAL_SIZE / 2, -INITIAL_SIZE / (2 * (3**0.5))) # Center the base
    fractal_turtle.pendown() # Put the pen down to start drawing

    # Start the fractal generation process.
    # We pass the turtle object, the desired recursion depth,
    # the initial size, and the fill color for the initial triangle.
    print(f"Generating Sierpinski Triangle with recursion depth: {RECURSION_DEPTH}")
    draw_sierpinski(fractal_turtle, RECURSION_DEPTH, INITIAL_SIZE, FILL_COLOR_BASE)

    # Hide the turtle cursor after drawing is complete
    fractal_turtle.hideturtle()

    # Keep the window open until it's manually closed
    screen.mainloop()

# --- How to Use and Explore ---
# 1. Run this Python script.
# 2. A graphics window will appear, showing the Sierpinski Triangle.
# 3. To explore different patterns:
#    - Modify the RECURSION_DEPTH constant (e.g., 3, 5, 6). Higher values create
#      more intricate patterns but take longer to draw.
#    - Change the INITIAL_SIZE to make the overall fractal larger or smaller.
#    - Experiment with PEN_COLOR, FILL_COLOR_BASE, and FILL_COLOR_RECURSIVE.
# 4. Observe how the `draw_sierpinski` function calls itself with decreasing
#    `order` and `size`. This is the essence of recursion.
# 5. The base case (`order == 0`) stops the recursion, and the recursive step
#    breaks down the problem into smaller, identical tasks.