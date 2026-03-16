#!/usr/bin/python
# Heap Operations in Python

class Heap:
    def __init__(self):
        self.heap = []

    # Insert a value into the heap
    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    # Delete and return the minimum value from the heap
    def delete_min(self):
        if len(self.heap) == 0:
            return None
        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self._heapify_down(0)
        return min_value

    # Get the minimum value from the heap without deleting it
    def get_min(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    # Heapify up to maintain the heap property after insertion
    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self._heapify_up(parent_index)

    # Heapify down to maintain the heap property after deletion
    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index
        if len(self.heap) > left_child_index and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index
        if len(self.heap) > right_child_index and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

# Create a heap and insert some values
heap = Heap()
heap.insert(5)
heap.insert(3)
heap.insert(1)
heap.insert(9)
print(heap.get_min())  # Output: 1

# Delete the minimum value from the heap
print(heap.delete_min())  # Output: 1

# Get the minimum value from the heap without deleting it
print(heap.get_min())  # Output: 3