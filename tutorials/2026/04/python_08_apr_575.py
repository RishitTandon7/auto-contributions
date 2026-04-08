# Topological Sort in Python
# ===========================

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        # Create an adjacency list representation of the graph
        self.adj_list = [[] for _ in range(vertices)]

    # Add a directed edge from vertex u to vertex v
    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    # Perform topological sort using DFS
    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self._dfs(i, visited, stack)
        return stack

    # Recursive helper function for DFS
    def _dfs(self, vertex, visited, stack):
        visited[vertex] = True  # Mark the current vertex as visited
        # Recur for all adjacent vertices
        for neighbor in self.adj_list[vertex]:
            if not visited[neighbor]:
                self._dfs(neighbor, visited, stack)
        stack.append(vertex)  # Push the current vertex to the stack


# Create a graph with 6 vertices
g = Graph(6)

# Add edges to the graph
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

# Perform topological sort
sorted_vertices = g.topological_sort()

# Print the sorted vertices
print("Topological Sort:")
for vertex in sorted_vertices:
    print(vertex)