# Union-Find Algorithm

```python
class UnionFind:
    def __init__(self, size):
        """
        Initializes the Union-Find data structure.
        
        Args:
        size (int): The number of elements in the set.
        """
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        """
        Finds the root of the set that contains x.
        
        Args:
        x (int): The element to find the root for.
        
        Returns:
        int: The root of the set that contains x.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        Merges the sets that contain x and y.
        
        Args:
        x (int): The first element.
        y (int): The second element.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

# Example usage
if __name__ == "__main__":
    # Create a Union-Find data structure with 5 elements
    uf = UnionFind(5)

    # Add elements to the sets
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)
    uf.union(4, 0)

    # Find the root of each set
    print("Root of set 0:", uf.find(0))  # Output: 0
    print("Root of set 1:", uf.find(1))  # Output: 0
    print("Root of set 2:", uf.find(2))  # Output: 0
    print("Root of set 3:", uf.find(3))  # Output: 3
    print("Root of set 4:", uf.find(4))  # Output: 3

    # Merge two sets
    uf.union(2, 3)

    # Find the root of each set
    print("Root of set 0:", uf.find(0))  # Output: 0
    print("Root of set 1:", uf.find(1))  # Output: 0
    print("Root of set 2:", uf.find(2))  # Output: 0
    print("Root of set 3:", uf.find(3))  # Output: 0
    print("Root of set 4:", uf.find(4))  # Output: 0