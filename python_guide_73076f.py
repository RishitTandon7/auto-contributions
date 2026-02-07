# Algorithmic Art with Pygame: Controlling Shape Movement

# Learning Objective:
# This tutorial will teach you how to create simple algorithmic art
# by controlling the movement of basic shapes (rectangles) on a Pygame
# window. We will explore how to:
# 1. Initialize Pygame.
# 2. Create a display window.
# 3. Define and draw a rectangle.
# 4. Implement basic movement for the rectangle using variables.
# 5. Update the screen to show the changes.
# 6. Handle the game loop and quitting.

# Import the Pygame library, which provides tools for creating games and multimedia applications.
import pygame

# --- Constants ---
# Constants are variables whose values should not change. They are usually
# written in ALL CAPS. Using constants makes code more readable and maintainable.

# Define the dimensions of the game window.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define colors using RGB tuples (Red, Green, Blue). Each value ranges from 0 to 255.
# White is (255, 255, 255), Black is (0, 0, 0).
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# --- Game Initialization ---
# Pygame needs to be initialized before it can be used.
pygame.init()

# Create the display surface (the window where our art will be drawn).
# We pass the screen dimensions as a tuple.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window. This appears in the window's title bar.
pygame.display.set_caption("Algorithmic Art: Moving Rectangle")

# --- Shape Properties ---
# These variables will control the position and size of our rectangle.
# We'll use them to make the rectangle move.

# Initial position (top-left corner of the rectangle)
rect_x = 50
rect_y = 50

# Size of the rectangle (width, height)
rect_width = 100
rect_height = 75

# Movement speed (how many pixels the rectangle moves per frame)
# We'll move it both horizontally (x) and vertically (y).
move_speed_x = 2
move_speed_y = 1

# --- Game Loop ---
# The game loop is the heart of any Pygame application.
# It continuously runs, handling events, updating game logic, and drawing to the screen.
running = True  # A flag to control whether the loop should continue.
while running:
    # --- Event Handling ---
    # Pygame needs to process events (like keyboard presses, mouse clicks, or closing the window).
    # We iterate through all the events that have occurred since the last check.
    for event in pygame.event.get():
        # If the user clicks the close button (the 'X' in the corner of the window)...
        if event.type == pygame.QUIT:
            running = False  # ...set the running flag to False to exit the loop.

    # --- Game Logic (Updating Shape Position) ---
    # This is where we change the state of our game elements.
    # In this case, we update the rectangle's position to make it move.

    # Update the x-coordinate of the rectangle.
    rect_x += move_speed_x
    # Update the y-coordinate of the rectangle.
    rect_y += move_speed_y

    # --- Boundary Checking ---
    # We want the rectangle to bounce off the edges of the screen.
    # If the rectangle hits the right edge (its right side is past the screen width)
    # or the left edge (its left side is before the screen width)...
    if rect_x + rect_width > SCREEN_WIDTH or rect_x < 0:
        # ...reverse the horizontal movement direction by multiplying the speed by -1.
        move_speed_x *= -1

    # If the rectangle hits the bottom edge (its bottom side is past the screen height)
    # or the top edge (its top side is before the screen height)...
    if rect_y + rect_height > SCREEN_HEIGHT or rect_y < 0:
        # ...reverse the vertical movement direction.
        move_speed_y *= -1

    # --- Drawing ---
    # This section is responsible for rendering the visual elements on the screen.
    # We do this by drawing shapes onto the 'screen' surface.

    # First, fill the screen with a background color. This clears the screen
    # from the previous frame, preventing trails of old drawings.
    screen.fill(BLACK)  # Using our BLACK constant for the background.

    # Draw the rectangle.
    # pygame.draw.rect() takes:
    # 1. The surface to draw on (our 'screen').
    # 2. The color of the rectangle (we'll use RED).
    # 3. A tuple representing the rectangle: (x, y, width, height).
    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))

    # --- Update the Display ---
    # After all drawing commands are executed, we need to update the
    # entire screen to show what we've drawn.
    pygame.display.flip()

# --- Quitting Pygame ---
# Once the 'running' loop finishes, we need to properly shut down Pygame.
pygame.quit()
print("Pygame window closed. Art creation finished.")

# --- Example Usage ---
# To run this code:
# 1. Make sure you have Python and Pygame installed.
#    (Install Pygame with: pip install pygame)
# 2. Save the code as a Python file (e.g., moving_art.py).
# 3. Run the file from your terminal: python moving_art.py
# You will see a black window with a red rectangle bouncing around.
# You can experiment by changing the SCREEN_WIDTH, SCREEN_HEIGHT,
# initial rect_x, rect_y, rect_width, rect_height, and move_speed_x, move_speed_y values.