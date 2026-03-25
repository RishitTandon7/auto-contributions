# Divide and Conquer in Python
=====================================

## Introduction

Divide and Conquer is an algorithmic paradigm that breaks down a problem into smaller sub-problems, solves them recursively, and combines their solutions to solve the original problem.

## Binary Search Algorithm

This code implements the Binary Search algorithm, which is a classic example of Divide and Conquer. It searches for an element in a sorted array by repeatedly dividing the search interval in half.

```python
def binary_search(arr, target):
    # Initialize the low and high indices
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Calculate the mid index
        mid = (low + high) // 2

        # Compare the middle element with the target
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            # If the middle element is less than the target, move to the right half
            low = mid + 1
        else:
            # If the middle element is greater than the target, move to the left half
            high = mid - 1

    # If the target is not found, return -1
    return -1


# Example usage
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

result = binary_search(arr, target)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")