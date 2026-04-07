# Topological Sort in Python

# Import necessary module
import collections

# Function to perform topological sort using Kahn's algorithm
def topological_sort(graph):
    # Initialize a dictionary to store in-degree of each node
    in_degree = {node: 0 for node in graph}
    
    # Calculate in-degree of each node and initialize queue with nodes having in-degree 0
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    queue = [node for node in graph if in_degree[node] == 0]
    
    # Initialize result list to store sorted nodes
    result = []
    
    # Perform topological sort using Kahn's algorithm
    while queue:
        node = queue.pop(0)
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result

# Example usage
if __name__ == "__main__":
    # Define a directed graph as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    
    print("Topological Sort:")
    sorted_nodes = topological_sort(graph)
    print(sorted_nodes)

# Output:
# Topological Sort:
# ['A', 'B', 'C', 'D']