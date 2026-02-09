# Hash Map Implementation in Python
"""
This script provides an implementation of a hash map data structure in Python.

A hash map is a type of data structure that maps keys to values using a hash function.
"""

class HashMap:
    def __init__(self, size=1000):
        """
        Initialize the hash map with a given size.

        :param size: The initial capacity of the hash map.
        """
        self.size = size
        # Create a list to store the buckets of the hash map.
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        """
        Calculate the index of the bucket where the key-value pair should be stored.

        :param key: The key to be hashed.
        :return: The calculated index.
        """
        return hash(key) % self.size

    def put(self, key, value):
        """
        Add a key-value pair to the hash map.

        :param key: The key of the key-value pair.
        :param value: The value of the key-value pair.
        """
        # Calculate the index of the bucket where the key should be stored.
        index = self._hash(key)
        # Check if the bucket already exists.
        if not self.buckets[index]:
            # If the bucket does not exist, create it.
            self.buckets[index] = []
        # Add the key-value pair to the bucket.
        self.buckets[index].append((key, value))

    def get(self, key):
        """
        Get the value associated with a given key from the hash map.

        :param key: The key whose value is to be retrieved.
        :return: The value associated with the key if it exists; otherwise, None.
        """
        # Calculate the index of the bucket where the key should be stored.
        index = self._hash(key)
        # Check if the bucket exists and contains the key.
        if self.buckets[index] and (key, _) in self.buckets[index]:
            # If the key is found, return its value.
            return self.buckets[index][index].get(1)
        # If the key is not found, return None.
        return None

    def remove(self, key):
        """
        Remove a key-value pair from the hash map.

        :param key: The key of the key-value pair to be removed.
        """
        # Calculate the index of the bucket where the key should be stored.
        index = self._hash(key)
        # Check if the bucket exists and contains the key.
        if self.buckets[index] and (key, _) in self.buckets[index]:
            # Remove the key-value pair from the bucket.
            self.buckets[index].remove((key, _))

# Example usage of the hash map
if __name__ == "__main__":
    # Create a new hash map with an initial capacity of 1000.
    hash_map = HashMap()
    # Add some key-value pairs to the hash map.
    hash_map.put("apple", 1)
    hash_map.put("banana", 2)
    hash_map.put("orange", 3)
    # Get and print the values associated with certain keys.
    print(hash_map.get("apple"))  # Output: 1
    print(hash_map.get("banana"))  # Output: 2
    print(hash_map.get("orange"))