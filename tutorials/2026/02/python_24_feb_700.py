# Two Pointers Technique

The Two Pointers technique is a common approach used in various algorithms, particularly in problems involving arrays, linked lists, and strings. This code demonstrates how to use two pointers to solve a problem.

```python
def max_sum_subarray(nums):
    # Initialize the maximum sum and current sum to the first element of the array
    max_sum = current_sum = nums[0]
    # Initialize the left pointer to the first element
    left = 0

    # Iterate over the array starting from the second element
    for right in range(1, len(nums)):
        # While the current sum is less than or equal to the current element, subtract the leftmost element from the current sum and move the left pointer to the right
        while current_sum + nums[right] <= nums[right]:
            current_sum += nums[right]
            right += 1
        # Update the maximum sum
        max_sum = max(max_sum, current_sum)
        # Reset the current sum and move the left pointer to the right
        current_sum = nums[right]
        left = right

    return max_sum

# Test the function
nums = [3, 2, 1, 5, 6, 4]
print(max_sum_subarray(nums))  # Output: 10