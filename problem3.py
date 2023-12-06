import heapq

def shortest_path(graph, source, destination):
    # Number of nodes in the graph
    num_nodes = len(graph)
    # Initialize distance and visited arrays
    distances = [float('inf')] * num_nodes
    distances[source] = 0
    visited = [False] * num_nodes
    # Priority queue to store (distance, node) pairs
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        # Skip if already visited
        if visited[current_node]:
            continue

        visited[current_node] = True
        # Update distances for adjacent nodes
        for neighbor, weight in enumerate(graph[current_node]):
            if not visited[neighbor]:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))

    # Reconstruct the path from source to destination
    path = []
    current_node = destination

    while current_node != source:
        path.insert(0, current_node)
        current_node = min((node for node in range(num_nodes) if graph[node][current_node] != float('inf') and distances[node] == distances[current_node] - graph[node][current_node]), default=None)

        if current_node is None:
            return None  # No path exists

    path.insert(0, source)
    return path

# Example Usage:
graph = [
    [0, 2, 4, 1, float('inf')],
    [float('inf'), 0, float('inf'), 3, float('inf')],
    [float('inf'), float('inf'), 0, float('inf'), 5],
    [float('inf'), float('inf'), float('inf'), 0, 2],
    [float('inf'), float('inf'), float('inf'), float('inf'), 0]
]

source = 0
destination = 4
result = shortest_path(graph, source, destination)
print(result)
