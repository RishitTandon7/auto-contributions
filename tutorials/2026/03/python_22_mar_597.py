# Divide and Conquer Algorithm Implementation in Python

def merge_sort(arr):
    # Base case: If the array has 1 or fewer elements, it is already sorted.
    if len(arr) <= 1:
        return arr
    
    # Find the middle index of the array.
    mid = len(arr) // 2
    
    # Divide the array into two halves.
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively call merge_sort on each half.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves back together.
    return merge(left_half, right_half)

def merge(left, right):
    # Initialize an empty list to store the merged result.
    merged = []
    
    # While both lists have elements, compare and add the smallest one to the merged list.
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    
    # Add any remaining elements from either list.
    merged += left
    merged += right
    
    return merged

# Test the merge_sort function with a sample array.
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = merge_sort(arr)
    print("Sorted Array:", sorted_arr)