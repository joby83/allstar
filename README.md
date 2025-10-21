allstar
=======

superjam

## Depth-First Search (DFS) Algorithm

This repository contains comprehensive implementations of the Depth-First Search algorithm.

### Features

- **Multiple DFS Implementations:**
  - Recursive DFS
  - Iterative DFS (stack-based)
  - Path finding using DFS
  - Connectivity checking
  - Support for both adjacency list and adjacency matrix representations

- **Flexible Graph Representation:**
  - Undirected and directed graphs
  - Support for any hashable vertex type (integers, strings, etc.)

### Usage

#### Basic DFS Traversal

```python
from dfs import Graph

# Create a graph
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)

# Perform DFS traversal
print(g.dfs_recursive(0))  # Recursive approach
print(g.dfs_iterative(0))  # Iterative approach
```

#### Finding a Path

```python
from dfs import Graph

g = Graph()
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'D')

path = g.dfs_path('A', 'D')
print(f"Path from A to D: {path}")
```

#### Checking Connectivity

```python
from dfs import Graph

g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)

is_connected = g.is_connected(1, 3)
print(f"1 and 3 are connected: {is_connected}")
```

### Running Examples

Execute the main file to see various DFS examples:

```bash
python dfs.py
```

### Running Tests

Run the test suite using pytest:

```bash
pytest test_dfs.py -v
```

### Algorithm Complexity

- **Time Complexity:** O(V + E) where V is the number of vertices and E is the number of edges
- **Space Complexity:** O(V) for the visited set and recursion stack/iteration stack

### Applications of DFS

- Finding connected components
- Topological sorting
- Cycle detection
- Path finding
- Maze solving
- Tree and graph traversals
