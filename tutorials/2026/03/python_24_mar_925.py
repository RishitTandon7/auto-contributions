# Binary Search Algorithm in Python
#=====================================

def binary_search(arr, target):
    # Initialize the low and high pointers
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Calculate the mid index
        mid = (low + high) // 2
        
        # If the target is found at the mid index, return it
        if arr[mid] == target:
            return mid
        # If the target is less than the value at the mid index,
        # move the high pointer to the left
        elif arr[mid] > target:
            high = mid - 1
        # If the target is greater than the value at the mid index,
        # move the low pointer to the right
        else:
            low = mid + 1

    # If the target is not found, return -1
    return -1


# Example usage
if __name__ == "__main__":
    # Create a sorted array
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    
    # Find the index of a target value in the array
    target = 23
    
    # Call the binary_search function and print the result
    result = binary_search(arr, target)
    if result != -1:
        print("Target found at index", result)
    else:
        print("Target not found")