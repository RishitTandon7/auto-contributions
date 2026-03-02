# Heap Operations in Python

class Heap:
    def __init__(self):
        self.heap = []

    # Insert a new element into the heap
    def insert(self, element):
        # Add the new element to the end of the heap
        self.heap.append(element)
        # Call the heapify_up function to maintain the heap property
        self.heapify_up(len(self.heap) - 1)

    # Remove and return the smallest element from the heap
    def extract_min(self):
        # Check if the heap is empty
        if len(self.heap) == 0:
            return None
        # If the heap has only one element, return it and clear the heap
        if len(self.heap) == 1:
            return self.heap.pop()
        # Store the smallest element in a variable
        min_element = self.heap[0]
        # Replace the smallest element with the last element in the heap
        self.heap[0] = self.heap.pop()
        # Call the heapify_down function to maintain the heap property
        self.heapify_down(0)
        return min_element

    # Heapify up: move an element up the heap until it is in its correct position
    def heapify_up(self, index):
        # While the element is not at the root of the heap
        while index > 0:
            # Calculate the parent index
            parent_index = (index - 1) // 2
            # If the parent element is smaller than the current element, break
            if self.heap[parent_index] <= self.heap[index]:
                break
            # Swap the parent and current elements
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            # Move to the parent index
            index = parent_index

    # Heapify down: move an element down the heap until it is in its correct position
    def heapify_down(self, index):
        # While the left child exists and is smaller than the current element
        while (index * 2 + 1) < len(self.heap) and self.heap[(index * 2) + 1] < self.heap[index]:
            # Calculate the left child index
            left_child_index = (index * 2) + 1
            # If the right child exists and is smaller than the left child, update the left child index
            if (index * 2 + 2) < len(self.heap) and self.heap[(index * 2) + 2] < self.heap[left_child_index]:
                left_child_index = (index * 2) + 2
            # Swap the left child and current elements
            self.heap[left_child_index], self.heap[index] = self.heap[index], self.heap[left_child_index]
            # Move to the left child index
            index = left_child_index


# Example usage
if __name__ == "__main__":
    # Create a new heap
    heap = Heap()
    # Insert elements into the heap
    heap.insert(10)
    heap.insert(20)
    heap.insert(5)
    heap.insert(15)
    heap.insert(1)
    heap.insert(4)
    # Remove and print the smallest elements from the heap
    while True:
        min_element = heap.extract_min()
        if min_element is None:
            break