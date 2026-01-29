# Learning Objective: Explore the power of recursion to generate complex, beautiful fractal patterns using Python's Turtle graphics module.

# Import the turtle module for graphics.
import turtle

# --- Fractal Generation Function ---
# This function uses recursion to draw a fractal.
# Recursion is when a function calls itself to solve smaller versions of the same problem.
# Think of it like a set of Russian nesting dolls – each doll contains a smaller, similar doll.

def draw_fractal(t, order, size):
    """
    Draws a fractal pattern recursively.

    Args:
        t: The turtle object to draw with.
        order: The depth of the recursion. Higher order means more detail.
        size: The current length of the line segment to draw.
    """

    # Base Case: This is the stopping condition for our recursion.
    # When the order reaches 0, we stop drawing and just draw a simple line.
    # Without a base case, the recursion would go on forever (or until Python runs out of memory).
    if order == 0:
        t.forward(size)  # Draw a line segment of the given size.
        return  # Exit the function, stopping this branch of recursion.

    # Recursive Step: This is where the magic happens!
    # We divide the current problem (drawing a line of 'size') into smaller, similar sub-problems.

    # 1. Calculate the size for the smaller segments.
    # We divide the current size by 3 because each segment will be broken into three smaller parts.
    new_size = size / 3

    # 2. Recursively draw the first part of the fractal.
    # We call draw_fractal again, but with a decreased order (moving closer to the base case)
    # and the calculated new_size.
    draw_fractal(t, order - 1, new_size)

    # 3. Turn left and draw the second part.
    # This turn creates the angles that form the fractal shape.
    t.left(60)  # Turn 60 degrees to the left.
    draw_fractal(t, order - 1, new_size)

    # 4. Turn right twice and draw the third part.
    # We turn right 120 degrees (60 + 60) to get back to the original direction
    # and then another 60 degrees to prepare for the next segment.
    t.right(120)
    draw_fractal(t, order - 1, new_size)

    # 5. Turn left and draw the fourth part.
    # We turn left 60 degrees to get back to the direction of the first segment
    # and draw the final part.
    t.left(60)
    draw_fractal(t, order - 1, new_size)

# --- Setup and Example Usage ---

if __name__ == "__main__":
    # Create a screen object to manage the drawing window.
    screen = turtle.Screen()
    screen.setup(width=800, height=600)  # Set the dimensions of the window.
    screen.bgcolor("black")  # Set the background color to black for better contrast.
    screen.title("Recursive Fractal Art")  # Set the title of the window.

    # Create a turtle object. This is our "pen" for drawing.
    artist = turtle.Turtle()
    artist.speed(0)  # Set the drawing speed to the fastest (0).
    artist.color("cyan")  # Set the drawing color to cyan.
    artist.penup()  # Lift the pen so we don't draw while moving to the starting position.
    artist.goto(-200, 100)  # Move the turtle to a starting position.
    artist.pendown()  # Put the pen down to start drawing.

    # --- Parameters for the fractal ---
    # 'fractal_order': Controls the complexity and detail of the fractal.
    #                  Higher values create more intricate patterns but take longer to draw.
    # 'initial_size': The initial length of the main line segment.
    fractal_order = 4  # Try changing this to 0, 1, 2, 3, 5 to see different levels of detail.
    initial_size = 400  # The total width of the fractal.

    # Call the recursive function to draw the fractal.
    # The turtle will start drawing from its current position.
    draw_fractal(artist, fractal_order, initial_size)

    # Hide the turtle cursor after drawing is complete.
    artist.hideturtle()

    # Keep the window open until it's manually closed.
    screen.mainloop()