# Divide and Conquer in Python
#=====================================

def merge_sort(arr):
    # Base case: If the array has one or zero elements, it's already sorted.
    if len(arr) <= 1:
        return arr
    
    # Find the middle of the array to split it into two halves.
    mid = len(arr) // 2
    
    # Recursively sort the left and right halves.
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Merge the sorted halves back together in a single sorted array.
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    # Compare elements from both arrays and add the smaller one to the merged list.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # If there are remaining elements in either array, add them to the merged list.
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)