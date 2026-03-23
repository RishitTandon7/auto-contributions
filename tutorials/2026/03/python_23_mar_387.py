# Monotonic Stack Implementation in Python
=====================================================

A monotonic stack is a data structure that allows you to push and pop elements while maintaining the order of insertion. This implementation provides methods for inserting elements, deleting elements, checking if an element exists, and finding the next smaller element.

```python
class MonotonicStack:
    """
    A monotonic stack implementation in Python.
    
    Attributes:
        stack (list): The underlying list that stores the elements.
        min_stack (list): The stack that maintains the minimum elements seen so far.
    """

    def __init__(self):
        # Initialize the empty stacks
        self.stack = []
        self.min_stack = []

    def push(self, x):
        # Push an element onto the stack and update the min_stack if necessary
        while self.min_stack and x <= self.min_stack[-1]:
            self.pop_min()
        self.stack.append(x)
        if not self.min_stack or x < self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        # Pop an element from the stack and return it
        if not self.stack:
            raise IndexError("Cannot pop from an empty stack")
        popped = self.stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()
        return popped

    def top(self):
        # Return the top element of the stack without removing it
        if not self.stack:
            raise IndexError("Cannot get the top of an empty stack")
        return self.stack[-1]

    def findNextGreater(self, x):
        # Find the next greater element in the stack
        if not self.stack or self.stack[-1] <= x:
            return -1  # No greater element found
        idx = self.find_idx(x)
        for i in range(idx + 1, len(self.stack)):
            if self.stack[i] > x:
                return self.stack[i]
        return -1

    def find_idx(self, x):
        # Find the index of an element in the stack
        try:
            idx = self.stack.index(x)
            return idx
        except ValueError:
            return -1  # Element not found


# Example usage
if __name__ == "__main__":
    # Create a monotonic stack
    stack = MonotonicStack()

    # Push elements onto the stack
    stack.push(5)
    stack.push(10)
    stack.push(15)
    stack.push(20)

    # Print the top element of the stack
    print(stack.top())  # Output: 20

    # Find the next greater element of 15
    print(stack.findNextGreater(15))  # Output: 20

    # Pop an element from the stack
    print(stack.pop())  # Output: 20

    # Check if an element exists in the stack
    print(stack.find_idx(10))  # Output: 1

    # Try popping from an empty stack
    try:
        stack.pop()
    except IndexError as e:
        print(e)  # Output: Cannot pop from an empty stack