# Trie Data Structure in Python

class TrieNode:
    # Initialize a new node in the trie
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    # Initialize a new trie
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into the trie
    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    # Search for a word in the trie
    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    # Check if a word starts with a certain prefix
    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    # Delete a word from the trie
    def delete(self, word):
        def _delete(current, word, index):
            if index == len(word):
                if not current.is_end_of_word:
                    return False
                current.is_end_of_word = False
                return len(current.children) == 0
            char = word[index]
            if char not in current.children:
                return False
            should_delete_current_node = _delete(current.children[char], word, index + 1)
            if should_delete_current_node:
                del current.children[char]
                return len(current.children) == 0 and not current.is_end_of_word
            return False
        return _delete(self.root, word, 0)

# Example usage
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("banana")
trie.insert("bat")

print(trie.search("apple"))  # Output: True
print(trie.search("app"))     # Output: True
print(trie.search("banana"))  # Output: True
print(trie.search("bat"))     # Output: True
print(trie.search("a"))       # Output: False
print(trie.starts_with("app"))  # Output: True
print(trie.starts_with("b"))    # Output: True
print(trie.delete("apple"))    # Output: True
print(trie.search("apple"))    # Output: False