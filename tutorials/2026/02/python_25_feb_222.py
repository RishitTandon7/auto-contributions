def compute_prefix_function(pattern):
    # Create a list to store the prefix function values
    prefix = [0] * len(pattern)
    # Initialize the prefix value for the first character
    prefix[0] = 0
    # Iterate through the pattern starting from the second character
    for i in range(1, len(pattern)):
        # Initialize the length of the longest proper prefix that is also a proper suffix
        j = prefix[i - 1]
        # While the current character does not match the character at the end of the prefix
        while j > 0 and pattern[i] != pattern[j]:
            # Update the prefix value using the previous prefix value
            j = prefix[j - 1]
        # If the characters match, increment the prefix value
        if pattern[i] == pattern[j]:
            j += 1
        # Update the prefix value for the current character
        prefix[i] = j
    return prefix

def knuth_morris_pratt_search(text, pattern):
    # Compute the prefix function for the pattern
    prefix = compute_prefix_function(pattern)
    # Initialize the text index and pattern index
    i = j = 0
    # Iterate through the text
    while i < len(text):
        # If the current character matches the character at the pattern index
        if text[i] == pattern[j]:
            # Increment both the text index and the pattern index
            i += 1
            j += 1
            # If the pattern index reaches the end of the pattern, we have a match
            if j == len(pattern):
                # Find the match position in the text
                match_start = i - j
                print(f"Match found at position {match_start}")
                # Reset the pattern index
                j = prefix[j - 1]
        # If the current character does not match the character at the pattern index
        elif j > 0:
            # Update the pattern index using the previous prefix value
            j = prefix[j - 1]
        else:
            # Increment the text index
            i += 1
    return

# Test the KMP algorithm
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
knuth_morris_pratt_search(text, pattern)