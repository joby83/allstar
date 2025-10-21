"""
Unit tests for DFS algorithm implementations.
"""

import pytest
from dfs import Graph, dfs_matrix


class TestGraph:
    """Test cases for the Graph class and DFS methods."""

    def test_add_edge_undirected(self):
        """Test adding undirected edges."""
        g = Graph()
        g.add_edge(1, 2)
        assert 2 in g.graph[1]
        assert 1 in g.graph[2]

    def test_add_edge_directed(self):
        """Test adding directed edges."""
        g = Graph()
        g.add_edge(1, 2, directed=True)
        assert 2 in g.graph[1]
        assert 1 not in g.graph[2]

    def test_dfs_recursive_simple(self):
        """Test recursive DFS on a simple graph."""
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 4)

        result = g.dfs_recursive(1)
        assert len(result) == 4
        assert result[0] == 1
        assert all(v in result for v in [1, 2, 3, 4])

    def test_dfs_iterative_simple(self):
        """Test iterative DFS on a simple graph."""
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 4)

        result = g.dfs_iterative(1)
        assert len(result) == 4
        assert result[0] == 1
        assert all(v in result for v in [1, 2, 3, 4])

    def test_dfs_recursive_vs_iterative(self):
        """Test that both DFS methods visit all vertices."""
        g = Graph()
        edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)]
        for u, v in edges:
            g.add_edge(u, v)

        rec_result = g.dfs_recursive(0)
        iter_result = g.dfs_iterative(0)

        assert len(rec_result) == len(iter_result)
        assert set(rec_result) == set(iter_result)

    def test_dfs_path_exists(self):
        """Test finding a path when one exists."""
        g = Graph()
        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'D')

        path = g.dfs_path('A', 'D')
        assert len(path) > 0
        assert path[0] == 'A'
        assert path[-1] == 'D'

    def test_dfs_path_not_exists(self):
        """Test finding a path when none exists."""
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(3, 4)

        path = g.dfs_path(1, 4)
        assert path == []

    def test_is_connected_true(self):
        """Test connectivity check when vertices are connected."""
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 4)

        assert g.is_connected(1, 4) is True

    def test_is_connected_false(self):
        """Test connectivity check when vertices are not connected."""
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(3, 4)

        assert g.is_connected(1, 3) is False

    def test_dfs_single_vertex(self):
        """Test DFS on a graph with a single vertex."""
        g = Graph()
        g.graph[1] = []  # Single vertex with no edges

        result = g.dfs_recursive(1)
        assert result == [1]

    def test_dfs_with_cycle(self):
        """Test DFS on a graph with cycles."""
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 1)  # Creates a cycle

        result = g.dfs_iterative(1)
        assert len(result) == 3
        assert len(set(result)) == 3  # No duplicates

    def test_dfs_string_vertices(self):
        """Test DFS with string vertices."""
        g = Graph()
        g.add_edge('start', 'middle')
        g.add_edge('middle', 'end')

        result = g.dfs_recursive('start')
        assert result == ['start', 'middle', 'end']


class TestDFSMatrix:
    """Test cases for adjacency matrix DFS."""

    def test_dfs_matrix_simple(self):
        """Test DFS on a simple adjacency matrix."""
        matrix = [
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 1, 0]
        ]
        result = dfs_matrix(matrix, 0)
        assert len(result) == 4
        assert result[0] == 0

    def test_dfs_matrix_disconnected(self):
        """Test DFS on a disconnected graph."""
        matrix = [
            [0, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
        ]
        result = dfs_matrix(matrix, 0)
        assert len(result) == 2  # Only visits connected component
        assert 0 in result and 1 in result
        assert 2 not in result and 3 not in result

    def test_dfs_matrix_single_vertex(self):
        """Test DFS on a single vertex."""
        matrix = [[0]]
        result = dfs_matrix(matrix, 0)
        assert result == [0]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
