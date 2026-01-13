# MANDELBROT SET EXPLORATION WITH PYTHON

# Learning Objective: This tutorial will teach you how to visualize and interact
# with the Mandelbrot set using Python's plotting capabilities. We will focus on
# understanding the core concept of fractal generation through iterative functions
# and how to map these results to a visual representation.

# The Mandelbrot set is a fascinating mathematical object that exhibits
# self-similarity at all scales. It's defined by a simple iterative process.
# For each point 'c' in the complex plane, we iterate the function z = z^2 + c,
# starting with z = 0. If the magnitude of 'z' remains bounded (doesn't
# grow infinitely large) after a certain number of iterations, the point 'c'
# belongs to the Mandelbrot set.

import numpy as np
import matplotlib.pyplot as plt

# --- Configuration ---
# These parameters control the resolution and area of the Mandelbrot set we'll generate.
WIDTH = 800  # The number of pixels horizontally.
HEIGHT = 800 # The number of pixels vertically.
MAX_ITERATIONS = 100 # How many times we'll iterate the function for each point.
                     # Higher values reveal more detail but take longer to compute.

# These define the region of the complex plane we are interested in.
# The Mandelbrot set is known to exist roughly between -2 and 1 on the real axis,
# and -1.5i and 1.5i on the imaginary axis.
X_MIN = -2.0
X_MAX = 1.0
Y_MIN = -1.5
Y_MAX = 1.5

def is_in_mandelbrot(c_real, c_imag, max_iter):
    """
    Determines if a complex number 'c' belongs to the Mandelbrot set.

    Args:
        c_real (float): The real part of the complex number 'c'.
        c_imag (float): The imaginary part of the complex number 'c'.
        max_iter (int): The maximum number of iterations to perform.

    Returns:
        int: The number of iterations it took for 'z' to escape, or max_iter
             if it didn't escape within the limit. A lower return value
             indicates the point is further from the set.
    """
    z_real = 0.0  # Initialize the real part of 'z'.
    z_imag = 0.0  # Initialize the imaginary part of 'z'.

    # We iterate the function z = z^2 + c.
    # In complex numbers, z^2 = (z_real + i*z_imag)^2
    #                     = z_real^2 + 2*i*z_real*z_imag + (i*z_imag)^2
    #                     = z_real^2 + 2*i*z_real*z_imag - z_imag^2
    # So, the new real part is z_real^2 - z_imag^2.
    # And the new imaginary part is 2*z_real*z_imag.
    # Then we add the real and imaginary parts of 'c' respectively.

    for i in range(max_iter):
        # Calculate z_real^2 - z_imag^2. This is the real part of z^2.
        z_real_squared = z_real * z_real
        z_imag_squared = z_imag * z_imag
        new_z_real = z_real_squared - z_imag_squared + c_real

        # Calculate 2*z_real*z_imag. This is the imaginary part of z^2.
        new_z_imag = 2 * z_real * z_imag + c_imag

        # Update z.
        z_real = new_z_real
        z_imag = new_z_imag

        # Check if the magnitude of 'z' has exceeded 2.
        # The magnitude squared is z_real^2 + z_imag^2.
        # If magnitude squared > 4, then magnitude > 2.
        # We check the magnitude squared for efficiency as it avoids a square root.
        if z_real_squared + z_imag_squared > 4.0:
            # The point escaped, meaning it's NOT in the Mandelbrot set.
            # We return the number of iterations it took to escape.
            # This value will be used for coloring.
            return i
    # If the loop completes without escaping, the point is considered to be in the set.
    # We return max_iter to signify it's part of the set.
    return max_iter

def generate_mandelbrot_image():
    """
    Generates a 2D NumPy array representing the Mandelbrot set.

    The array will contain the iteration count for each pixel.
    """
    # Create an empty array to store the iteration counts for each pixel.
    mandelbrot_data = np.zeros((HEIGHT, WIDTH), dtype=np.int32)

    # Iterate over each pixel in the image.
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # Map the pixel coordinates (x, y) to complex plane coordinates (c_real, c_imag).
            # This is a linear transformation.
            # We want x=0 to map to X_MIN, and x=WIDTH-1 to map to X_MAX.
            # Similarly for y and Y_MIN/Y_MAX.
            c_real = X_MIN + (X_MAX - X_MIN) * x / (WIDTH - 1)
            c_imag = Y_MIN + (Y_MAX - Y_MIN) * y / (HEIGHT - 1)

            # Calculate whether this complex number belongs to the Mandelbrot set
            # and get the iteration count.
            mandelbrot_data[y, x] = is_in_mandelbrot(c_real, c_imag, MAX_ITERATIONS)
    return mandelbrot_data

# --- Example Usage ---
if __name__ == "__main__":
    print("Generating Mandelbrot set image...")
    # Generate the data for the Mandelbrot set.
    mandelbrot_pixels = generate_mandelbrot_image()

    print("Displaying Mandelbrot set image...")
    # Create a plot using Matplotlib.
    plt.figure(figsize=(10, 10)) # Set the figure size for better viewing.

    # Display the image.
    # 'extent' sets the limits of the x and y axes to match our complex plane coordinates.
    # 'origin='lower'' ensures that (0,0) corresponds to the bottom-left corner of the plot.
    # 'cmap='hot'' is a colormap. 'hot' often looks good for fractals,
    # but you can experiment with others like 'viridis', 'plasma', 'inferno', 'magma', 'gray', etc.
    plt.imshow(mandelbrot_pixels, extent=[X_MIN, X_MAX, Y_MIN, Y_MAX], cmap='hot', origin='lower')

    # Add a color bar to show what the different colors represent (iteration counts).
    plt.colorbar(label='Iterations to Escape')

    # Set the title of the plot.
    plt.title('Mandelbrot Set')

    # Label the axes.
    plt.xlabel('Real Part (Re)')
    plt.ylabel('Imaginary Part (Im)')

    # Ensure the aspect ratio is equal, so the fractal isn't distorted.
    plt.gca().set_aspect('equal', adjustable='box')

    # Show the plot.
    plt.show()

    print("Done!")
# --- End of Tutorial ---