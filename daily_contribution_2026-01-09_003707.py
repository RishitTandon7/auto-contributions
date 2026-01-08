# Python
# This code simulates a simple Conway's Game of Life grid and
# applies a few evolution steps to a specific initial pattern.

import random

def create_grid(rows, cols, initial_density=0.2):
    """Creates a grid with random initial state."""
    return [[1 if random.random() < initial_density else 0 for _ in range(cols)] for _ in range(rows)]

def count_neighbors(grid, r, c):
    """Counts live neighbors for a given cell."""
    rows, cols = len(grid), len(grid[0])
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            neighbor_r, neighbor_c = r + i, c + j
            if 0 <= neighbor_r < rows and 0 <= neighbor_c < cols:
                count += grid[neighbor_r][neighbor_c]
    return count

def next_generation(grid):
    """Applies Conway's Game of Life rules to evolve the grid."""
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            live_neighbors = count_neighbors(grid, r, c)
            if grid[r][c] == 1:  # If the cell is alive
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[r][c] = 0  # Dies
                else:
                    new_grid[r][c] = 1  # Survives
            else:  # If the cell is dead
                if live_neighbors == 3:
                    new_grid[r][c] = 1  # Becomes alive
    return new_grid

def print_grid(grid):
    """Prints the grid to the console."""
    for row in grid:
        print(" ".join(["#" if cell else "." for cell in row]))
    print("-" * (len(grid[0]) * 2 - 1))

if __name__ == "__main__":
    grid_rows = 10
    grid_cols = 20
    num_generations = 5

    # Initialize with a specific pattern (e.g., a glider)
    initial_pattern = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    # Embed the pattern in a larger grid
    game_grid = [[0 for _ in range(grid_cols)] for _ in range(grid_rows)]
    pattern_rows = len(initial_pattern)
    pattern_cols = len(initial_pattern[0])

    start_row = (grid_rows - pattern_rows) // 2
    start_col = (grid_cols - pattern_cols) // 2

    for r in range(pattern_rows):
        for c in range(pattern_cols):
            game_grid[start_row + r][start_col + c] = initial_pattern[r][c]

    print("Initial State:")
    print_grid(game_grid)

    for gen in range(num_generations):
        game_grid = next_generation(game_grid)
        print(f"Generation {gen + 1}:")
        print_grid(game_grid)