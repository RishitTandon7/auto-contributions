# Learning Objective:
# This tutorial will teach you how to build a Python dictionary that
# "remembers" your most frequently accessed items. This is achieved by
# using a specialized dictionary subclass that tracks lookup frequency
# and can potentially be optimized for faster access to these common items.
# We'll focus on creating a custom dictionary that keeps track of lookup counts.

# Import the 'collections' module for useful data structures.
# While not strictly necessary for this *basic* version, it's a good
# habit for more advanced dictionary-like implementations.
import collections

# Define a custom class that inherits from Python's built-in 'dict'.
# This allows our new class to have all the standard dictionary features
# but also lets us add our own custom behavior.
class FrequentLookupDict(dict):
    """
    A dictionary subclass that tracks the frequency of key lookups.

    This class inherits all the functionality of a standard Python dictionary
    but adds a mechanism to record how many times each key has been accessed.
    This can be the foundation for building more advanced features like
    auto-sorting by frequency or implementing a cache.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the FrequentLookupDict.

        It first calls the parent class's __init__ to set up the standard
        dictionary functionality. Then, it initializes an empty dictionary
        to store the lookup counts for each key.
        """
        # Call the initializer of the parent class (dict) to set up the dictionary itself.
        super().__init__(*args, **kwargs)

        # Initialize a dictionary to store the lookup counts.
        # The keys of this dictionary will be the keys of our main dictionary,
        # and the values will be the number of times that key has been looked up.
        self._lookup_counts = {}

        # Pre-populate _lookup_counts if the dictionary is initialized with existing items.
        # We assume initial items have not been looked up yet, so their count is 0.
        for key in self:
            self._lookup_counts[key] = 0

    def __getitem__(self, key):
        """
        Overrides the standard dictionary's get item behavior.

        When a key is accessed using square bracket notation (e.g., my_dict[key]),
        this method is called. We increment the lookup count for that key and
        then return the actual value from the dictionary.
        """
        # Use the parent class's __getitem__ to get the actual value.
        # This is crucial for maintaining standard dictionary behavior.
        value = super().__getitem__(key)

        # Increment the lookup count for the accessed key.
        # If the key is not yet in _lookup_counts (which shouldn't happen if initialized correctly,
        # but is good practice for robustness), defaultdict would be useful here.
        # For simplicity with our __init__ pre-population, we can assume it exists.
        self._lookup_counts[key] = self._lookup_counts.get(key, 0) + 1

        # Return the retrieved value.
        return value

    def get_lookup_count(self, key):
        """
        Returns the number of times a specific key has been looked up.

        Args:
            key: The key whose lookup count is requested.

        Returns:
            The integer count of lookups for the given key.
            Returns 0 if the key doesn't exist or has never been looked up.
        """
        # Use .get() with a default value of 0. This handles cases where
        # the key might not exist in _lookup_counts (e.g., if it was just added
        # and never looked up, or if it's an invalid key).
        return self._lookup_counts.get(key, 0)

    def get_all_lookup_counts(self):
        """
        Returns a copy of the dictionary containing all lookup counts.

        This method allows inspection of the frequency of all keys.
        A copy is returned to prevent external modification of the internal counts.
        """
        return self._lookup_counts.copy()

    # Optional: Override other dictionary methods if you want to track their impact on counts.
    # For example, __setitem__ could reset counts if you wanted that behavior,
    # or __delitem__ could remove an item from _lookup_counts.
    # For this basic tutorial, we focus on __getitem__.

# --- Example Usage ---

# 1. Create an instance of our custom dictionary.
# We can initialize it with some data, just like a regular dictionary.
my_special_dict = FrequentLookupDict({
    "apple": "A fruit, typically red or green.",
    "banana": "A long, curved fruit with yellow skin.",
    "cherry": "A small, round, red or black fruit.",
    "date": "A sweet, brown fruit from a palm tree."
})

# 2. Access some items to "train" the dictionary.
print("--- Initializing and accessing items ---")
print(f"Looking up 'apple': {my_special_dict['apple']}")
print(f"Looking up 'banana': {my_special_dict['banana']}")
print(f"Looking up 'apple' again: {my_special_dict['apple']}")
print(f"Looking up 'cherry': {my_special_dict['cherry']}")
print(f"Looking up 'apple' a third time: {my_special_dict['apple']}")
print(f"Looking up 'banana' again: {my_special_dict['banana']}")

# 3. Check the lookup counts for specific keys.
print("\n--- Checking lookup counts ---")
print(f"Lookup count for 'apple': {my_special_dict.get_lookup_count('apple')}")
print(f"Lookup count for 'banana': {my_special_dict.get_lookup_count('banana')}")
print(f"Lookup count for 'cherry': {my_special_dict.get_lookup_count('cherry')}")
print(f"Lookup count for 'date' (never looked up): {my_special_dict.get_lookup_count('date')}")
print(f"Lookup count for 'grape' (non-existent): {my_special_dict.get_lookup_count('grape')}")

# 4. View all lookup counts.
print("\n--- All lookup counts ---")
all_counts = my_special_dict.get_all_lookup_counts()
print(all_counts)

# 5. Add a new item and access it.
print("\n--- Adding and accessing a new item ---")
my_special_dict["elderberry"] = "A dark purple berry, often used for juice or jam."
print(f"Looking up 'elderberry': {my_special_dict['elderberry']}")
print(f"Lookup count for 'elderberry': {my_special_dict.get_lookup_count('elderberry')}")

# 6. Notice how accessing an item updates its count.
print("\n--- Accessing 'cherry' again ---")
print(f"Looking up 'cherry': {my_special_dict['cherry']}")
print(f"Lookup count for 'cherry': {my_special_dict.get_lookup_count('cherry')}")