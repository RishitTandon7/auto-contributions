# Binary Search Algorithm in Python

def binary_search(arr, target):
    """
    This function performs a binary search on the given array to find the index of the target element.
    
    Parameters:
    arr (list): The sorted list of elements.
    target: The target element to be searched.

    Returns:
    int: The index of the target element if found, -1 otherwise.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2
        
        # If the target is found at the middle index, return it
        if arr[mid] == target:
            return mid
        
        # If the left half of the array is sorted
        elif arr[low] <= arr[mid]:
            # If the target is in the left half, update high to mid - 1
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            # Otherwise, update low to mid + 1
            else:
                low = mid + 1
        
        # If the right half of the array is sorted
        else:
            # If the target is in the right half, update low to mid + 1
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            # Otherwise, update high to mid - 1
            else:
                high = mid - 1

    # If the target is not found, return -1
    return -1


# Example usage:
if __name__ == "__main__":
    arr = [2, 4, 6, 8, 10]
    target = 6
    
    print("Binary search result:", binary_search(arr, target))

    # Test case for target not in the array
    target = 11
    print("Binary search result for", target, ":", binary_search(arr, target))