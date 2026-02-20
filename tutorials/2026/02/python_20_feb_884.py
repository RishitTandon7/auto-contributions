# Breadth First Search (BFS) Graph Traversal in Python

class Graph:
    # Initialize a graph with adjacency list representation
    def __init__(self):
        self.adj_list = {}

    # Function to add an edge to the graph
    def add_edge(self, src, dest):
        # Check if the source and destination are already in the graph
        if src not in self.adj_list:
            self.adj_list[src] = []
        if dest not in self.adj_list:
            self.adj_list[dest] = []
        # Add the destination to the source's adjacency list
        self.adj_list[src].append(dest)

    # Function to perform BFS traversal of the graph
    def bfs_traversal(self, start_vertex):
        # Initialize a visited set to keep track of visited vertices
        visited = set()
        # Initialize a queue with the start vertex
        queue = [start_vertex]
        # Mark the start vertex as visited
        visited.add(start_vertex)
        # Initialize a list to store the traversal order
        traversal_order = []

        while queue:
            # Dequeue the next vertex
            vertex = queue.pop(0)
            # Add the vertex to the traversal order
            traversal_order.append(vertex)
            # Iterate over the neighbors of the current vertex
            for neighbor in self.adj_list[vertex]:
                # If the neighbor has not been visited, mark it as visited and enqueue it
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return traversal_order

# Create a graph with edges
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('D', 'E')

# Perform BFS traversal starting from vertex 'A'
print("BFS Traversal Order:")
print(g.bfs_traversal('A'))  # Output: ['A', 'B', 'C', 'D', 'E', 'F']