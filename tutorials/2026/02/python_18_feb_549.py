class UnionFind:
    def __init__(self, size):
        # Initialize the parent array with each element as itself
        self.parent = list(range(size))
    
    # Function to find the root of a node
    def find(self, x):
        if self.parent[x] != x:  # If the element is not its own parent
            self.parent[x] = self.find(self.parent[x])  # Recursively find and update the parent
        return self.parent[x]
    
    # Function to union two nodes
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:  # If the elements are not already in the same group
            self.parent[root_x] = root_y  # Make one element its parent

# Example usage:
if __name__ == "__main__":
    uf = UnionFind(6)  # Create a union-find object with 6 nodes
    
    print("Initial groups:")
    for i in range(6):
        print(f"Node {i} is in group: {uf.find(i)}")
    
    uf.union(0, 1)  # Merge node 0 and node 1
    uf.union(2, 3)  # Merge node 2 and node 3
    
    print("\nGroups after union operations:")
    for i in range(6):
        print(f"Node {i} is in group: {uf.find(i)}")
    
    # Check if nodes 0 and 1 are still in the same group
    assert uf.find(0) == uf.find(1)
    
    # Check if nodes 2 and 3 are still in the same group
    assert uf.find(2) == uf.find(3)