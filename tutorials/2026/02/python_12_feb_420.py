# String Hashing using Rolling Hash Technique

def calculate_hash(string, hash_size):
    # Calculate the hash value for the given string
    hash_value = 0
    p = 31
    
    # Traverse the string and update the hash value
    for i in range(len(string)):
        char_value = ord(string[i])
        
        # Update the hash value using rolling hash technique
        hash_value += (char_value - ord('a') + 1) * (p ** (len(string) - i - 1))
        
        # Apply modulo operation to keep hash value within bounds
        hash_value %= hash_size
        
    return hash_value

def string_search(target_string, needle_string):
    # Calculate the length of target and needle strings
    target_len = len(target_string)
    needle_len = len(needle_string)
    
    # Calculate the hash values for both strings
    target_hash = calculate_hash(target_string, 101)
    needle_hash = calculate_hash(needle_string, 101)
    
    # Initialize window boundaries
    left = 0
    
    # Traverse through the string and search for the pattern
    while left <= target_len - needle_len:
        # Calculate hash value for current substring
        current_hash = (target_hash - (ord(target_string[left]) - ord('a') + 1) * (31 ** (left))) % 101
        
        if current_hash == needle_hash:
            # Check for matching characters in the window
            match_index = left
            for i in range(needle_len):
                if target_string[match_index + i] != needle_string[i]:
                    break
            else:
                return match_index
        
        # Move the window to the right
        left += 1
    
    return -1

# Test the function
target_string = "example"
needle_string = "xle"

index = string_search(target_string, needle_string)
if index != -1:
    print(f"Found '{needle_string}' at index {index} in '{target_string}'")
else:
    print(f"'{needle_string}' not found in '{target_string}'")