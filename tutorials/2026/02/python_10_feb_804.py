# Dynamic Programming Memoization Example

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

    # Check if the Fibonacci number has already been calculated
    if n not in memo:
        # Calculate the Fibonacci number using recursion and store it in the dictionary
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)

    # Return the cached Fibonacci number
    return memo[n]


def longest_common_subsequence(seq1, seq2):
    """
    Find the length of the longest common subsequence between two sequences.

    Args:
        seq1 (str): The first sequence.
        seq2 (str): The second sequence.

    Returns:
        int: The length of the longest common subsequence.
    """

    # Create a dictionary to store previously calculated lengths
    memo = {}

    def lcs(i, j):
        """
        Calculate the length of the longest common subsequence using memoization.

        Args:
            i (int): The current position in seq1.
            j (int): The current position in seq2.

        Returns:
            int: The length of the longest common subsequence.
        """

        # Base case: If both sequences are empty, return 0
        if i < 0 and j < 0:
            return 0

        # Check if the length has already been calculated
        if (i, j) in memo:
            return memo[(i, j)]

        # If the current characters match, increment the length and move to the next characters
        if seq1[i] == seq2[j]:
            result = lcs(i-1, j-1)
            if result > 0:
                memo[(i, j)] = result + 1
            else:
                memo[(i, j)] = max(memo.get((i-1, j), 0),
                                   memo.get((i+1, j), 0))
        # If the current characters do not match, move to the next character in seq1
        elif i < len(seq1):
            result = lcs(i-1, j)
            if result > 0:
                memo[(i, j)] = result
            else:
                memo[(i, j)] = max(memo.get((i+1, j), 0),
                                   memo.get((i, j+1), 0))
        # If the current characters do not match and i is out of range, move to the next character in seq2
        elif j < len(seq2):
            result = lcs(i, j-1)
            if result > 0:
                memo[(i, j)] = result
            else:
                memo[(i, j)] = max(memo.get((i, j+1), 0),
                                   memo.get((i-1, j), 0))
        # If the current characters do not match and both sequences are out of range, return 0
        else:
            memo[(i,