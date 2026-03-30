# Divide and Conquer Algorithm in Python
# This program uses the merge sort algorithm as an example of divide and conquer.

def merge_sort(arr):
    # Base case: If the array has only one element, it is already sorted.
    if len(arr) <= 1:
        return arr
    
    # Find the middle point of the array.
    mid = len(arr) // 2
    
    # Divide the array into two halves.
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively call merge_sort on both halves.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves back together.
    return merge(left_half, right_half)


def merge(left, right):
    # Create a new array to store the merged result.
    merged = []
    
    # While both arrays have elements, merge them one by one.
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    
    # If there are remaining elements in either array, append them to the merged array.
    merged.extend(left)
    merged.extend(right)
    
    return merged


# Test the merge_sort function with an example array.
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original Array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted Array:", sorted_arr)


# Test the merge_sort function with a larger example array.
arr = [64, 34, 25, 12, 22, 11, 90, 50, 75, 32]
print("\nOriginal Large Array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted Large Array:", sorted_arr)


# Test the merge_sort function with a negative example array.
arr = [-5, -3, -1, 0, 2, 4]
print("\nOriginal Negative Array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted Negative Array:", sorted_arr)