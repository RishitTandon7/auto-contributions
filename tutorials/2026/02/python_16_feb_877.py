# Monotonic Stack Implementation in Python

class MonotonicStack:
    def __init__(self):
        # Initialize a list to store the elements of the stack
        self.stack = []
        # Initialize two lists to store the increasing and decreasing sequences
        self.increasing = []
        self.decreasing = []

    def push(self, x):
        # Add an element to the top of the stack
        self.stack.append(x)
        
        # Check if the stack is empty or not
        if len(self.stack) == 1:
            # If it's empty, we start a new increasing sequence
            self.increasing = [x]
        else:
            # If it's not empty, compare x with the last element in the stack
            last_element = self.stack[-1]
            
            # Check if x is greater than or equal to the last element
            if x >= last_element:
                # If x is greater, add it to the increasing sequence
                self.increasing.append(x)
            else:
                # If x is less, add it to the decreasing sequence
                self.decreasing.append(x)

    def get_increasing(self):
        # Return the list of elements in the increasing sequence
        return self.increasing

    def get_decreasing(self):
        # Return the list of elements in the decreasing sequence
        return self.decreasing


# Test the implementation
if __name__ == "__main__":
    stack = MonotonicStack()
    stack.push(5)
    stack.push(10)
    stack.push(15)
    stack.push(20)
    stack.push(25)

    # Print the increasing and decreasing sequences
    print("Increasing Sequence:", stack.get_increasing())
    print("Decreasing Sequence:", stack.get_decreasing())