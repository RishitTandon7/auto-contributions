def compute_prefix_function(pattern):
    # Initialize the prefix function with zeros for pattern length
    prefix = [0] * len(pattern)
    
    # Initialize j to 1 and i to 0
    j = 1
    i = 0
    
    # Loop through pattern string
    while i < len(pattern) - 1:
        if pattern[i] == pattern[j]:
            # If the characters match, update prefix at index i
            prefix[i + 1] = j + 1
            # Move to next character in both strings
            i += 1
            j += 1
        elif j > 0:
            # If characters don't match and we have a non-zero prefix value for previous step, use it
            j = prefix[j - 1]
        else:
            # If we reach the end of pattern without finding a character in input string, set prefix at current index to zero
            prefix[i + 1] = 0
            i += 1
    
    return prefix


def knuth_morris_pratt_search(input_str, pattern):
    # Initialize prefix function for pattern
    prefix = compute_prefix_function(pattern)
    
    # Initialize j to 0 and m to length of input string
    j = 0
    m = len(input_str)
    
    # Loop through each character in input string
    while j < m:
        if input_str[j] == pattern[j]:
            # If characters match, move forward in both strings
            j += 1
        elif j > 0:
            # If characters don't match and we have a non-zero prefix value for previous step, use it
            j = prefix[j - 1]
        else:
            # If we reach the end of pattern without finding a character in input string, move to next position
            j += 1
    
    # If j is equal to length of pattern, we have found a match
    if j == len(pattern):
        return True, j
    else:
        return False, None


# Example usage
input_str = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

match_found, start_index = knuth_morris_pratt_search(input_str, pattern)

if match_found:
    print(f"Pattern '{pattern}' found at index {start_index} in input string.")
else:
    print(f"Pattern '{pattern}' not found in input string.")