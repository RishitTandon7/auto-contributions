# Recursive Backtracking

def solve_sudoku(board):
    """
    Solve the Sudoku puzzle using recursive backtracking.
    
    Args:
        board (list): A 2D list representing the Sudoku board.
        
    Returns:
        bool: True if a solution is found, False otherwise.
    """
    def is_valid(num, row, col):
        # Check the row and column for the number
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        
        # Check the 3x3 sub-grid for the number
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        
        # If no conflicts found, the number is valid
        return True
    
    def backtrack():
        # Iterate over each cell in the board
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:  # Empty cell
                    for num in range(1, 10):  # Try numbers from 1 to 9
                        if is_valid(num, i, j):  # Check if the number is valid
                            board[i][j] = num  # Assign the number to the cell
                            
                            # Recursively call backtrack() on the updated board
                            if solve_sudoku(board):
                                return True  # If a solution is found, return True
                            else:
                                # If no solution is found, reset the cell and try the next number
                                board[i][j] = 0
        
        # If all cells have been tried and no solution is found, return False
        return False
    
    return backtrack()


# Example usage:

board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

if solve_sudoku(board):
    for row in board:
        print(row)
else:
    print("No solution found")