# Sliding Window
# ===========

def max_sum_subarray(arr, k):
    """
    This function finds the maximum sum of a subarray of size k in the given array.
    
    Parameters:
    arr (list): The input array
    k (int): The size of the subarray
    
    Returns:
    int: The maximum sum of a subarray of size k
    """
    # Initialize the window boundaries
    left = 0
    right = 0
    
    # Initialize the current sum and the maximum sum
    curr_sum = 0
    max_sum = float('-inf')
    
    # Move the window to the right
    while right < len(arr):
        # Add the element at the right boundary to the current sum
        curr_sum += arr[right]
        
        # If the window size is greater than k, remove the leftmost element from the current sum
        if right - left + 1 > k:
            curr_sum -= arr[left]
            left += 1
        
        # Update the maximum sum
        if right - left + 1 == k:
            max_sum = max(max_sum, curr_sum)
        
        # Move the window to the right
        right += 1
    
    return max_sum

# Example usage
arr = [1, 2, 3, 4, 5]
k = 3
print("Maximum sum of subarray of size", k, ":", max_sum_subarray(arr, k))