"""
Learning Objective:
This tutorial will teach you how to generate unique, fractal-like 2D terrain maps
using Perlin noise in Python. We will focus on understanding how Perlin noise
can create natural-looking patterns and how to use it to simulate elevation.
This is a fundamental technique for procedural content generation in games and visualizations.
"""

# Import necessary libraries
# NumPy is essential for numerical operations, especially array manipulation,
# which is perfect for handling our terrain map data.
import numpy as np
# This library provides a Perlin noise implementation.
# We'll use it to generate our random, yet structured, noise values.
import noise

# Define a function to generate the terrain map
def generate_terrain(width, height, scale, octaves, persistence, lacunarity, seed=None):
    """
    Generates a 2D terrain map using Perlin noise.

    Args:
        width (int): The width of the terrain map (number of columns).
        height (int): The height of the terrain map (number of rows).
        scale (float): Controls the overall "zoom" level of the noise.
                       Higher values zoom out, lower values zoom in.
        octaves (int): The number of layers of noise to combine. More octaves
                       create more detail and complexity.
        persistence (float): Controls how much each successive octave contributes
                             to the overall shape. Values between 0 and 1 are typical.
                             Lower persistence means higher octaves have less impact.
        lacunarity (float): Controls the frequency of each successive octave.
                            Higher values mean higher octaves have finer detail.
                            Values greater than 1 are typical.
        seed (int, optional): An integer to seed the random number generator.
                              Using the same seed will produce the same terrain.
                              If None, a random seed is used.

    Returns:
        numpy.ndarray: A 2D NumPy array representing the terrain map,
                       where values typically range from -1 to 1.
    """

    # Initialize the terrain map as a 2D array of zeros.
    # This array will store our elevation values.
    terrain_map = np.zeros((height, width))

    # Iterate over each pixel (or grid point) in our terrain map.
    for i in range(height):
        for j in range(width):
            # Calculate the coordinates for the Perlin noise function.
            # We divide by 'scale' to control the frequency/zoom.
            # This makes sure that as we move across our terrain map (j, i),
            # we sample different points in the Perlin noise space.
            x_coord = j / scale
            y_coord = i / scale

            # Generate the Perlin noise value for the current coordinates.
            # The 'octaves', 'persistence', and 'lacunarity' parameters
            # are crucial for creating fractal-like detail.
            # 'octaves': adds layers of noise to increase complexity.
            # 'persistence': determines how much influence each octave has.
            # 'lacunarity': determines how much the frequency increases for each octave.
            # 'seed': ensures reproducibility if provided.
            terrain_map[i][j] = noise.pnoise2(x_coord,
                                             y_coord,
                                             octaves=octaves,
                                             persistence=persistence,
                                             lacunarity=lacunarity,
                                             base=seed) # 'base' is the seed in the 'noise' library

    # The generated noise values typically range from -1 to 1.
    # For visualization or game use, you might want to normalize or remap these values.
    # For this educational example, we'll return the raw Perlin noise values.
    return terrain_map

# --- Example Usage ---

if __name__ == "__main__":
    # Define parameters for terrain generation
    terrain_width = 256
    terrain_height = 256
    noise_scale = 50.0  # Larger scale means more zoomed out, more gradual hills
    num_octaves = 6
    octave_persistence = 0.5 # How much each subsequent octave adds detail
    octave_lacunarity = 2.0 # How much finer the details get with each octave

    # Generate the terrain map
    # We'll use a seed for reproducibility, so you can get the same terrain every time.
    # Try changing the seed to see different terrain patterns!
    my_terrain = generate_terrain(terrain_width,
                                  terrain_height,
                                  noise_scale,
                                  num_octaves,
                                  octave_persistence,
                                  octave_lacunarity,
                                  seed=42)

    print("Terrain map generated successfully!")
    print(f"Shape of the terrain map: {my_terrain.shape}")
    print(f"Min value in terrain map: {np.min(my_terrain)}")
    print(f"Max value in terrain map: {np.max(my_terrain)}")

    # In a real application, you would now visualize or use 'my_terrain'.
    # For example, you could use matplotlib to display it as an image:
    # import matplotlib.pyplot as plt
    # plt.imshow(my_terrain, cmap='terrain', origin='lower')
    # plt.title("Generated Perlin Noise Terrain")
    # plt.colorbar(label="Elevation")
    # plt.show()