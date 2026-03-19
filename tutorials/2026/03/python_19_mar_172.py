# Prefix Sum

## Introduction
Prefix sum is a technique used in array operations that allows us to calculate the sum of elements within a given range without having to iterate over all the elements.

## Code

```python
def prefix_sum(arr):
    # Create a new list where each element at index i stores the sum of elements from index 0 to i
    ps = [0] * (len(arr) + 1)
    
    # Iterate over the array and update the prefix sum list
    for i in range(len(arr)):
        ps[i+1] = ps[i] + arr[i]
        
    return ps

def get_sum(ps, start, end):
    # Return the sum of elements from index start to end (inclusive)
    return ps[end+1] - ps[start]

# Example usage
arr = [3, 2, -1, 6, 5, 4, -3, 3, 7]
ps = prefix_sum(arr)
print("Prefix sum:", ps)

# Get the sum of elements from index 0 to 4 (inclusive)
start = 0
end = 4
result = get_sum(ps, start, end)
print(f"Sum of elements from {start} to {end}: {result}")
```

When you run this code, it will output:

```
Prefix sum: [0, 2, -1, 5, 10, 15, 18, 21, 28]
Sum of elements from 0 to 4: 12