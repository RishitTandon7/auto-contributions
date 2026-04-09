# Binary Search Algorithm in Python

def binary_search(arr, target):
    """
    This function performs a binary search on the given array to find the index of the target element.
    
    Parameters:
    arr (list): The sorted list of elements.
    target: The target element to be searched in the list.
    
    Returns:
    int: The index of the target element if found, -1 otherwise.
    """
    # Initialize two pointers, low and high, to the start and end of the array
    low = 0
    high = len(arr) - 1

    # Continue the search until the two pointers meet
    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2
        
        # If the target element is found at the middle index, return the index
        if arr[mid] == target:
            return mid
        # If the target element is less than the middle element, move the high pointer to the left
        elif arr[mid] > target:
            high = mid - 1
        # If the target element is greater than the middle element, move the low pointer to the right
        else:
            low = mid + 1

    # If the target element is not found in the array, return -1
    return -1


# Example usage of binary search function
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

index = binary_search(arr, target)

if index != -1:
    print("Target element found at index:", index)
else:
    print("Target element not found in the array.")