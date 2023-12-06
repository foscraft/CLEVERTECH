#### 1.  Problem Description:

You are tasked with creating a Python script that analyzes log files from a server and extracts meaningful information. The log files are in a custom format, and each entry in the log file represents an event on the server.

The log entries have the following format:

```css

[timestamp] [severity] [source] [message]
```

timestamp: The time when the event occurred, formatted as YYYY-MM-DD HH:MM:SS.

severity: The severity level of the event (INFO, WARNING, ERROR).

source: The source module or component where the event originated.

message: The detailed message describing the event.

Your task is to write a Python script that can perform the following tasks:

Parse Log File:
Read a log file (provided as input) and parse each log entry into a structured format.

Filter by Severity:
Allow the user to filter log entries based on severity (INFO, WARNING, ERROR).

Count Events:
Provide a count of events for each source.

Error Analysis:
Identify and display the top 5 error messages (entries with ERROR severity).

Time Range Analysis:
Allow the user to specify a time range and display events within that range.

Please make sure to handle edge cases gracefully and provide clear instructions on how to run your script. Additionally, include a sample log file for testing purposes.

Note to the Candidate:
You are encouraged to use any standard Python libraries to accomplish this task.
    Pay attention to code readability, maintainability, and efficiency.
    Provide comments and docstrings where necessary.
    The goal is to create a solution that is not only correct but also well-organized and easy to understand.

This problem covers aspects of file I/O, string parsing, data manipulation, and user interaction. It assesses the candidate's ability to design a solution for a real-world problem and implement it using Python.


#### 2. Problem Title: Finding Common Elements in Two Arrays

Problem Description:

You are given two arrays of integers, arr1 and arr2. Write a Python function that finds and returns an array containing the common elements between the two arrays. The order of elements in the resulting array should be the same as they appear in the first array (arr1).


#### 3. Problem Title: Shortest Path in a Weighted Graph

Problem Description:

You are given a directed graph with weighted edges, represented as an adjacency matrix. Each edge has a non-negative weight, and the graph may contain cycles. Write a Python function that finds the shortest path from a given source node to a destination node. If no path exists, return None.

Write a function with the following signature:

```python

def shortest_path(graph, source, destination):
    # Your code here
    pass
```

Input:

graph: A square 2D list representing the adjacency matrix of the graph. graph[i][j] is the weight of the edge from node i to node j. If there is no edge, the value is set to float('inf').

source: The source node (0-based index).
destination: The destination node (0-based index).

Output:

If a path exists, return a list of nodes representing the shortest path from the source to the destination.
If no path exists, return None.

Example:

```python

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
```

Expected Output:

```
[0, 3, 4]
```

Note:

The graph is represented as an adjacency matrix where float('inf') indicates no direct edge between nodes.
You need to find the shortest path from the source node to the destination node using an appropriate algorithm (e.g., Dijkstra's algorithm or Bellman-Ford algorithm).
    Consider edge cases, such as negative weights and the absence of a path between nodes.