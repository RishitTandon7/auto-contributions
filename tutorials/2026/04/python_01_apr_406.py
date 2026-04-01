# Monotonic Stack Implementation in Python

class MonotonicStack:
    def __init__(self):
        # Initialize an empty list to store elements
        self.stack = []

    def is_monotonically_increasing(self):
        """
        Check if the stack is monotonically increasing.
        
        Returns:
            bool: True if the stack is monotonically increasing, False otherwise.
        """
        # Iterate through all elements in the stack
        for i in range(1, len(self.stack)):
            # If the current element is less than or equal to the previous one,
            # the stack is not monotonically increasing
            if self.stack[i] <= self.stack[i - 1]:
                return False
        # If no decreasing pair is found, the stack is monotonically increasing
        return True

    def is_monotonically_decreasing(self):
        """
        Check if the stack is monotonically decreasing.
        
        Returns:
            bool: True if the stack is monotonically decreasing, False otherwise.
        """
        # Iterate through all elements in the stack
        for i in range(1, len(self.stack)):
            # If the current element is greater than or equal to the previous one,
            # the stack is not monotonically decreasing
            if self.stack[i] >= self.stack[i - 1]:
                return False
        # If no increasing pair is found, the stack is monotonically decreasing
        return True

    def push(self, element):
        """
        Push an element onto the stack.
        
        Args:
            element: The element to be pushed onto the stack.
        """
        self.stack.append(element)

    def pop(self):
        """
        Pop an element from the stack.
        
        Returns:
            The popped element.
        """
        return self.stack.pop()

# Run the example
if __name__ == "__main__":
    # Create a monotonic stack
    ms = MonotonicStack()
    
    # Push elements onto the stack
    ms.push(1)
    ms.push(2)
    ms.push(3)
    ms.push(4)
    ms.push(5)

    print("Is monotonically increasing?", ms.is_monotonically_increasing())
    print("Is monotonically decreasing?", ms.is_monotonically_decreasing())

    # Pop elements from the stack
    while True:
        element = ms.pop()
        if element == 1:
            break

    print("Popped element:", element)