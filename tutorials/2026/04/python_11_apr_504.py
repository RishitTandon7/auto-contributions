def fibonacci(n, memo = {}):
    # Base case: if n is less than or equal to 0, return 0
    if n <= 0:
        return 0
    
    # If the Fibonacci number for n has already been calculated, return it from the memo dictionary
    if n in memo:
        return memo[n]
    
    # Calculate the Fibonacci number for n as the sum of the two preceding numbers (n-1 and n-2)
    # Store this value in the memo dictionary to avoid repeating calculations later on
    result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    memo[n] = result
    
    return result

# Example usage:
print(fibonacci(10))  # Output: 55