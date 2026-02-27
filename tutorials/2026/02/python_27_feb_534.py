class UnionFind:
    def __init__(self, n):
        # Initialize the parent array, where each element is the parent of itself
        self.parent = list(range(n))
        # Initialize the rank array, where each element is the rank of itself
        self.rank = [0] * n

    def find(self, x):
        # If x is not the parent of itself, find its root and update the parent
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        # Return the root of x
        return self.parent[x]

    def union(self, x, y):
        # Find the roots of x and y
        root_x = self.find(x)
        root_y = self.find(y)
        # If the roots are different, merge the trees
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def is_connected(uf, x, y):
    # Find the roots of x and y
    root_x = uf.find(x)
    root_y = uf.find(y)
    # Return True if the roots are the same, False otherwise
    return root_x == root_y

def num_connected_components(uf, x):
    # Find the root of x
    root = uf.find(x)
    # Initialize the count of connected components
    count = 0
    # Iterate over all elements
    for i in range(len(uf.parent)):
        # If the element is in the same tree as the root, increment the count
        if uf.find(i) == root:
            count += 1
    # Return the count of connected components
    return count

# Example usage
if __name__ == "__main__":
    # Create a UnionFind object with 5 elements
    uf = UnionFind(5)
    # Union elements
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)
    # Print the result of is_connected(uf, 0, 1)
    print(is_connected(uf, 0, 1))  # Output: True
    print(is_connected(uf, 0, 2))  # Output: False
    print(is_connected(uf, 0, 3))  # Output: False
    print(is_connected(uf, 0, 4))  # Output: False
    print(is_connected(uf, 0, 5))  # Output: False
    # Print the result of num_connected_components(uf, 0)
    print(num_connected_components(uf, 0))  # Output: 3