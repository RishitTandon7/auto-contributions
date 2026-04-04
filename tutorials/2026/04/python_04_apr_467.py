# Knuth-Morris-Pratt String Search Algorithm
```python
def compute_prefix_function(pattern):
    # Initialize the prefix function with zeros
    m = len(pattern)
    pi = [0] * m

    # Compute the prefix function values
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[j] != pattern[i]:
            j = pi[j - 1]
        if pattern[j] == pattern[i]:
            j += 1
        pi[i] = j

    return pi


def kmp_search(text, pattern):
    # Compute the prefix function for the pattern
    pi = compute_prefix_function(pattern)

    # Initialize pointers for text and pattern
    i = 0
    j = 0

    # Search for the pattern in the text
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

            # If the entire pattern is found, return the index
            if j == len(pattern):
                return i - j

        elif j > 0:
            j = pi[j - 1]

        else:
            i += 1

    # Pattern not found in the text
    return None


# Example usage
text = "banana"
pattern = "ana"

index = kmp_search(text, pattern)

if index is not None:
    print(f"Pattern '{pattern}' found at index {index} in the text.")
else:
    print(f"Pattern '{pattern}' not found in the text.")