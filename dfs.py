"""
Depth-First Search (DFS) Algorithm Implementation

This module provides both recursive and iterative implementations of DFS
for graph traversal.
"""

from typing import List, Set, Dict, Any
from collections import defaultdict


class Graph:
    """A simple graph class using adjacency list representation."""

    def __init__(self):
        """Initialize an empty graph."""
        self.graph = defaultdict(list)

    def add_edge(self, u: Any, v: Any, directed: bool = False):
        """
        Add an edge to the graph.

        Args:
            u: Source vertex
            v: Destination vertex
            directed: If False, adds edge in both directions (default: False)
        """
        self.graph[u].append(v)
        if not directed:
            self.graph[v].append(u)

    def dfs_recursive(self, start: Any, visited: Set[Any] = None) -> List[Any]:
        """
        Perform DFS traversal using recursion.

        Args:
            start: Starting vertex
            visited: Set of already visited vertices

        Returns:
            List of vertices in DFS order
        """
        if visited is None:
            visited = set()

        result = []

        def dfs_helper(vertex: Any):
            """Helper function for recursive DFS."""
            visited.add(vertex)
            result.append(vertex)

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(start)
        return result

    def dfs_iterative(self, start: Any) -> List[Any]:
        """
        Perform DFS traversal using iteration (stack-based).

        Args:
            start: Starting vertex

        Returns:
            List of vertices in DFS order
        """
        visited = set()
        stack = [start]
        result = []

        while stack:
            vertex = stack.pop()

            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)

                # Add neighbors to stack in reverse order to maintain
                # left-to-right traversal order
                for neighbor in reversed(self.graph[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return result

    def dfs_path(self, start: Any, goal: Any) -> List[Any]:
        """
        Find a path from start to goal using DFS.

        Args:
            start: Starting vertex
            goal: Goal vertex

        Returns:
            List representing path from start to goal, or empty list if no path exists
        """
        visited = set()
        stack = [(start, [start])]

        while stack:
            vertex, path = stack.pop()

            if vertex == goal:
                return path

            if vertex not in visited:
                visited.add(vertex)

                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor]))

        return []

    def is_connected(self, start: Any, goal: Any) -> bool:
        """
        Check if there's a path between start and goal vertices.

        Args:
            start: Starting vertex
            goal: Goal vertex

        Returns:
            True if path exists, False otherwise
        """
        visited = set()
        stack = [start]

        while stack:
            vertex = stack.pop()

            if vertex == goal:
                return True

            if vertex not in visited:
                visited.add(vertex)

                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        stack.append(neighbor)

        return False


def dfs_matrix(graph: List[List[int]], start: int) -> List[int]:
    """
    Perform DFS on an adjacency matrix representation.

    Args:
        graph: Adjacency matrix where graph[i][j] = 1 if edge exists
        start: Starting vertex index

    Returns:
        List of vertices in DFS order
    """
    n = len(graph)
    visited = [False] * n
    result = []

    def dfs_helper(vertex: int):
        """Helper function for recursive DFS on matrix."""
        visited[vertex] = True
        result.append(vertex)

        for neighbor in range(n):
            if graph[vertex][neighbor] == 1 and not visited[neighbor]:
                dfs_helper(neighbor)

    dfs_helper(start)
    return result


if __name__ == "__main__":
    # Example 1: Basic DFS traversal
    print("Example 1: Basic DFS Traversal")
    print("-" * 40)
    g1 = Graph()
    g1.add_edge(0, 1)
    g1.add_edge(0, 2)
    g1.add_edge(1, 3)
    g1.add_edge(1, 4)
    g1.add_edge(2, 5)
    g1.add_edge(2, 6)

    print(f"DFS Recursive from vertex 0: {g1.dfs_recursive(0)}")
    print(f"DFS Iterative from vertex 0: {g1.dfs_iterative(0)}")
    print()

    # Example 2: Finding a path
    print("Example 2: Finding Path")
    print("-" * 40)
    g2 = Graph()
    g2.add_edge('A', 'B')
    g2.add_edge('A', 'C')
    g2.add_edge('B', 'D')
    g2.add_edge('C', 'E')
    g2.add_edge('D', 'F')
    g2.add_edge('E', 'F')

    path = g2.dfs_path('A', 'F')
    print(f"Path from A to F: {' -> '.join(map(str, path))}")
    print(f"Is A connected to F? {g2.is_connected('A', 'F')}")
    print()

    # Example 3: Adjacency matrix
    print("Example 3: DFS on Adjacency Matrix")
    print("-" * 40)
    matrix = [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0]
    ]
    print(f"DFS from vertex 0: {dfs_matrix(matrix, 0)}")
    print()

    # Example 4: Directed graph
    print("Example 4: Directed Graph")
    print("-" * 40)
    g3 = Graph()
    g3.add_edge(1, 2, directed=True)
    g3.add_edge(1, 3, directed=True)
    g3.add_edge(2, 4, directed=True)
    g3.add_edge(3, 4, directed=True)
    g3.add_edge(4, 5, directed=True)

    print(f"DFS from vertex 1: {g3.dfs_iterative(1)}")
