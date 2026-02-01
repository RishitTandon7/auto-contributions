# Learning Objective:
# This tutorial teaches fundamental image manipulation techniques and
# data structures in Python by building a program that generates
# pixel art from simple text descriptions. We will focus on
# representing images as 2D lists (a common data structure) and
# using a library to draw pixels.

# Import the Pillow library (PIL fork) for image manipulation.
# If you don't have it installed, run: pip install Pillow
from PIL import Image, ImageDraw

def create_pixel_art(description):
    """
    Generates a simple pixel art image based on a text description.

    Args:
        description (dict): A dictionary containing pixel art instructions.
                            Expected keys:
                            - 'width' (int): The width of the pixel art canvas.
                            - 'height' (int): The height of the pixel art canvas.
                            - 'background_color' (tuple): RGB tuple for the background (e.g., (255, 255, 255) for white).
                            - 'pixels' (list of dicts): A list where each dict describes a pixel or a shape.
                                Each pixel dict should have:
                                - 'x' (int): The x-coordinate of the pixel.
                                - 'y' (int): The y-coordinate of the pixel.
                                - 'color' (tuple): RGB tuple for the pixel color.
    Returns:
        PIL.Image.Image: A Pillow Image object representing the generated pixel art.
    """

    # Extract dimensions and background color from the description.
    width = description.get('width', 64)  # Default to 64 if not provided
    height = description.get('height', 64) # Default to 64 if not provided
    background_color = description.get('background_color', (0, 0, 0)) # Default to black

    # Create a new blank image. This is our canvas.
    # 'RGB' mode means each pixel has Red, Green, and Blue components.
    # The size is (width, height).
    image = Image.new('RGB', (width, height), background_color)

    # Get a drawing context for the image. This object allows us to draw shapes and pixels.
    draw = ImageDraw.Draw(image)

    # Iterate through the list of pixel instructions.
    # Each 'pixel_instruction' is a dictionary defining a single pixel to draw.
    for pixel_instruction in description.get('pixels', []):
        # Extract x, y coordinates and color from the instruction.
        x = pixel_instruction.get('x')
        y = pixel_instruction.get('y')
        color = pixel_instruction.get('color')

        # Basic validation: ensure we have all necessary information.
        if x is not None and y is not None and color is not None:
            # Draw a single pixel.
            # The draw.point() method takes a coordinate (x, y) and a color.
            # We are essentially setting the color of a single point on our canvas.
            draw.point((x, y), fill=color)

    # Return the created image object.
    return image

# --- Example Usage ---

# Define a simple pixel art description.
# This is a dictionary, a powerful data structure that stores key-value pairs.
# It's perfect for organizing our pixel art's properties.
my_pixel_art_description = {
    'width': 10,  # Our canvas will be 10 pixels wide.
    'height': 10, # And 10 pixels tall.
    'background_color': (255, 255, 255), # White background.
    'pixels': [
        {'x': 2, 'y': 2, 'color': (255, 0, 0)},  # Red pixel at (2, 2)
        {'x': 3, 'y': 2, 'color': (255, 0, 0)},  # Red pixel at (3, 2)
        {'x': 4, 'y': 2, 'color': (255, 0, 0)},  # Red pixel at (4, 2)
        {'x': 3, 'y': 3, 'color': (255, 0, 0)},  # Red pixel at (3, 3)

        {'x': 6, 'y': 7, 'color': (0, 0, 255)},  # Blue pixel at (6, 7)
        {'x': 7, 'y': 7, 'color': (0, 0, 255)},  # Blue pixel at (7, 7)
        {'x': 7, 'y': 6, 'color': (0, 0, 255)},  # Blue pixel at (7, 6)
    ]
}

# Generate the pixel art image using our function.
generated_image = create_pixel_art(my_pixel_art_description)

# Save the generated image to a file.
# This allows us to view our creation!
try:
    generated_image.save("my_pixel_art.png")
    print("Pixel art saved as my_pixel_art.png")
except IOError:
    print("Error: Could not save image. Make sure you have write permissions.")

# Another example: a simple smiley face
smiley_description = {
    'width': 12,
    'height': 12,
    'background_color': (50, 50, 50), # Dark gray background
    'pixels': [
        # Outline of the face (yellow)
        {'x': 1, 'y': 2, 'color': (255, 255, 0)}, {'x': 2, 'y': 2, 'color': (255, 255, 0)}, {'x': 3, 'y': 2, 'color': (255, 255, 0)},
        {'x': 4, 'y': 2, 'color': (255, 255, 0)}, {'x': 5, 'y': 2, 'color': (255, 255, 0)}, {'x': 6, 'y': 2, 'color': (255, 255, 0)},
        {'x': 7, 'y': 2, 'color': (255, 255, 0)}, {'x': 8, 'y': 2, 'color': (255, 255, 0)}, {'x': 9, 'y': 2, 'color': (255, 255, 0)},

        {'x': 1, 'y': 3, 'color': (255, 255, 0)}, {'x': 9, 'y': 3, 'color': (255, 255, 0)},
        {'x': 1, 'y': 4, 'color': (255, 255, 0)}, {'x': 9, 'y': 4, 'color': (255, 255, 0)},
        {'x': 1, 'y': 5, 'color': (255, 255, 0)}, {'x': 9, 'y': 5, 'color': (255, 255, 0)},
        {'x': 1, 'y': 6, 'color': (255, 255, 0)}, {'x': 9, 'y': 6, 'color': (255, 255, 0)},
        {'x': 1, 'y': 7, 'color': (255, 255, 0)}, {'x': 9, 'y': 7, 'color': (255, 255, 0)},
        {'x': 1, 'y': 8, 'color': (255, 255, 0)}, {'x': 9, 'y': 8, 'color': (255, 255, 0)},

        {'x': 2, 'y': 9, 'color': (255, 255, 0)}, {'x': 3, 'y': 9, 'color': (255, 255, 0)},
        {'x': 4, 'y': 9, 'color': (255, 255, 0)}, {'x': 5, 'y': 9, 'color': (255, 255, 0)},
        {'x': 6, 'y': 9, 'color': (255, 255, 0)}, {'x': 7, 'y': 9, 'color': (255, 255, 0)},
        {'x': 8, 'y': 9, 'color': (255, 255, 0)},

        # Eyes (black)
        {'x': 4, 'y': 5, 'color': (0, 0, 0)},
        {'x': 7, 'y': 5, 'color': (0, 0, 0)},

        # Mouth (black)
        {'x': 5, 'y': 7, 'color': (0, 0, 0)},
        {'x': 6, 'y': 7, 'color': (0, 0, 0)},
    ]
}

generated_smiley = create_pixel_art(smiley_description)
try:
    generated_smiley.save("smiley_pixel_art.png")
    print("Smiley pixel art saved as smiley_pixel_art.png")
except IOError:
    print("Error: Could not save image. Make sure you have write permissions.")