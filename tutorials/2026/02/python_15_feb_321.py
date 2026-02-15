class UnionFind:
    def __init__(self, n):
        # Initialize the parent array to keep track of parent nodes in the union-find data structure.
        self.parent = list(range(n))
        
        # Initialize the rank array to help us perform operations with efficiency.
        self.rank = [0] * n

    def find(self, x):
        # Path compression optimization: If the element is not its own parent, set it as its own parent.
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Find the roots of both sets.
        root_x = self.find(x)
        root_y = self.find(y)

        # If they are already in the same set, there's no need to do anything.
        if root_x != root_y:
            # Merge the smaller tree into the larger one.
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                # When ranks are equal, we can just increment the rank of one and copy the other.
                self.rank[root_x] += 1

# Create a UnionFind object with n elements (in this case, 5).
uf = UnionFind(5)

# Test cases:
print("Test case 1:")
# Check that each element is its own parent initially
for i in range(5):
    print(f"{i} -> {uf.find(i)}")

print("\nTest case 2:")
# First union operation: 0 and 1 are merged into set {0, 1}
uf.union(0, 1)
# Check that the elements have been correctly grouped
print(f"0 and 1 -> {uf.find(0)} and {uf.find(1)}")

print("\nTest case 3:")
# Second union operation: 2 and 4 are merged into set {0, 1, 2}
uf.union(2, 4)
# Check that the elements have been correctly grouped
print(f"2 and 4 -> {uf.find(2)} and {uf.find(4)}")

print("\nTest case 4:")
# Third union operation: 3 is merged into set {0, 1, 2}
uf.union(3, 0)
# Check that the elements have been correctly grouped
print(f"3 and 0 -> {uf.find(3)} and {uf.find(0)}")

print("\nTest case 5:")
# Fourth union operation: 4 is merged into set {0, 1}
uf.union(4, 1)
# Check that the elements have been correctly grouped
print(f"4 and 1 -> {uf.find(4)} and {uf.find(1)}")