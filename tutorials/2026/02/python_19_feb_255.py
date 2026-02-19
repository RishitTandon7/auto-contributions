# Dynamic Programming Memoization in Python

def fibonacci(n, memo={}):
    """
    Compute the nth Fibonacci number using dynamic programming memoization.
    
    Args:
        n (int): The index of the Fibonacci number to compute.
        memo (dict, optional): A dictionary to store previously computed values. Defaults to {}.
        
    Returns:
        int: The nth Fibonacci number.
    """

    # Base case: If n is 0 or 1, return n
    if n <= 1:
        return n
    
    # Check if the Fibonacci number has already been computed
    if n in memo:
        # If it has, return the stored value
        return memo[n]
    
    # Compute the nth Fibonacci number using recursion and memoization
    else:
        # Recursively compute the (n-1)th and (n-2)th Fibonacci numbers
        result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        
        # Store the computed value in the memo dictionary
        memo[n] = result
        
        # Return the computed value
        return result

# Test the function with different values of n
for i in range(10):
    print(f"Fibonacci number at index {i}: {fibonacci(i)}")