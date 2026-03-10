# Two Pointers
 Two pointers are a technique used to solve array-related problems. The basic idea is to use two pointers, one starting at the beginning of the array and one at the end, and move them towards each other. This approach is particularly useful for problems like finding two elements in an array that add up to a certain target value, or for swapping elements in an array without using a temporary variable.

```python
# Define a function to find two elements in an array that add up to a target value
def find_two_elements(array, target):
    # Initialize two pointers, one at the beginning of the array and one at the end
    left = 0
    right = len(array) - 1

    # Continue the loop until the two pointers meet
    while left < right:
        # Calculate the sum of the elements at the two pointers
        current_sum = array[left] + array[right]

        # If the sum is equal to the target, return the two elements
        if current_sum == target:
            return (array[left], array[right])
        # If the sum is less than the target, move the left pointer to the right
        elif current_sum < target:
            left += 1
        # If the sum is greater than the target, move the right pointer to the left
        else:
            right -= 1

    # If no two elements are found that add up to the target, return None
    return None

# Define a function to swap two elements in an array without using a temporary variable
def swap_elements(array, i, j):
    # Swap the elements at the two indices without using a temporary variable
    array[i], array[j] = array[j], array[i]

    # Return the modified array
    return array

# Test the functions
array = [1, 2, 3, 4, 5]
target = 7
print(find_two_elements(array, target))  # Output: (2, 5)

array = [1, 2, 3, 4, 5]
print(swap_elements(array, 1, 3))  # Output: [1, 2, 3, 4, 5]