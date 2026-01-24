"""
Learning Objective:
This tutorial will guide you through programmatically generating beautiful fractal art
using the concept of recursion and basic color manipulation in Python. We will focus
on the Sierpinski Triangle as a visual example.
"""

# Import necessary libraries
import turtle  # For drawing graphics
import random  # For generating random colors (optional, but adds variety)

# --- Core Fractal Generation (Recursion) ---

def draw_triangle(points, color, t):
    """
    Draws a single triangle given three points.

    Args:
        points (list): A list of three (x, y) tuples representing the vertices of the triangle.
        color (str): The fill color for the triangle.
        t (turtle.Turtle): The turtle object used for drawing.
    """
    t.fillcolor(color)  # Set the fill color for the upcoming shape
    t.up()              # Lift the pen to move without drawing
    t.goto(points[0])   # Move to the first vertex
    t.down()            # Put the pen down to start drawing
    t.begin_fill()      # Start filling the shape
    t.goto(points[1])   # Draw a line to the second vertex
    t.goto(points[2])   # Draw a line to the third vertex
    t.goto(points[0])   # Draw a line back to the first vertex to close the shape
    t.end_fill()        # End the filling process

def get_midpoint(p1, p2):
    """
    Calculates the midpoint between two given points.

    Args:
        p1 (tuple): The first point (x, y).
        p2 (tuple): The second point (x, y).

    Returns:
        tuple: The midpoint (x, y).
    """
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, degree, t):
    """
    Recursively draws the Sierpinski Triangle.

    The Sierpinski triangle is created by repeatedly applying a transformation
    to an initial shape. In this case, we start with a large triangle and
    then divide it into three smaller triangles, ignoring the middle one,
    and repeat this process on the remaining three.

    Args:
        points (list): A list of three (x, y) tuples representing the current
                       vertices of the triangle to subdivide.
        degree (int): The current level of recursion. This determines how many
                      times the subdivision process is repeated. A higher degree
                      results in a more detailed fractal.
        t (turtle.Turtle): The turtle object used for drawing.
    """
    # Base Case: If the degree is 0, we stop the recursion.
    # This is crucial to prevent infinite recursion.
    if degree == 0:
        return

    # Recursive Step:
    # 1. Draw the current triangle.
    # We can use a simple color or a color based on the recursion depth.
    # For simplicity, let's use a single color for the initial triangles.
    # More advanced color manipulation can be added here.
    draw_triangle(points, 'blue', t)

    # 2. Calculate the midpoints of the sides of the current triangle.
    # These midpoints will define the vertices of the smaller triangles.
    mid1 = get_midpoint(points[0], points[1])
    mid2 = get_midpoint(points[1], points[2])
    mid3 = get_midpoint(points[2], points[0])

    # 3. Recursively call sierpinski on the three new, smaller triangles.
    # Each recursive call reduces the 'degree' by 1.
    # This creates the self-similar structure characteristic of fractals.

    # Top triangle
    sierpinski([points[0], mid1, mid3], degree - 1, t)
    # Left triangle
    sierpinski([mid1, points[1], mid2], degree - 1, t)
    # Right triangle
    sierpinski([mid3, mid2, points[2]], degree - 1, t)

# --- Color Manipulation Function (Example) ---

def color_based_on_degree(degree_level):
    """
    Generates a color based on the current recursion degree.
    This is a simple example; more complex color schemes are possible.

    Args:
        degree_level (int): The current recursion depth.

    Returns:
        str: A color string (e.g., 'red', 'green', '#RRGGBB').
    """
    # We can use HSV color space for smoother transitions.
    # Hue cycles through the rainbow. Saturation and Value control brightness/intensity.
    # This maps the degree level to a hue value between 0 and 1.
    hue = (degree_level % 10) / 10.0  # Cycle through 10 colors
    return f"hsl({hue * 360}, 100%, 50%)" # Convert hue to degrees for hsl()

def sierpinski_with_color(points, degree, t):
    """
    Recursively draws the Sierpinski Triangle with color changing based on depth.

    Args:
        points (list): A list of three (x, y) tuples representing the current
                       vertices of the triangle to subdivide.
        degree (int): The current level of recursion.
        t (turtle.Turtle): The turtle object used for drawing.
    """
    if degree == 0:
        return

    # Draw the current triangle with a color determined by its depth
    draw_triangle(points, color_based_on_degree(degree), t)

    mid1 = get_midpoint(points[0], points[1])
    mid2 = get_midpoint(points[1], points[2])
    mid3 = get_midpoint(points[2], points[0])

    # Recursive calls for the sub-triangles, passing the decremented degree
    sierpinski_with_color([points[0], mid1, mid3], degree - 1, t)
    sierpinski_with_color([mid1, points[1], mid2], degree - 1, t)
    sierpinski_with_color([mid3, mid2, points[2]], degree - 1, t)


# --- Main execution block ---

if __name__ == "__main__":
    # Set up the turtle screen
    screen = turtle.Screen()
    screen.setup(width=800, height=700)  # Set screen dimensions
    screen.bgcolor("black")            # Set background color
    screen.title("Sierpinski Triangle Fractal") # Set window title

    # Create a turtle object
    my_turtle = turtle.Turtle()
    my_turtle.speed(0)          # Set speed to fastest (0)
    my_turtle.penup()           # Lift pen initially to position
    my_turtle.hideturtle()      # Hide the turtle icon for a cleaner look

    # Define the initial vertices of the largest triangle
    # These points form an equilateral triangle.
    initial_points = [(-200, -150), (0, 250), (200, -150)]

    # Define the desired recursion depth.
    # Higher degrees create more intricate fractals but take longer to render.
    recursion_degree = 5

    # --- Example Usage ---

    # Option 1: Generate a Sierpinski Triangle with a single color
    # print("Generating Sierpinski Triangle with a single color...")
    # sierpinski(initial_points, recursion_degree, my_turtle)

    # Option 2: Generate a Sierpinski Triangle with color changing based on depth
    print(f"Generating Sierpinski Triangle with color based on recursion depth ({recursion_degree})...")
    sierpinski_with_color(initial_points, recursion_degree, my_turtle)


    # Keep the window open until it's manually closed
    screen.mainloop()