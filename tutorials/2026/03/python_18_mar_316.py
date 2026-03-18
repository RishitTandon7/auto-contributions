# Two Pointers Exercise
## Step 1: Introduction to Two Pointers
Two pointers are a common technique used in algorithms and data structures. They allow us to traverse through elements of an array or list while performing operations based on their values.

## Step 2: Basic Example - Removing Duplicates from Array
We will start with a basic example where we have an array containing duplicate elements, and our task is to remove these duplicates.
```python
def remove_duplicates(arr):
    # Initialize two pointers
    i = 0
    j = 1

    # Traverse through the array
    while j < len(arr):
        # Check if current element is different from previous one
        if arr[j] != arr[i]:
            # If it's different, move next element to the right of 'i'
            i += 1
            # Move 'j' forward
            arr[i] = arr[j]
        # Move 'j' forward
        j += 1

    return arr[:i+1]

# Test the function
arr = [1, 2, 3, 2, 4, 5, 6, 7, 8, 9, 2]
print(remove_duplicates(arr))
```

## Step 3: Array Rotation Example - Rotate Matrix by 90 Degrees
Next, we'll create a function that rotates an array (representing a matrix) by 90 degrees clockwise. We will use two pointers to achieve this.
```python
def rotate_matrix(matrix):
    # Get the dimensions of the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Traverse through each element in the matrix
    for i in range(rows):
        for j in range(i+1, cols):
            # Swap elements at position (i,j) and (j,i)
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    return matrix

# Test the function
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate_matrix(matrix))
```

## Step 4: Linked List Implementation - Two Sum Problem
We will implement a linked list to solve the classic "Two Sum" problem. Given an array of integers and a target sum, find two numbers that add up to this sum.