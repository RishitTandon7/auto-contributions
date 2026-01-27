# Learning Objective:
# This tutorial will teach you how to create beautiful fractal patterns
# using the concept of recursion and the Python turtle graphics module.
# We will focus on understanding how a simple rule can generate complex
# and self-similar shapes.

# Import the turtle module, which provides graphics capabilities.
import turtle

# --- The Recursive Fractal Function ---

def draw_fractal(turtle_obj, length, level):
    """
    This function draws a fractal pattern recursively.

    Args:
        turtle_obj (turtle.Turtle): The turtle object used for drawing.
        length (int): The current length of the line segment to draw.
        level (int): The current recursion depth or level.
    """

    # --- Base Case ---
    # The base case is crucial for any recursive function. It defines when
    # the recursion stops. Without a base case, the function would call
    # itself infinitely, leading to a stack overflow error.
    # In this fractal, when the level reaches 0, we simply draw a line
    # of the specified length and stop.
    if level == 0:
        turtle_obj.forward(length)  # Move the turtle forward by 'length' pixels.
        return  # Exit the function, ending this branch of recursion.

    # --- Recursive Step ---
    # This is where the magic happens! We break down the problem into
    # smaller, self-similar subproblems.
    # For this fractal (a simple line fractal, similar to a Koch curve segment),
    # we divide the current line into three equal parts.
    # For each part, we apply a transformation and then recursively call
    # draw_fractal on that smaller part.

    # 1. Draw the first third of the line.
    # We reduce the length by a factor (here, we divide by 3) for the next level.
    new_length = length / 3

    # Recursively call draw_fractal for the first segment.
    # This means the same logic will be applied to this smaller segment.
    draw_fractal(turtle_obj, new_length, level - 1)

    # 2. Turn left and draw the "peak" or "bump".
    # This is where the fractal shape emerges. We turn the turtle
    # and draw another fractal pattern. The angle (60 degrees) and the
    # length are key to the specific fractal shape.
    turtle_obj.left(60)  # Turn the turtle 60 degrees to the left.
    draw_fractal(turtle_obj, new_length, level - 1)

    # 3. Turn right to face the original direction and draw the second third.
    # We need to correct the turtle's orientation after the left turn.
    turtle_obj.right(120) # Turn right by 120 degrees (60 + 60 for correction).
    draw_fractal(turtle_obj, new_length, level - 1)

    # 4. Turn left and draw the last third of the line.
    # Another turn to draw the final segment of this level.
    turtle_obj.left(60)  # Turn left by 60 degrees.
    draw_fractal(turtle_obj, new_length, level - 1)

    # After drawing all parts of the current level, the function returns,
    # allowing the previous level of recursion to continue.

# --- Example Usage ---

if __name__ == "__main__":
    # This block of code runs only when the script is executed directly
    # (not when it's imported as a module).

    # Set up the screen for drawing.
    screen = turtle.Screen()
    screen.setup(width=800, height=600)  # Set the window size.
    screen.bgcolor("lightblue")        # Set the background color.
    screen.title("Recursive Fractal Art") # Set the window title.

    # Create a turtle object. This is our drawing pen.
    artist = turtle.Turtle()
    artist.speed(0)  # Set the fastest drawing speed (0 means fastest).
    artist.penup()   # Lift the pen so it doesn't draw while moving to position.
    artist.goto(-200, 0) # Move the turtle to a starting position.
    artist.pendown() # Put the pen down to start drawing.
    artist.color("darkgreen") # Set the drawing color.
    artist.pensize(2) # Set the thickness of the pen.

    # Define the initial parameters for our fractal.
    initial_length = 400  # The total length of the first line segment.
    recursion_level = 4   # The depth of the recursion. Higher levels mean more detail.

    # Call the draw_fractal function to start drawing.
    # This will initiate the recursive process.
    print(f"Drawing fractal with length {initial_length} and level {recursion_level}...")
    draw_fractal(artist, initial_length, recursion_level)
    print("Fractal drawing complete!")

    # Hide the turtle cursor after drawing.
    artist.hideturtle()

    # Keep the window open until it's manually closed.
    screen.mainloop()