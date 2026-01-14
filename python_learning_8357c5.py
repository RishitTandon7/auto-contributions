# Learning Objective:
# This tutorial will teach you how to generate beautiful fractal patterns
# in Python using the concept of recursion and visualizing the results.
# We will focus on a simple fractal called the Sierpinski Triangle
# to demonstrate the power of recursive self-similarity.

# Import necessary libraries for drawing.
# `turtle` is a built-in Python module that provides a simple graphics API,
# perfect for beginners to understand drawing commands and recursion.
import turtle

# --- Configuration ---
# Define the screen dimensions and drawing speed.
# These can be adjusted to change the visual output.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
DRAWING_SPEED = 0 # 0 means fastest, 1-10 are increasing speeds.

# --- Recursive Fractal Generation ---

def draw_sierpinski_triangle(points, level, my_turtle):
    """
    Recursively draws the Sierpinski Triangle.

    Args:
        points (list): A list of three tuples, each representing a corner
                       (x, y) of the current triangle.
        level (int): The current recursion level. This determines how many
                     times we subdivide the triangle.
        my_turtle (turtle.Turtle): The turtle object used for drawing.
    """
    # Base case for recursion:
    # If the recursion level reaches 0, we stop subdividing and draw the triangle.
    # This prevents infinite recursion.
    if level == 0:
        # Plot the triangle using the provided points.
        # `penup()` lifts the pen so the turtle doesn't draw lines
        # while moving to the starting point.
        my_turtle.penup()
        # `goto()` moves the turtle to the specified coordinates.
        my_turtle.goto(points[0])
        # `pendown()` puts the pen down, ready to draw.
        my_turtle.pendown()
        # `goto()` is called for each point to connect them and form a triangle.
        my_turtle.goto(points[1])
        my_turtle.goto(points[2])
        my_turtle.goto(points[0])
        # `penup()` again to avoid drawing lines after the triangle is complete.
        my_turtle.penup()
    else:
        # Recursive step:
        # If the level is greater than 0, we need to further subdivide the triangle.
        # We do this by finding the midpoints of each side and creating three
        # smaller triangles.

        # 1. Calculate midpoints:
        # The midpoint between two points (x1, y1) and (x2, y2) is ((x1+x2)/2, (y1+y2)/2).
        midpoints = [
            # Midpoint of side 1 (points[0] to points[1])
            ((points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2),
            # Midpoint of side 2 (points[1] to points[2])
            ((points[1][0] + points[2][0]) / 2, (points[1][1] + points[2][1]) / 2),
            # Midpoint of side 3 (points[2] to points[0])
            ((points[2][0] + points[0][0]) / 2, (points[2][1] + points[0][1]) / 2)
        ]

        # 2. Recursively call draw_sierpinski_triangle for the three smaller triangles:
        # Each recursive call reduces the `level` by 1.
        # The `points` for each new call are formed by the original vertices
        # and the calculated midpoints.

        # Top triangle: Formed by points[0], midpoint[0], midpoint[2]
        draw_sierpinski_triangle([points[0], midpoints[0], midpoints[2]], level - 1, my_turtle)
        # Left triangle: Formed by points[1], midpoint[0], midpoint[1]
        draw_sierpinski_triangle([points[1], midpoints[0], midpoints[1]], level - 1, my_turtle)
        # Right triangle: Formed by points[2], midpoint[1], midpoint[2]
        draw_sierpinski_triangle([points[2], midpoints[1], midpoints[2]], level - 1, my_turtle)

# --- Initialization and Execution ---

def main():
    """
    Sets up the turtle screen and initiates the Sierpinski Triangle drawing.
    """
    # Set up the screen.
    screen = turtle.Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.title("Sierpinski Triangle Fractal")
    screen.bgcolor("white") # Set background color to white.

    # Create a turtle object.
    # This object will perform all the drawing actions.
    artist = turtle.Turtle()
    artist.speed(DRAWING_SPEED) # Set drawing speed to fastest.
    artist.hideturtle() # Hide the turtle icon for a cleaner drawing.
    artist.penup() # Lift pen initially.

    # Define the initial vertices of the largest triangle.
    # These define the overall shape and size of the fractal.
    # We'll use a large equilateral triangle centered on the screen.
    initial_points = [
        (-250, -150),  # Bottom-left vertex
        (0, 250),      # Top vertex
        (250, -150)    # Bottom-right vertex
    ]

    # Define the desired recursion level.
    # Higher levels create more detailed and complex fractals.
    # Be aware that very high levels can take a long time to render.
    recursion_level = 5

    # Start the recursive drawing process.
    draw_sierpinski_triangle(initial_points, recursion_level, artist)

    # Keep the window open until it's manually closed.
    screen.mainloop()

# --- Example Usage ---
if __name__ == "__main__":
    # This block ensures that main() is called only when the script is executed directly,
    # not when it's imported as a module.
    main()

# How to Run:
# 1. Save the code as a Python file (e.g., fractal_generator.py).
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the script using: python fractal_generator.py
# A window will pop up showing the generated Sierpinski Triangle.

# Further Exploration:
# - Change `recursion_level` to see how it affects the complexity.
# - Modify `initial_points` to create fractals of different sizes and shapes.
# - Experiment with `DRAWING_SPEED` and `screen.bgcolor()`.
# - Research other fractal patterns like the Koch Snowflake or Mandelbrot Set
#   and try to implement them (these might require more advanced techniques).