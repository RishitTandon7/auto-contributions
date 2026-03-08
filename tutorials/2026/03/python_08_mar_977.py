# Dijkstra's Shortest Path Algorithm

# Importing necessary module
import sys
import heapq

# Defining a class for a graph
class Graph:
    def __init__(self):
        self.vertices = {}

    # Function to add a vertex
    def add_vertex(self, vertex):
        self.vertices[vertex] = {}

    # Function to add an edge
    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1][vertex2] = weight
            self.vertices[vertex2][vertex1] = weight  # For undirected graph

    # Function to implement Dijkstra's algorithm
    def dijkstra(self, start_vertex):
        # Create a dictionary to store the shortest distances
        distances = {vertex: sys.maxsize for vertex in self.vertices}
        distances[start_vertex] = 0

        # Create a priority queue to store vertices
        priority_queue = [(0, start_vertex)]

        while priority_queue:
            # Extract the vertex with the minimum distance
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # If the current distance is greater than the already found distance, skip it
            if current_distance > distances[current_vertex]:
                continue

            # Iterate over the neighbors of the current vertex
            for neighbor, weight in self.vertices[current_vertex].items():
                # Calculate the distance to the neighbor
                distance = current_distance + weight

                # If the calculated distance is less than the already found distance, update it
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# Creating a graph
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')

# Adding edges
graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'C', 5)
graph.add_edge('B', 'D', 1)
graph.add_edge('C', 'D', 3)
graph.add_edge('C', 'E', 2)
graph.add_edge('D', 'E', 1)

# Running Dijkstra's algorithm
distances = graph.dijkstra('A')

# Printing the shortest distances
print("Shortest distances from vertex 'A':")
for vertex, distance in distances.items():
    print(f"{vertex}: {distance}")