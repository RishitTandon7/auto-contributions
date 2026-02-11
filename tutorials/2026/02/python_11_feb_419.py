import heapq

def dijkstra(graph, start_node):
    # Create a dictionary to store the distance to each node
    distances = {node: float('infinity') for node in graph}
    distances[start_node] = 0
    
    # Create a priority queue to hold nodes to be processed
    pq = [(0, start_node)]
    
    while pq:
        # Get the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(pq)
        
        # If the current distance is greater than the known distance, skip this node
        if current_distance > distances[current_node]:
            continue
        
        # For each neighbor of the current node that has not been processed yet
        for neighbor, weight in graph[current_node].items():
            if neighbor not in distances:
                continue
            
            distance = current_distance + weight
            
            # If a shorter path to this neighbor is found, update its distance and add it to the priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

def print_distances(distances):
    for node in distances:
        print(f"{node}: {distances[node]}")

# Define a graph as an adjacency list
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 2},
    'C': {'A': 3, 'D': 4},
    'D': {'B': 2, 'C': 4}
}

# Run Dijkstra's algorithm on the graph
start_node = 'A'
distances = dijkstra(graph, start_node)

# Print the shortest distances from the start node to all other nodes
print_distances(distances)