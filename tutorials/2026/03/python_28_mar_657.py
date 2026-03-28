# Breadth First Search Graph Traversal in Python

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]

    # Function to add an edge between two vertices
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # For undirected graph

    # Function to perform BFS traversal of the graph
    def bfs_traversal(self, start_vertex):
        visited = [False] * self.V
        distance = [-1] * self.V
        queue = []

        # Create a queue and add the starting vertex
        queue.append(start_vertex)
        visited[start_vertex] = True

        while queue:
            current_vertex = queue.pop(0)

            print(current_vertex, end=" ")

            for neighbor in self.adj_list[current_vertex]:
                if not visited[neighbor]:
                    distance[neighbor] = distance[current_vertex] + 1
                    queue.append(neighbor)
                    visited[neighbor] = True

    # Example usage of BFS traversal
if __name__ == "__main__":
    g = Graph(6)  # Create a graph with 6 vertices
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)

    print("BFS Traversal:")
    g.bfs_traversal(0)  # Perform BFS traversal starting from vertex 0