# Merge Sort Algorithm in Python
=====================================

Merge sort is a divide-and-conquer algorithm that splits an array into two halves, recursively sorts them, and then merges the sorted halves.

```python
def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm.
    
    Args:
        arr (list): The input array to be sorted.
    
    Returns:
        list: The sorted array.
    """

    # Base case: If the array has 1 or fewer elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle index of the array
    mid = len(arr) // 2

    # Divide the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merges two sorted arrays into a single sorted array.
    
    Args:
        left (list): The first sorted array.
        right (list): The second sorted array.
    
    Returns:
        list: The merged sorted array.
    """

    # Initialize an empty list to store the merged result
    merged = []
    left_index = 0
    right_index = 0

    # Merge smaller elements first
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left or right arrays
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


# Example usage:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)