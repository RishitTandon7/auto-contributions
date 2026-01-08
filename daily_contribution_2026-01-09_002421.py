# Python code to simulate a simple cellular automaton (Conway's Game of Life)

import random
import time

def create_grid(rows, cols):
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

def get_neighbors(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    neighbors = 0
    for i in range(max(0, r - 1), min(rows, r + 2)):
        for j in range(max(0, c - 1), min(cols, c + 2)):
            if (i, j) != (r, c):
                neighbors += grid[i][j]
    return neighbors

def update_grid(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            live_neighbors = get_neighbors(grid, r, c)
            if grid[r][c] == 1:  # If cell is alive
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[r][c] = 0  # Dies due to underpopulation or overpopulation
                else:
                    new_grid[r][c] = 1  # Survives
            else:  # If cell is dead
                if live_neighbors == 3:
                    new_grid[r][c] = 1  # Becomes alive due to reproduction
    return new_grid

def display_grid(grid):
    for row in grid:
        print("".join(['#' if cell else ' ' for cell in row]))

if __name__ == "__main__":
    rows, cols = 20, 40
    generations = 50
    delay = 0.2

    current_grid = create_grid(rows, cols)

    for _ in range(generations):
        display_grid(current_grid)
        current_grid = update_grid(current_grid)
        time.sleep(delay)
        print("\033c", end="") # Clear screen (Unix-like systems)