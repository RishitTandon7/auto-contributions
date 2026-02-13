# String Hashing with Python

# Introduction to string hashing
def introduction_to_string_hashing():
    print("String hashing is a technique used in computer science to efficiently store and retrieve large amounts of data.")
    print("In this chapter, we will learn about the basics of string hashing.")

# Types of String Hashing
def types_of_string_hashing():
    print("\nThere are several types of string hashing techniques:")
    print("1. Rolling Hashing")
    print("2. Polynomial Hashing")
    print("3. Modular Arithmetic")

# Rolling Hashing
def rolling_hashing():
    # Rolling hash is a technique used to calculate the hash value of a substring.
    print("\nRolling Hashing Technique:")
    s = "hello"
    n = len(s)
    h = 0

    # Calculate the initial hash value.
    for i in range(n):
        h += ord(s[i])

    # Print the initial hash value
    print(f"Initial Hash Value: {h}")

    # To calculate the hash value of a substring, subtract the hash value of the first character from the current character's hash value and add the hash value of the last character.
    s1 = "world"
    n = len(s)
    h = 0

    for i in range(n):
        if i < n-1:
            h += ord(s[i+1])
        else:
            break
        h -= ord(s[i])

    # Print the hash value of a substring
    print(f"Hash Value of Substring: {h}")

# Polynomial Hashing
def polynomial_hashing():
    # Polynomial hashing is another technique used to calculate the hash value of a substring.
    print("\nPolynomial Hashing Technique:")
    s = "hello"
    n = len(s)
    p = 100000003

    h = 0
    for i in range(n):
        h += (ord(s[i]) % p) * pow(p, i, p)

    # Print the initial hash value
    print(f"Initial Hash Value: {h}")

    s1 = "world"
    n = len(s)
    h = 0

    for i in range(n):
        if i < n-1:
            h += (ord(s[i+1]) % p) * pow(p, i, p)
        else:
            break
        h -= (ord(s[i]) % p) * pow(p, i, p)

    # Print the hash value of a substring
    print(f"Hash Value of Substring: {h}")

# Modular Arithmetic
def modular_arithmetic():
    # In modular arithmetic, we use modulo operator to find the remainder when the hash value is divided by a certain number.
    print("\nModular Arithmetic Technique:")
    s = "hello"
    n = len(s)
    m = 100000003

    h = 0
    for i in range(n):
        h += ord(s[i])
        h %= m

    # Print the initial hash value
    print(f"Initial Hash Value: {h}")

    s1 = "world"
    n = len(s)
    h = 0

    for i in range(n):
        if i < n-1:
            h += ord(s[i+1])
            h %= m
        else:
            break
        h