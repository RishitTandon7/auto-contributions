# Binary Search Algorithm in Python
=====================================================

### Overview

Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.

### Code

```python
def binary_search(arr, target):
    """
    Searches for the index of the target element in the given array.
    
    Args:
        arr (list): A sorted list of elements.
        target: The element to be searched.
        
    Returns:
        int: The index of the target element if found; -1 otherwise.
    """

    # Initialize two pointers, one at the start and one at the end of the array
    left = 0
    right = len(arr) - 1

    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2
        
        # If the target element is found at the middle index, return it
        if arr[mid] == target:
            return mid
        
        # If the target element is less than the middle element, move to the left half
        elif arr[mid] > target:
            right = mid - 1
        
        # If the target element is greater than the middle element, move to the right half
        else:
            left = mid + 1
    
    # If the target element is not found, return -1
    return -1

# Example usage
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

index = binary_search(arr, target)

if index != -1:
    print(f"Target element {target} found at index {index}")
else:
    print(f"Target element {target} not found in the array")