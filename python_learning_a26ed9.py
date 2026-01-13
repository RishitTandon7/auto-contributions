# Learning Objective:
# This tutorial will teach you how to generate intricate fractal art using
# the power of recursion and basic image manipulation in Python.
# We'll focus on the Mandelbrot set as a prime example of a fractal.
# You'll learn how to:
# 1. Understand the concept of recursion for fractal generation.
# 2. Implement the Mandelbrot set calculation.
# 3. Create an image from numerical data.
# 4. Map iteration counts to colors for visual representation.

# We'll use the Pillow library for image manipulation.
# If you don't have it installed, run: pip install Pillow
from PIL import Image

# --- Fractal Generation Parameters ---
# Define the area of the complex plane we want to visualize.
# The Mandelbrot set is typically viewed in the range:
# real part: -2.0 to 1.0
# imaginary part: -1.5 to 1.5
REAL_START = -2.0
REAL_END = 1.0
IMAG_START = -1.5
IMAG_END = 1.5

# Define the resolution of our output image. Higher values mean more detail
# but also longer computation times.
IMAGE_WIDTH = 800
IMAGE_HEIGHT = 600

# Maximum number of iterations to check for each point.
# This determines the detail and complexity of the fractal.
MAX_ITERATIONS = 100

# --- The Core Recursive Function (Implicitly) ---
# For the Mandelbrot set, the 'recursion' is in the iterative process
# of checking if a point 'escapes' a certain boundary.
# The function `mandelbrot` below simulates this.
# Each call to itself within the loop is like a step deeper into the fractal.

def mandelbrot(c_real, c_imag, max_iter):
    """
    Calculates the number of iterations for a point (c_real, c_imag)
    to escape the Mandelbrot set.

    The Mandelbrot set is defined by the equation: z = z^2 + c
    where z starts at 0. If |z| stays bounded (doesn't grow infinitely)
    after many iterations, the point c is in the set.

    Args:
        c_real (float): The real part of the complex number 'c'.
        c_imag (float): The imaginary part of the complex number 'c'.
        max_iter (int): The maximum number of iterations to perform.

    Returns:
        int: The number of iterations it took for |z| to exceed 2.0,
             or max_iter if it didn't escape within the limit.
    """
    z_real = 0.0
    z_imag = 0.0
    # We'll track the number of iterations.
    iterations = 0

    # The core of the Mandelbrot calculation:
    # Iterate the equation z = z^2 + c.
    # This loop implicitly represents the recursive nature of fractal generation,
    # where each step depends on the previous one.
    while (z_real * z_real + z_imag * z_imag) < 4.0 and iterations < max_iter:
        # Calculate z^2:
        # (a + bi)^2 = a^2 + 2abi + (bi)^2 = a^2 + 2abi - b^2
        # So, new_z_real = z_real^2 - z_imag^2
        # And new_z_imag = 2 * z_real * z_imag
        temp_z_real = z_real * z_real - z_imag * z_imag + c_real
        z_imag = 2.0 * z_real * z_imag + c_imag
        z_real = temp_z_real

        # Increment the iteration count for this point.
        iterations += 1

    # If iterations reaches max_iter, the point is considered to be in the set.
    # Otherwise, it escaped.
    return iterations

# --- Image Generation ---

def generate_mandelbrot_image(width, height, max_iter):
    """
    Generates a Pillow Image object representing the Mandelbrot set.

    Args:
        width (int): The desired width of the image.
        height (int): The desired height of the image.
        max_iter (int): The maximum number of iterations for the Mandelbrot calculation.

    Returns:
        PIL.Image.Image: A Pillow Image object of the Mandelbrot set.
    """
    # Create a new blank image with RGB color mode.
    img = Image.new('RGB', (width, height), color='black')
    # Get access to the pixel data for faster manipulation.
    pixels = img.load()

    # Calculate the scaling factors to map image coordinates to complex plane coordinates.
    # delta_real is the size of one pixel in the real dimension.
    delta_real = (REAL_END - REAL_START) / width
    # delta_imag is the size of one pixel in the imaginary dimension.
    delta_imag = (IMAG_END - IMAG_START) / height

    # Iterate through each pixel of the image.
    for x in range(width):
        for y in range(height):
            # Convert pixel coordinates (x, y) to complex plane coordinates (c_real, c_imag).
            # We subtract y from height because image y-coordinates increase downwards,
            # while imaginary axis typically increases upwards.
            c_real = REAL_START + x * delta_real
            c_imag = IMAG_START + (height - 1 - y) * delta_imag

            # Calculate the number of iterations for this complex point.
            iterations = mandelbrot(c_real, c_imag, max_iter)

            # --- Coloring the Fractal ---
            # The color of a pixel is determined by how quickly its corresponding
            # complex number 'escaped'. Points that didn't escape (iterations == max_iter)
            # are typically colored black (part of the set).
            # Points that escaped quickly can be colored differently to show structure.
            if iterations == max_iter:
                # Point is in the Mandelbrot set. Color it black.
                color = (0, 0, 0)
            else:
                # Point escaped. We'll map the iteration count to a color.
                # A simple way is to use the iteration count to generate RGB values.
                # We can scale the iteration count to fit within the 0-255 range for each color channel.
                # This is a very basic coloring scheme; more advanced ones exist for richer visuals.
                # Using modulo to create a cyclical color pattern.
                r = (iterations * 5) % 256
                g = (iterations * 8) % 256
                b = (iterations * 10) % 256
                color = (r, g, b)

            # Set the color of the pixel in the image.
            pixels[x, y] = color

    return img

# --- Example Usage ---
if __name__ == "__main__":
    print("Generating Mandelbrot fractal image...")
    mandelbrot_image = generate_mandelbrot_image(IMAGE_WIDTH, IMAGE_HEIGHT, MAX_ITERATIONS)

    # Save the generated image to a file.
    output_filename = "mandelbrot_fractal.png"
    mandelbrot_image.save(output_filename)
    print(f"Fractal image saved as '{output_filename}'")

    # Optionally, display the image (requires a viewer installed on your system).
    # mandelbrot_image.show()