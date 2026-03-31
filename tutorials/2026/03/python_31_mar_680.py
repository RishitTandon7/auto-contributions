# Segment Tree Implementation in Python
=====================================

A segment tree is a tree data structure for storing information about intervals of an array. It is particularly useful for range queries and updates.

## Code

```python
class SegmentTree:
    def __init__(self, arr):
        self.N = len(arr)
        self.tree = [0] * (4 * self.N)
        self.build_tree(arr, 0, 0, self.N - 1)

    # Build the segment tree recursively
    def build_tree(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build_tree(arr, 2 * node + 1, start, mid)
            self.build_tree(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    # Range query: get the sum of values in the range [start, end]
    def query(self, start, end):
        return self.query_range(0, 0, self.N - 1, start, end)

    def query_range(self, node, start, end, query_start, query_end):
        if query_start > end or query_end < start:
            return 0
        elif query_start <= start and query_end >= end:
            return self.tree[node]
        else:
            mid = (start + end) // 2
            left_sum = self.query_range(2 * node + 1, start, mid, query_start, query_end)
            right_sum = self.query_range(2 * node + 2, mid + 1, end, query_start, query_end)
            return left_sum + right_sum

    # Update the value at index 'idx' to 'new_val'
    def update(self, idx, new_val):
        self.update_range(0, 0, self.N - 1, idx, new_val)

    def update_range(self, node, start, end, idx, new_val):
        if start == end:
            self.tree[node] = new_val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update_range(2 * node + 1, start, mid, idx, new_val)
            else:
                self.update_range(2 * node + 2, mid + 1, end, idx, new_val)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

# Example usage
arr = [1, 3, -1, 5, 2]
segment_tree = SegmentTree(arr)

print("Sum of values in range [0, 4]:", segment_tree.query(0, 4))
print("Update value at index 2 to 10:")
segment_tree.update(2, 10)
print("Sum of values in range [0, 4] after update:", segment_tree.query(0, 4))