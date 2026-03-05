# Topological Sort in Python
================================

## Introduction
---------------

Topological sort is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge u -> v, vertex u comes before v in the ordering.

## Code
------

```python
from collections import defaultdict, deque

def topological_sort(graph):
    """
    Performs a topological sort on a given directed acyclic graph (DAG).

    Args:
        graph (dict): Adjacency list representation of the DAG.

    Returns:
        list: Topologically sorted vertices.
    """
    # Initialize a dictionary to store in-degree of each vertex
    in_degree = defaultdict(int)
    # Initialize a dictionary to store adjacency list
    adj_list = defaultdict(list)

    # Populate in-degree and adjacency list
    for vertex in graph:
        for neighbor in graph[vertex]:
            # Increment in-degree of neighbor
            in_degree[neighbor] += 1
            # Add edge to adjacency list
            adj_list[vertex].append(neighbor)

    # Initialize a queue to store vertices with in-degree 0
    queue = deque([vertex for vertex in graph if in_degree[vertex] == 0])

    # Initialize a list to store topologically sorted vertices
    sorted_vertices = []

    # Perform topological sort
    while queue:
        vertex = queue.popleft()
        sorted_vertices.append(vertex)

        # Decrease in-degree of neighboring vertices
        for neighbor in adj_list[vertex]:
            in_degree[neighbor] -= 1
            # Add neighbor to queue if in-degree becomes 0
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if graph contains a cycle
    if len(sorted_vertices) != len(graph):
        raise ValueError("Graph contains a cycle and cannot be topologically sorted")

    return sorted_vertices

# Example usage
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }

    sorted_vertices = topological_sort(graph)
    print("Topologically sorted vertices:", sorted_vertices)