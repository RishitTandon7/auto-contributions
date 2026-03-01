# Hash Map Implementation in Python

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self, size=1000):
        # Initialize the size of the hash map
        self.size = size
        # Create an empty array to store the nodes
        self.array = [None] * size

    def _hash(self, key):
        # Calculate the hash value using the modulo operator
        return hash(key) % self.size

    def put(self, key, value):
        # Calculate the index of the array using the hash value
        index = self._hash(key)
        # Check if the key already exists in the array
        if self.array[index] is not None:
            # If the key exists, update its value
            self.array[index].value = value
        else:
            # If the key does not exist, create a new node and add it to the array
            self.array[index] = Node(key, value)

    def get(self, key):
        # Calculate the index of the array using the hash value
        index = self._hash(key)
        # Check if the key exists in the array
        if self.array[index] is not None:
            # If the key exists, return its value
            return self.array[index].value
        else:
            # If the key does not exist, return None
            return None

    def delete(self, key):
        # Calculate the index of the array using the hash value
        index = self._hash(key)
        # Check if the key exists in the array
        if self.array[index] is not None:
            # If the key exists, remove it from the array
            self.array[index] = None

def main():
    # Create a new hash map
    hash_map = HashMap()
    # Add some key-value pairs to the hash map
    hash_map.put('apple', 5)
    hash_map.put('banana', 10)
    hash_map.put('orange', 15)
    # Get the value of a key
    print(hash_map.get('apple'))  # Output: 5
    # Delete a key
    hash_map.delete('banana')
    # Check if the key still exists
    print(hash_map.get('banana'))  # Output: None

if __name__ == '__main__':
    main()