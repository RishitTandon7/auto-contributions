# Fractal Art Generator Tutorial
#
# Learning Objective: This tutorial will teach you how to generate
# mesmerizing fractal art using the power of recursion and the
# Pillow library in Python. We will focus on understanding how
# recursive functions can be used to create infinitely complex
# patterns that repeat at different scales.

# Import the Pillow library for image manipulation.
# Pillow (PIL fork) is a powerful image processing library for Python.
# We'll use it to create a blank canvas and draw pixels on it.
from PIL import Image

# Define the main recursive function to draw the fractal.
# This function will call itself to draw smaller versions of the pattern.
def draw_fractal_recursive(image, x, y, size, depth):
    # Base Case: If the depth of recursion reaches 0, we stop drawing.
    # This prevents infinite recursion and defines the smallest detail level.
    if depth == 0:
        return

    # Get the dimensions of the image to ensure we stay within bounds.
    img_width, img_height = image.size

    # Calculate the color based on the current recursion depth.
    # We use 'depth' to create variations in color, making the fractal visually
    # interesting. A simple linear mapping is used here.
    # We ensure the color values are within the valid range (0-255).
    color_value = max(0, min(255, 255 - depth * 40))
    color = (color_value, color_value, color_value) # Grayscale color

    # Draw a rectangle (or a point if size is small) at the current position.
    # This represents the current level of the fractal.
    # We ensure coordinates are within image bounds.
    x1 = max(0, x - size // 2)
    y1 = max(0, y - size // 2)
    x2 = min(img_width - 1, x + size // 2)
    y2 = min(img_height - 1, y + size // 2)

    # Draw the rectangle if it has a positive area.
    if x2 > x1 and y2 > y1:
        # For simplicity, we'll just fill a square. In more complex fractals,
        # you might draw lines or more intricate shapes.
        # The 'putpixel' method is less efficient for larger areas than drawing
        # rectangles, but it clearly illustrates drawing individual elements.
        # For this basic example, we draw a small square for visual representation.
        for px in range(x1, x2 + 1):
            for py in range(y1, y2 + 1):
                image.putpixel((px, py), color)

    # Recursive Step: Call the function again for smaller, offset versions.
    # The 'size' is reduced for each recursive call, creating the self-similarity.
    # The offset positions determine the structure of the fractal.
    # Here, we're creating a simple branching structure.
    new_size = size // 2
    offset_factor = 0.8 # Controls how far apart the branches are

    # Branch 1 (Up-Left)
    draw_fractal_recursive(image, int(x - size * offset_factor / 2), int(y - size * offset_factor / 2), new_size, depth - 1)

    # Branch 2 (Up-Right)
    draw_fractal_recursive(image, int(x + size * offset_factor / 2), int(y - size * offset_factor / 2), new_size, depth - 1)

    # Branch 3 (Down-Left)
    draw_fractal_recursive(image, int(x - size * offset_factor / 2), int(y + size * offset_factor / 2), new_size, depth - 1)

    # Branch 4 (Down-Right)
    draw_fractal_recursive(image, int(x + size * offset_factor / 2), int(y + size * offset_factor / 2), new_size, depth - 1)

# --- Example Usage ---

if __name__ == "__main__":
    # Define image dimensions.
    width, height = 800, 800

    # Create a new blank image with a white background.
    # 'RGB' mode for color images.
    img = Image.new('RGB', (width, height), color='white')

    # Define starting parameters for the fractal.
    # x, y: The center coordinates for the initial drawing.
    # size: The initial size of the fractal element.
    # depth: The maximum recursion depth, controlling complexity.
    start_x, start_y = width // 2, height // 2
    initial_size = 400
    recursion_depth = 7 # Adjust this number to change complexity!

    # Start the recursive drawing process.
    print(f"Generating fractal with depth {recursion_depth}...")
    draw_fractal_recursive(img, start_x, start_y, initial_size, recursion_depth)
    print("Fractal generation complete.")

    # Save the generated fractal image.
    output_filename = "mesmerizing_fractal.png"
    img.save(output_filename)
    print(f"Fractal image saved as '{output_filename}'")
    # You can now open 'mesmerizing_fractal.png' to see your artwork!