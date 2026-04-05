# Dynamic Programming with Memoization
=====================================

This script explains the concept of dynamic programming using memoization in Python.

```python
def fibonacci(n, memo={}):
    # Base cases: if n is 0 or 1, return it directly
    if n <= 1:
        return n
    
    # Check if we've already computed this value
    if n not in memo:
        # If not, compute it and store it in the dictionary
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    
    # Return the result from the dictionary
    return memo[n]

def fibonacci_iterative(n):
    fib_values = [0, 1]
    
    # Compute Fibonacci values up to n and store them in the list
    for i in range(2, n+1):
        fib_values.append(fib_values[i-1] + fib_values[i-2])
    
    # Return the nth value
    return fib_values[n]

def fibonacci_recursive(n):
    if n <= 1:
        return n
    
    # Recursive call to compute the next Fibonacci number
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Example usage
n = 10

print("Fibonacci function with memoization:", fibonacci(n))
print("Fibonacci function using iteration:", fibonacci_iterative(n))
print("Fibonacci function using recursion:", fibonacci_recursive(n))