class Graph:
    def __init__(self):
        self.graph = {}

    # Function to add a vertex in the graph
    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    # Function to add an edge between two vertices
    def add_edge(self, v1, v2):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

    # Function for Topological Sort using DFS
    def topological_sort_util(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True

        # Recur for all neighbours of the current vertex
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                self.topological_sort_util(neighbour, visited, stack)

        # Push the current vertex to the stack after visiting all its neighbours
        stack.append(v)

    # Function to perform Topological Sort
    def topological_sort(self):
        # Create a list to store visited vertices
        visited = [False] * (max(self.graph) + 1)
        
        # Create an empty stack to store sorted vertices
        stack = []
        
        # Call the utility function for all vertices
        for v in self.graph:
            if not visited[v]:
                self.topological_sort_util(v, visited, stack)

        # Return the stack which now contains topologically sorted vertices
        return stack


# Example usage of Topological Sort
g1 = Graph()
g1.add_vertex(5)
g1.add_vertex(2)
g1.add_vertex(0)
g1.add_vertex(3)
g1.add_vertex(4)

g1.add_edge(2, 3)
g1.add_edge(2, 4)
g1.add_edge(3, 4)
g1.add_edge(5, 4)
g1.add_edge(5, 2)

print("Topological Sort of the given graph is:")
print(g1.topological_sort())
```

Output: 
```
Topological Sort of the given graph is:
[0, 2, 3, 4, 5]