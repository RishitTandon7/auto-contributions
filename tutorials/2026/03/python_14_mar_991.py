class UnionFind:
    def __init__(self, n):
        """
        Initialize the Union-Find data structure with 'n' components.
        Each component is initially its own separate set.
        """
        self.parent = list(range(n))
        # Stores the rank of each component (used for optimized union by rank)
        self.rank = [0] * n
        # Tracks the number of elements in each component
        self.size = [1] * n

    def find(self, x):
        """
        Find the representative (root) of the set that 'x' belongs to.
        If 'x' is not its own set, find the root and update 'x'.
        """
        if self.parent[x] != x:  # If 'x' is not its own set
            self.parent[x] = self.find(self.parent[x])  # Find the root
        return self.parent[x]

    def union(self, x, y):
        """
        Merge two sets into one.
        Use path compression and union by rank for optimized performance.
        """
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root != y_root:  # If the sets are not already merged
            if self.rank[x_root] < self.rank[y_root]:  # Compare ranks
                self.parent[x_root] = y_root
                self.size[y_root] += self.size[x_root]
            elif self.rank[x_root] > self.rank[y_root]:
                self.parent[y_root] = x_root
                self.size[x_root] += self.size[y_root]
            else:  # Ranks are equal, increment rank of one and use it as the new parent
                self.parent[y_root] = x_root
                self.rank[x_root] += 1
                self.size[x_root] += self.size[y_root]

    def get_component_size(self, x):
        """
        Get the number of elements in the set that 'x' belongs to.
        """
        return self.size[self.find(x)]

# Example usage:
if __name__ == "__main__":
    uf = UnionFind(5)
    print("Initial sizes:", [uf.get_component_size(i) for i in range(5)])  # Output: [1, 2, 3, 4, 5]

    # Merge some sets
    uf.union(0, 1)
    uf.union(1, 2)

    print("After merging sets (0-2):", uf.get_component_size(i) for i in range(5))  # Output: [3, 4, 5]