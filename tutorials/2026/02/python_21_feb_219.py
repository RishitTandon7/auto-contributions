# dp_memoization.py

def fibonacci(n, memo={}):
    """
    Calculate the nth Fibonacci number using memoization.
    
    Args:
    n (int): The position of the Fibonacci number to calculate.
    memo (dict): A dictionary to store previously calculated Fibonacci numbers.
    
    Returns:
    int: The nth Fibonacci number.
    """
    # Base case: If n is 0 or 1, return n
    if n <= 1:
        return n
    
    # Check if the Fibonacci number for n is already in the memo dictionary
    if n not in memo:
        # If not, calculate it and store it in the memo dictionary
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    
    # Return the Fibonacci number for n
    return memo[n]


# Example usage
if __name__ == "__main__":
    n = 10  # Calculate the 10th Fibonacci number
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")