# Caesar Cipher Decoder Tutorial
#
# Learning Objective: This tutorial will teach you how to decode messages
# encrypted with a Caesar cipher in Python. You'll learn fundamental
# programming concepts like string manipulation, character encoding,
# loops, and conditional statements. By the end, you'll have a working
# decoder and a better understanding of how to process text data.

def caesar_decode(encoded_message, shift):
    """
    Decodes a message encrypted using the Caesar cipher.

    The Caesar cipher is a simple substitution cipher where each letter
    in the plaintext is shifted a certain number of places down or up
    the alphabet. For example, with a shift of 3, 'A' would become 'D',
    'B' would become 'E', and so on.

    This function takes the encoded message and the shift value used for
    encryption and returns the original, decoded message.

    Args:
        encoded_message (str): The message that has been encrypted.
        shift (int): The number of positions each letter was shifted during encryption.

    Returns:
        str: The decoded (original) message.
    """
    decoded_message = ""  # Initialize an empty string to store our decoded message.
                          # We'll build this up character by character.

    # We need to iterate through each character in the encoded message.
    # A 'for' loop is perfect for this, as it allows us to process
    # each item in a sequence (like a string).
    for char in encoded_message:
        # First, let's check if the current character is an alphabet letter.
        # Non-alphabetic characters (like spaces, punctuation, numbers)
        # should not be shifted. We can use the `.isalpha()` string method
        # to check if a character is a letter.
        if char.isalpha():
            # If it is a letter, we need to determine if it's uppercase or lowercase.
            # This is important because the alphabet wraps around differently
            # for uppercase and lowercase letters.
            if char.isupper():
                # For uppercase letters:
                # 1. Get the ASCII value of the character using `ord()`.
                #    ASCII (American Standard Code for Information Interchange)
                #    is a numerical representation of characters.
                #    'A' is 65, 'B' is 66, ..., 'Z' is 90.
                # 2. Subtract the ASCII value of 'A' to get its position in the alphabet
                #    (0 for 'A', 1 for 'B', ..., 25 for 'Z'). This is our "0-indexed" position.
                # 3. Subtract the 'shift' value. This is the core decoding step.
                #    We're reversing the encryption shift.
                # 4. Use the modulo operator (%) with 26 (the number of letters in the alphabet).
                #    This handles "wrapping around" the alphabet. For example, if we have
                #    a letter 'A' (position 0) and a shift of 3, decoding would result
                #    in 0 - 3 = -3. -3 % 26 gives us 23, which corresponds to 'X'.
                #    This ensures we stay within the 0-25 range.
                # 5. Add back the ASCII value of 'A' to convert our 0-indexed position
                #    back into an ASCII value.
                # 6. Convert the ASCII value back to a character using `chr()`.
                start = ord('A')
                decoded_char_code = (ord(char) - start - shift) % 26 + start
                decoded_char = chr(decoded_char_code)
            else: # It's a lowercase letter
                # Similar logic for lowercase letters.
                # 'a' is 97, 'b' is 98, ..., 'z' is 122.
                start = ord('a')
                decoded_char_code = (ord(char) - start - shift) % 26 + start
                decoded_char = chr(decoded_char_code)

            # Append the decoded character to our result string.
            decoded_message += decoded_char
        else:
            # If the character is not a letter, just append it as is.
            # This preserves spaces, punctuation, and numbers.
            decoded_message += char

    # After looping through all characters, return the complete decoded message.
    return decoded_message

# --- Example Usage ---

# Let's say we have a message that was encrypted with a shift of 3.
# Example encrypted message: "Khoor, Zruog!"
# This would have been "Hello, World!" with a shift of 3.

# We need to know the shift value that was used for encryption.
encryption_shift = 3
my_encoded_message = "Khoor, Zruog!"

# Now, let's call our function to decode it.
original_message = caesar_decode(my_encoded_message, encryption_shift)

# Print the results to see our decoded message.
print(f"Encoded Message: {my_encoded_message}")
print(f"Encryption Shift: {encryption_shift}")
print(f"Decoded Message: {original_message}")

print("-" * 20) # Just a separator for clarity

# Another example:
another_encoded_message = "Wklv lv d whvw phvvdjh."
another_shift = 3
decoded_test_message = caesar_decode(another_encoded_message, another_shift)

print(f"Encoded Message: {another_encoded_message}")
print(f"Encryption Shift: {another_shift}")
print(f"Decoded Message: {decoded_test_message}")

print("-" * 20)

# Example with a different shift:
shift_of_5_encoded = "Mjqqt, Btwqi!" # "Hello, World!" shifted by 5
shift_value_5 = 5
decoded_shift_5 = caesar_decode(shift_of_5_encoded, shift_value_5)

print(f"Encoded Message: {shift_of_5_encoded}")
print(f"Encryption Shift: {shift_value_5}")
print(f"Decoded Message: {decoded_shift_5}")