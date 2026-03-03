# Union-Find Data Structure in Python
=====================================

### Overview

This Python code implements the Union-Find data structure, also known as the disjoint-set data structure. It allows us to perform operations on a set of elements, such as union and find.

### Implementation

```python
class UnionFind:
    def __init__(self, n):
        """
        Initializes the Union-Find data structure with n elements.
        
        :param n: The number of elements in the set.
        """
        # Create a list to store the parent of each element
        self.parent = list(range(n))
        
        # Create a list to store the rank of each element
        self.rank = [0] * n

    def find(self, x):
        """
        Finds the root of the set that contains x.
        
        :param x: The element to find the root for.
        :return: The root of the set.
        """
        # If x is not the root, find the root and update the parent
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        Merges the sets that contain x and y.
        
        :param x: The element to merge with.
        :param y: The element to merge with.
        """
        # Find the roots of the sets that contain x and y
        root_x = self.find(x)
        root_y = self.find(y)
        
        # If the roots are different, merge the sets
        if root_x != root_y:
            # If the rank of root_x is less than the rank of root_y, 
            # make root_y the parent of root_x
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            # If the rank of root_x is greater than the rank of root_y, 
            # make root_x the parent of root_y and increment the rank of root_x
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_x] += 1

# Example usage:
if __name__ == "__main__":
    # Create a Union-Find data structure with 5 elements
    uf = UnionFind(5)
    
    # Perform some operations
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(0, 2)
    
    # Find the roots of the sets
    print("Root of set 0:", uf.find(0))
    print("Root of set 1:", uf.find(1))
    print("Root of set 2:", uf.find(2))
    print("Root of set 3:", uf.find(3))
    print("Root of set 4:", uf.find(4))