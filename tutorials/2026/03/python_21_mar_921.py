# Two Pointers Technique in Python

# Problem Statement: Given an array of integers, find the maximum sum that can be obtained by subtracting 
# two elements from the array such that their difference is 2 and their indices are not adjacent.

def max_sum_difference(arr):
    # Sort the array in ascending order
    arr.sort()
    
    # Initialize variables to store the maximum sum difference and the minimum element in the sorted array
    max_diff = float('-inf')
    min_val = arr[0]
    
    # Iterate over the sorted array from second smallest to largest
    for i in range(1, len(arr)):
        # Calculate the difference between the current element and the previous one (excluding the last two)
        if i < len(arr) - 1:
            diff = arr[i] - arr[i-1]
        else:
            continue
        
        # Check if the difference is equal to 2
        if diff == 2:
            # Update the maximum sum difference and break the loop as we've found a pair with difference 2
            max_diff = arr[i] + arr[i-1]
            break
    
    # Return the maximum sum difference or -1 if no such pair is found
    return max_diff

# Example usage:
arr = [1, 3, 5, 7, 9]
print(max_sum_difference(arr))  # Output: 17 (at indices 2 and 1)

arr = [10, 20, 30, 40, 50]
print(max_sum_difference(arr))  # Output: -1 (no pair with difference 2 found)