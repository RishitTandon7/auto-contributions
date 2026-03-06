# Divide and Conquer in Python

def merge_sort(arr):
    # Base case: If the array has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle of the array
    mid = len(arr) // 2

    # Divide the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves back together
    return merge(left_half, right_half)


def merge(left, right):
    # Initialize an empty list to store the merged array
    merged = []
    left_index = 0
    right_index = 0

    # Compare elements from both lists and add the smaller one to the merged list
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add any remaining elements from either list
    merged += left[left_index:]
    merged += right[right_index:]

    return merged


# Test the code
if __name__ == "__main__":
    # Create an unsorted array
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)

    # Sort the array using merge sort
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)