# String Hashing in Python

# Import the required modules
import hashlib

# Function to calculate the hash of a string using SHA-256
def calculate_hash(string):
    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256()
    
    # Convert the string to bytes and update the hash object
    hash_object.update(string.encode('utf-8'))
    
    # Get the hexadecimal representation of the hash
    hash_hex = hash_object.hexdigest()
    
    return hash_hex

# Function to calculate the hash of a string using MD5
def calculate_md5_hash(string):
    # Create a new MD5 hash object
    hash_object = hashlib.md5()
    
    # Convert the string to bytes and update the hash object
    hash_object.update(string.encode('utf-8'))
    
    # Get the hexadecimal representation of the hash
    hash_hex = hash_object.hexdigest()
    
    return hash_hex

# Function to calculate the hash of a string using Repeated Hashing
def calculate_repeated_hash(string, iterations=3):
    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256()
    
    # Convert the string to bytes and update the hash object
    hash_object.update(string.encode('utf-8'))
    
    # Calculate the hash for the specified number of iterations
    for _ in range(iterations):
        hash_object.update(hash_object.digest())
    
    # Get the hexadecimal representation of the hash
    hash_hex = hash_object.hexdigest()
    
    return hash_hex

# Test the functions with a sample string
sample_string = "Hello, World!"

# Calculate the SHA-256 hash of the sample string
sha256_hash = calculate_hash(sample_string)
print("SHA-256 Hash:", sha256_hash)

# Calculate the MD5 hash of the sample string
md5_hash = calculate_md5_hash(sample_string)
print("MD5 Hash:", md5_hash)

# Calculate the repeated hash of the sample string
repeated_hash = calculate_repeated_hash(sample_string)
print("Repeated Hash:", repeated_hash)