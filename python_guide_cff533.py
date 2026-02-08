# Learning Objective: Programmatically create abstract digital art using Python's Pillow library and random color generation.
# This tutorial will guide you through generating unique, abstract images by drawing random shapes with random colors onto a canvas.
# We will focus on understanding how to manipulate pixels and colors with Pillow to create visual outputs.

# Import the Pillow library, specifically the Image and ImageDraw modules.
# Image is used for creating and manipulating images.
# ImageDraw provides drawing capabilities on an Image object.
from PIL import Image, ImageDraw
# Import the 'random' module to generate random numbers for colors and positions.
import random

# --- Configuration ---
# Define the dimensions of our canvas (the image).
IMAGE_WIDTH = 800
IMAGE_HEIGHT = 600

# Define the number of shapes we want to draw on the canvas.
NUM_SHAPES = 50

# Define the maximum size of the shapes (in pixels).
MAX_SHAPE_SIZE = 100

# --- Helper Function for Random Color Generation ---
def generate_random_color():
    # Generates a random RGB color tuple.
    # RGB stands for Red, Green, Blue. Each component can be an integer from 0 to 255.
    # 0 means no intensity of that color, 255 means full intensity.
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    # The tuple (red, green, blue) represents a specific color.
    return (red, green, blue)

# --- Main Art Generation Function ---
def create_abstract_art(width, height, num_shapes, max_shape_size):
    # Create a new blank image with a white background.
    # 'RGB' mode means the image will use Red, Green, and Blue channels for color.
    # (width, height) specifies the image dimensions.
    # (255, 255, 255) is the color white in RGB.
    image = Image.new('RGB', (width, height), (255, 255, 255))

    # Create a drawing object that we can use to draw on the image.
    draw = ImageDraw.Draw(image)

    # Loop to draw multiple random shapes.
    for _ in range(num_shapes):
        # Generate a random color for the current shape.
        color = generate_random_color()

        # Generate random coordinates for the shape's bounding box.
        # The bounding box is a rectangle that defines the area where the shape will be drawn.
        # We ensure the coordinates are within the image bounds.
        x1 = random.randint(0, width - 1)
        y1 = random.randint(0, height - 1)
        x2 = random.randint(x1, min(x1 + max_shape_size, width - 1))
        y2 = random.randint(y1, min(y1 + max_shape_size, height - 1))

        # Choose a random shape type to draw.
        # For simplicity, we'll stick to rectangles and ellipses.
        shape_type = random.choice(['rectangle', 'ellipse'])

        # Draw the chosen shape with the random color.
        if shape_type == 'rectangle':
            # The rectangle method takes a bounding box tuple: (x1, y1, x2, y2).
            # 'fill' specifies the color to fill the rectangle with.
            draw.rectangle([x1, y1, x2, y2], fill=color)
        elif shape_type == 'ellipse':
            # The ellipse method also takes a bounding box tuple.
            # It draws an ellipse within the defined bounding box.
            draw.ellipse([x1, y1, x2, y2], fill=color)

    # Return the generated image object.
    return image

# --- Example Usage ---
if __name__ == "__main__":
    # This block of code runs only when the script is executed directly (not imported as a module).

    print("Generating abstract digital art...")

    # Call the function to create the art with our configured parameters.
    abstract_artwork = create_abstract_art(IMAGE_WIDTH, IMAGE_HEIGHT, NUM_SHAPES, MAX_SHAPE_SIZE)

    # Define a filename for saving the artwork.
    output_filename = "abstract_art.png"

    # Save the generated image to a file.
    # PNG format is good for preserving image quality.
    abstract_artwork.save(output_filename)

    print(f"Abstract art saved successfully as {output_filename}")
    print("Open the file to see your creation!")

# End of tutorial. You can now run this script and experiment with changing
# IMAGE_WIDTH, IMAGE_HEIGHT, NUM_SHAPES, and MAX_SHAPE_SIZE to create different art.
# You could also explore adding other shapes like lines or polygons from ImageDraw.