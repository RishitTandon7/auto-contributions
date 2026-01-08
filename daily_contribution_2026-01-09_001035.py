# Python code to simulate a simple cellular automaton (Game of Life variant)

import random

def initialize_grid(rows, cols):
    """Creates a grid of specified dimensions, randomly populated with 0s and 1s."""
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

def count_neighbors(grid, row, col):
    """Counts the number of live neighbors (1s) for a given cell."""
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i, j) != (0, 0):  # Exclude the cell itself
                neighbor_row = (row + i + rows) % rows  # Wrap around edges
                neighbor_col = (col + j + cols) % cols  # Wrap around edges
                count += grid[neighbor_row][neighbor_col]
    return count

def update_grid(grid):
    """Applies the Game of Life rules to update the grid for the next generation."""
    rows = len(grid)
    cols = len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            live_neighbors = count_neighbors(grid, r, c)
            cell_state = grid[r][c]

            if cell_state == 1:  # Live cell
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[r][c] = 0  # Dies due to underpopulation or overpopulation
                else:
                    new_grid[r][c] = 1  # Survives
            else:  # Dead cell
                if live_neighbors == 3:
                    new_grid[r][c] = 1  # Becomes alive due to reproduction

    return new_grid

def print_grid(grid):
    """Prints the grid to the console, representing 0s as '.' and 1s as '#'."""
    for row in grid:
        print("".join(['#' if cell else '.' for cell in row]))
    print("-" * len(grid[0]))

if __name__ == "__main__":
    GRID_ROWS = 10
    GRID_COLS = 20
    NUM_GENERATIONS = 15

    current_grid = initialize_grid(GRID_ROWS, GRID_COLS)

    for generation in range(NUM_GENERATIONS):
        print(f"Generation {generation + 1}:")
        print_grid(current_grid)
        current_grid = update_grid(current_grid)