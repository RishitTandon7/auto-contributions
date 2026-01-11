# Learning Objective:
# This tutorial will teach you how to generate visually stunning fractal art
# using recursion and Python's Turtle graphics library. We will focus on
# the concept of self-similarity, where a shape is made up of smaller
# copies of itself, and how to implement this with a recursive function.

import turtle

# --- Configuration ---
# These settings control the appearance and behavior of our fractal.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
BACKGROUND_COLOR = "black"
PEN_COLOR = "cyan"
PEN_WIDTH = 1
DRAWING_SPEED = 0 # 0 is the fastest, 1 is slowest, 10 is fast
INITIAL_PEN_SIZE = 1 # Starting thickness of the lines

# --- Fractal Generation Function ---

def draw_fractal(t, branch_length, level):
    """
    Recursively draws a fractal pattern.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        branch_length (float): The current length of the branch to draw.
        level (int): The current recursion level. This determines how many
                     times the fractal will subdivide.
    """

    # Base Case:
    # This is the stopping condition for our recursion.
    # When the level reaches 0, we stop drawing further branches.
    # This prevents infinite recursion and defines the smallest detail.
    if level == 0:
        return

    # --- Drawing the current branch ---
    # Set the pen size for the current branch. We can make it thinner
    # as the branches get smaller and more numerous.
    t.pensize(max(1, level * 0.5)) # Ensure pensize is at least 1

    # Move the turtle forward by the current branch length.
    t.forward(branch_length)

    # --- Recursive Steps ---
    # This is where the magic of recursion happens. We call the function
    # again for smaller branches.

    # 1. Save the turtle's current state (position and heading).
    # This is crucial for returning to this point after drawing a sub-fractal.
    # We push the state onto a conceptual stack.
    current_position = t.position()
    current_heading = t.heading()

    # 2. Draw the first sub-fractal (e.g., left branch).
    # We reduce the branch length by a factor (e.g., 0.7) and decrement the level.
    # We also turn the turtle to create an angle.
    t.left(30) # Turn left by 30 degrees
    draw_fractal(t, branch_length * 0.7, level - 1)

    # 3. Restore the turtle's state.
    # We pop the saved state to return to where we were before drawing the left branch.
    t.penup() # Lift pen to avoid drawing while repositioning
    t.goto(current_position)
    t.setheading(current_heading)
    t.pendown() # Put pen down to continue drawing

    # 4. Draw the second sub-fractal (e.g., right branch).
    # Again, we reduce branch length and level, and turn the turtle.
    t.right(60) # Turn right by 60 degrees (creating a 30-degree spread from original)
    draw_fractal(t, branch_length * 0.7, level - 1)

    # 5. Restore the turtle's state again for the next level or to return to parent.
    t.penup()
    t.goto(current_position)
    t.setheading(current_heading)
    t.pendown()

    # 6. (Optional) Draw a third branch for more complexity, if desired.
    # For this example, we'll keep it to two branches for clarity,
    # but you could add more branches here by repeating the save/draw/restore steps.

    # --- Backtracking ---
    # After drawing all sub-fractals from this level, the function returns.
    # The turtle is now back at the end of the parent branch, ready for
    # its own backtracking or for the next sibling branch to be drawn by its parent.
    # We don't need explicit "pop" operations here because Python's function
    # call stack handles this automatically.

# --- Setup and Execution ---

def main():
    """
    Sets up the turtle screen and initiates the fractal drawing.
    """
    # Initialize the screen
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor(BACKGROUND_COLOR)
    screen.title("Recursive Fractal Art")

    # Create a turtle object
    artist = turtle.Turtle()
    artist.speed(DRAWING_SPEED)
    artist.color(PEN_COLOR)
    artist.pensize(INITIAL_PEN_SIZE)
    artist.hideturtle() # Hide the turtle arrow for a cleaner look
    artist.penup()      # Lift the pen initially
    artist.goto(0, -SCREEN_HEIGHT // 3) # Start position for the base of the fractal
    artist.left(90)     # Point the turtle upwards
    artist.pendown()    # Put the pen down to start drawing

    # --- Example Usage ---
    # Call the recursive function to draw the fractal.
    # Parameters:
    #   artist: The turtle object.
    #   branch_length: The initial length of the main branch.
    #   level: The maximum depth of recursion. Higher levels create more detail.
    initial_branch_length = 150
    recursion_level = 10 # Adjust this value to control complexity

    draw_fractal(artist, initial_branch_length, recursion_level)

    # Keep the window open until it's manually closed
    screen.mainloop()

if __name__ == "__main__":
    main()