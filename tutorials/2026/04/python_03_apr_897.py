# Dynamic Programming Memoization Example

def fibonacci(n, memo={}):
    """
    Calculate the nth Fibonacci number using memoization.
    
    Args:
        n (int): The index of the Fibonacci number to calculate.
        memo (dict): A dictionary to store previously calculated values.
        
    Returns:
        int: The nth Fibonacci number.
    """
    
    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n
    
    # Check if the value for n is already in memo
    if n not in memo:
        # Calculate the value by recursively calling fibonacci for n-1 and n-2
        # and store it in memo
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    
    # Return the stored value for n
    return memo[n]


# Test the function
print("Fibonacci numbers:")
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")