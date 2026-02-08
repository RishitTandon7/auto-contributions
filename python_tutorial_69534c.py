# Learning Objective:
# This tutorial teaches how to generate mesmerizing fractal art using
# recursive functions and the Python Imaging Library (PIL).
# We will focus on the Mandelbrot set, a classic example of fractal
# generation, and learn how to translate mathematical concepts into
# visual art through code.

# Import necessary libraries
from PIL import Image  # PIL (Pillow) is the Python Imaging Library, used for image manipulation.
import math  # The math module provides access to mathematical functions.

# Define image dimensions and parameters for the fractal
IMAGE_WIDTH = 800
IMAGE_HEIGHT = 800
MAX_ITERATIONS = 100  # The maximum number of iterations to check for convergence.
# The Mandelbrot set is defined in the complex plane. These define our viewing window.
# We'll zoom in on a specific region of the complex plane.
X_MIN, X_MAX = -2.0, 1.0
Y_MIN, Y_MAX = -1.5, 1.5

def mandelbrot_iterations(c, max_iter):
    """
    Calculates the number of iterations it takes for the sequence z = z^2 + c
    to escape a certain bound (usually |z| > 2).

    Args:
        c (complex): The complex number representing a point in the complex plane.
        max_iter (int): The maximum number of iterations to perform.

    Returns:
        int: The number of iterations before the sequence escapes, or max_iter if it doesn't.
             This value will be used to color the pixel.
    """
    z = 0  # Initialize z to 0 for the sequence.
    for i in range(max_iter):
        z = z*z + c  # The core of the Mandelbrot set calculation: z = z^2 + c
        if abs(z) > 2:  # Check if the magnitude of z has exceeded 2.
            return i  # If it escapes, return the number of iterations.
    return max_iter  # If it doesn't escape within max_iter, consider it part of the set.

def map_value(value, old_min, old_max, new_min, new_max):
    """
    Maps a value from one range to another linearly.
    This is crucial for converting pixel coordinates to complex plane coordinates.

    Args:
        value (float): The value to map.
        old_min (float): The minimum of the original range.
        old_max (float): The maximum of the original range.
        new_min (float): The minimum of the target range.
        new_max (float): The maximum of the target range.

    Returns:
        float: The mapped value.
    """
    # The formula for linear mapping:
    # new_value = new_min + (value - old_min) * (new_max - new_min) / (old_max - old_min)
    return new_min + (value - old_min) * (new_max - new_min) / (old_max - old_min)

def generate_mandelbrot_image(width, height, x_min, x_max, y_min, y_max, max_iter):
    """
    Generates a PIL Image object of the Mandelbrot set.

    Args:
        width (int): The width of the image in pixels.
        height (int): The height of the image in pixels.
        x_min (float): The minimum real part of the complex plane to view.
        x_max (float): The maximum real part of the complex plane to view.
        y_min (float): The minimum imaginary part of the complex plane to view.
        y_max (float): The maximum imaginary part of the complex plane to view.
        max_iter (int): The maximum number of iterations for the Mandelbrot calculation.

    Returns:
        PIL.Image.Image: The generated fractal image.
    """
    # Create a new blank image with RGB color mode.
    img = Image.new('RGB', (width, height), color = 'black')
    pixels = img.load()  # Get access to the pixel data for efficient writing.

    # Iterate over each pixel in the image.
    for x in range(width):
        for y in range(height):
            # Map the pixel coordinates (x, y) to a complex number 'c'.
            # We map the x-coordinate to the real part of 'c' (ranging from x_min to x_max).
            # We map the y-coordinate to the imaginary part of 'c' (ranging from y_min to y_max).
            # Note: In image coordinates, y increases downwards, so we map it to decreasing imaginary values.
            real_part = map_value(x, 0, width, x_min, x_max)
            imaginary_part = map_value(y, 0, height, y_max, y_min) # y_max to y_min to invert
            c = complex(real_part, imaginary_part)

            # Calculate the number of iterations for this complex number.
            iterations = mandelbrot_iterations(c, max_iter)

            # Determine the color of the pixel based on the number of iterations.
            # Points that escape quickly will have different colors than points that
            # take many iterations to escape (or never escape).
            if iterations == max_iter:
                # If the point is in the Mandelbrot set, color it black.
                color = (0, 0, 0)
            else:
                # For points outside the set, color them based on how quickly they escaped.
                # We can use a simple gradient or a more complex color mapping.
                # Here's a basic gradient:
                hue = int(255 * iterations / max_iter)
                # Create a RGB tuple. We can use different color schemes.
                # A simple grayscale mapping:
                # color = (hue, hue, hue)
                # A more colorful mapping:
                # Let's use a simple hue-based coloring where hue changes with iterations.
                # This mapping is just an example, and many others can be explored.
                red = int(255 * (iterations % 16) / 16)
                green = int(255 * (iterations % 8) / 8)
                blue = int(255 * (iterations % 4) / 4)
                color = (red, green, blue)

            # Set the pixel color.
            pixels[x, y] = color

    return img

# Example Usage:
if __name__ == "__main__":
    print("Generating Mandelbrot fractal...")
    # Generate the fractal image using the defined parameters.
    mandelbrot_image = generate_mandelbrot_image(
        IMAGE_WIDTH,
        IMAGE_HEIGHT,
        X_MIN,
        X_MAX,
        Y_MIN,
        Y_MAX,
        MAX_ITERATIONS
    )

    # Save the generated image to a file.
    output_filename = "mandelbrot_fractal.png"
    mandelbrot_image.save(output_filename)
    print(f"Mandelbrot fractal saved to {output_filename}")

    # To view the image, you can open the saved file using an image viewer.
    # Alternatively, you can uncomment the following line to display it if you have a GUI environment:
    # mandelbrot_image.show()