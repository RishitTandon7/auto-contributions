# Mandelbrot Set Visualization Tutorial

# Learning Objective:
# This tutorial will teach you how to visualize the Mandelbrot set
# using Python. We will leverage complex number arithmetic to
# understand the mathematical concept behind the set and use the
# matplotlib library to create a visual representation.
# By the end of this tutorial, you will be able to:
# 1. Understand the core iteration formula for the Mandelbrot set.
# 2. Implement this formula using Python's complex number support.
# 3. Map iteration counts to colors for visualization.
# 4. Generate and display the Mandelbrot set using matplotlib.

# 1. Import necessary libraries
import numpy as np  # For efficient array operations and complex number handling
import matplotlib.pyplot as plt  # For plotting and visualization

# 2. Define parameters for the Mandelbrot set calculation
WIDTH = 800  # Number of pixels horizontally
HEIGHT = 800  # Number of pixels vertically
MAX_ITER = 100  # Maximum number of iterations to check for divergence

# These define the region of the complex plane we want to visualize.
# The Mandelbrot set is located roughly between -2 and 1 on the real axis,
# and -1.5 and 1.5 on the imaginary axis.
REAL_START = -2.0
REAL_END = 1.0
IMAG_START = -1.5
IMAG_END = 1.5

# 3. The core Mandelbrot set calculation logic
def mandelbrot(c, max_iter):
    """
    Calculates the number of iterations for a given complex number 'c'
    to escape the Mandelbrot set.

    The Mandelbrot set is defined by the recurrence relation:
    z_{n+1} = z_n^2 + c
    starting with z_0 = 0.

    A complex number 'c' is in the Mandelbrot set if the sequence
    {z_n} remains bounded (i.e., does not tend to infinity).
    We check for divergence by seeing if the magnitude of z exceeds 2.
    If it exceeds 2, we consider it to have escaped and return the
    number of iterations it took. If it stays bounded after MAX_ITER,
    we assume it's in the set.

    Args:
        c (complex): The complex number to test.
        max_iter (int): The maximum number of iterations to perform.

    Returns:
        int: The number of iterations until divergence, or MAX_ITER if it
             does not diverge within the limit.
    """
    z = 0  # Initialize z_0 to 0
    for i in range(max_iter):
        z = z*z + c  # This is the core Mandelbrot iteration
        # We check the magnitude squared to avoid using sqrt, which is slower.
        # If |z|^2 > 4, then |z| > 2, meaning the point has escaped.
        if (z.real * z.real + z.imag * z.imag) > 4:
            return i  # Return the iteration count when it escapes
    return max_iter  # If it doesn't escape within max_iter, it's likely in the set

# 4. Create a grid of complex numbers to test
def create_mandelbrot_image(width, height, real_start, real_end, imag_start, imag_end, max_iter):
    """
    Generates a 2D array representing the Mandelbrot set for a given region.

    This function maps each pixel in the output image to a corresponding
    complex number in the complex plane. It then applies the mandelbrot
    function to each complex number to get an iteration count.

    Args:
        width (int): The width of the output image in pixels.
        height (int): The height of the output image in pixels.
        real_start (float): The starting value for the real axis.
        real_end (float): The ending value for the real axis.
        imag_start (float): The starting value for the imaginary axis.
        imag_end (float): The ending value for the imaginary axis.
        max_iter (int): The maximum number of iterations for the mandelbrot function.

    Returns:
        np.ndarray: A 2D numpy array where each element is the iteration
                    count for the corresponding complex number.
    """
    # Create arrays for the real and imaginary parts of the complex plane.
    # np.linspace creates evenly spaced numbers over a specified interval.
    # This effectively creates a grid of points in the complex plane.
    real_vals = np.linspace(real_start, real_end, width)
    imag_vals = np.linspace(imag_start, imag_end, height)

    # Initialize an empty 2D array to store the iteration counts.
    # This array will have dimensions (height, width).
    mandelbrot_image = np.zeros((height, width), dtype=int)

    # Iterate over each pixel (row, column) in the image.
    for row in range(height):
        for col in range(width):
            # For each pixel, we construct a complex number.
            # The real part comes from real_vals[col] (horizontal axis).
            # The imaginary part comes from imag_vals[row] (vertical axis).
            # We use 'j' for the imaginary unit in Python.
            c = complex(real_vals[col], imag_vals[row])

            # Calculate the number of iterations for this complex number 'c'.
            iterations = mandelbrot(c, max_iter)

            # Store the iteration count in our Mandelbrot image array.
            mandelbrot_image[row, col] = iterations

    return mandelbrot_image

# 5. Generate and display the Mandelbrot set
if __name__ == "__main__":
    # This block ensures the code runs only when the script is executed directly.

    print("Generating Mandelbrot set...")
    # Call the function to create the image data.
    mandelbrot_data = create_mandelbrot_image(
        WIDTH, HEIGHT, REAL_START, REAL_END, IMAG_START, IMAG_END, MAX_ITER
    )
    print("Generation complete. Displaying image...")

    # Use matplotlib to display the generated Mandelbrot set image.
    plt.figure(figsize=(10, 10))  # Create a figure and set its size.
    # imshow displays an image.
    # cmap='hot' uses a colormap where higher values are brighter/hotter.
    # You can experiment with other colormaps like 'viridis', 'plasma', 'inferno'.
    plt.imshow(mandelbrot_data, extent=[REAL_START, REAL_END, IMAG_START, IMAG_END], cmap='hot')
    plt.colorbar(label="Iterations to Escape")  # Add a color bar to show what colors represent.
    plt.title("Mandelbrot Set")  # Set the title of the plot.
    plt.xlabel("Real Axis")  # Label the x-axis.
    plt.ylabel("Imaginary Axis")  # Label the y-axis.
    plt.show()  # Display the plot.

# Example Usage:
# To run this code:
# 1. Save it as a Python file (e.g., mandelbrot_generator.py).
# 2. Make sure you have numpy and matplotlib installed:
#    pip install numpy matplotlib
# 3. Run the file from your terminal:
#    python mandelbrot_generator.py
#
# You can also experiment by changing the following parameters at the top:
# - WIDTH, HEIGHT: To change the resolution of the image.
# - MAX_ITER: To increase detail (higher values take longer to compute).
# - REAL_START, REAL_END, IMAG_START, IMAG_END: To zoom into different parts
#   of the complex plane. For example, to zoom into a specific area:
#   REAL_START = -0.74877
#   REAL_END = -0.74872
#   IMAG_START = 0.12353
#   IMAG_END = 0.12358