# Learning Objective:
# This tutorial will teach you how to generate beautiful fractal art
# using the concept of recursion and Python's built-in Turtle graphics module.
# We will focus on creating a Sierpinski Triangle, a classic fractal,
# to demonstrate how a simple rule repeated over and over can create complex patterns.

import turtle

# --- Configuration ---
# These settings control the appearance and behavior of our fractal.
# You can experiment by changing these values!

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DRAW_SPEED = 0  # 0 is the fastest, 1 is slowest, 10 is fast
PEN_COLOR = "blue"
BACKGROUND_COLOR = "white"
INITIAL_SIZE = 300 # The side length of the initial large triangle

# --- Helper Functions ---

def setup_screen(width, height, bg_color):
    """
    Initializes and configures the turtle screen.
    This function sets up the drawing canvas.
    """
    screen = turtle.Screen()
    screen.setup(width=width, height=height)
    screen.bgcolor(bg_color)
    screen.title("Recursive Fractal Art: Sierpinski Triangle")
    return screen

def setup_turtle(pen_color, speed):
    """
    Initializes and configures the turtle object.
    This function creates our drawing "pen".
    """
    t = turtle.Turtle()
    t.pencolor(pen_color)
    t.speed(speed)
    t.hideturtle() # Hide the turtle icon to see the art better
    return t

# --- Core Recursive Function ---

def draw_triangle(t, points, level):
    """
    Recursively draws a Sierpinski Triangle.

    Args:
        t (turtle.Turtle): The turtle object to draw with.
        points (list): A list of three tuples, each representing the (x, y)
                       coordinates of a vertex of the triangle.
        level (int): The current recursion level. This controls how many
                     sub-triangles are drawn.
    """
    # Base Case: If the recursion level is 0, we stop.
    # This is crucial for any recursive function to prevent infinite loops.
    # At this level, we draw a small filled triangle.
    if level == 0:
        t.penup()
        t.goto(points[0]) # Move to the first point without drawing
        t.pendown()
        t.begin_fill() # Start filling the shape
        t.goto(points[1])
        t.goto(points[2])
        t.goto(points[0]) # Close the triangle
        t.end_fill() # Finish filling
        return # Stop this branch of recursion

    # Recursive Step: If level is greater than 0, we divide the problem.
    # We find the midpoints of each side of the current triangle.
    midpoints = [
        get_midpoint(points[0], points[1]), # Midpoint between point 0 and point 1
        get_midpoint(points[1], points[2]), # Midpoint between point 1 and point 2
        get_midpoint(points[2], points[0])  # Midpoint between point 2 and point 0
    ]

    # Now, we recursively call draw_triangle for the three smaller triangles formed
    # by the original vertices and the midpoints.
    # We decrement the level for each recursive call.
    # This process creates the "holes" in the Sierpinski Triangle.
    draw_triangle(t, [points[0], midpoints[0], midpoints[2]], level - 1)
    draw_triangle(t, [points[1], midpoints[1], midpoints[0]], level - 1)
    draw_triangle(t, [points[2], midpoints[2], midpoints[1]], level - 1)

def get_midpoint(p1, p2):
    """
    Calculates the midpoint between two points (x, y).

    Args:
        p1 (tuple): The first point (x1, y1).
        p2 (tuple): The second point (x2, y2).

    Returns:
        tuple: The midpoint (x_mid, y_mid).
    """
    # The midpoint formula is (x1 + x2) / 2 and (y1 + y2) / 2.
    x_mid = (p1[0] + p2[0]) / 2
    y_mid = (p1[1] + p2[1]) / 2
    return (x_mid, y_mid)

# --- Main Execution ---

def main():
    """
    Sets up the drawing environment and initiates the fractal drawing process.
    This is the main entry point for our program.
    """
    screen = setup_screen(SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR)
    my_turtle = setup_turtle(PEN_COLOR, DRAW_SPEED)

    # Define the initial large triangle.
    # We place it in the center of the screen.
    # The height of an equilateral triangle with side 's' is s * sqrt(3) / 2.
    # We use this to position the top vertex.
    height = INITIAL_SIZE * (3**0.5) / 2
    initial_points = [
        (-INITIAL_SIZE / 2, -height / 2), # Bottom-left vertex
        (INITIAL_SIZE / 2, -height / 2),  # Bottom-right vertex
        (0, height / 2)                   # Top vertex
    ]

    # Set the recursion depth.
    # Higher levels create more detailed fractals but take longer to draw.
    recursion_level = 5

    # Start drawing the Sierpinski Triangle.
    # The first call to draw_triangle is with the initial points and level.
    print(f"Drawing Sierpinski Triangle with level {recursion_level}...")
    draw_triangle(my_turtle, initial_points, recursion_level)
    print("Drawing complete!")

    # Keep the window open until it's manually closed.
    screen.mainloop()

# --- Example Usage ---
if __name__ == "__main__":
    main()