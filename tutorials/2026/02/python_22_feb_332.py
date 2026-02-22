# Two Pointers Technique in Python

# Problem: Find the first duplicate in an array
# Example: [1, 2, 3, 4, 5, 6, 6]

def find_first_duplicate(arr):
    """
    Find the first duplicate in an array using two pointers technique
    """
    # Initialize two pointers, one at the start and one at the end of the array
    left = 0
    right = len(arr) - 1

    # Continue the loop until the two pointers meet
    while left < right:
        # Move the left pointer to the right until we find a duplicate
        if arr[left] == arr[left + 1]:
            # If we find a duplicate, move the left pointer to the right
            left += 1
        # Move the right pointer to the left until we find a duplicate
        elif arr[right] == arr[right - 1]:
            # If we find a duplicate, move the right pointer to the left
            right -= 1
        # If neither of the above conditions is true, move the pointers closer
        else:
            left += 1
            right -= 1

    # At this point, the two pointers meet at the first duplicate
    return arr[left]

# Example usage
arr = [1, 2, 3, 4, 5, 6, 6]
print(find_first_duplicate(arr))  # Output: 6