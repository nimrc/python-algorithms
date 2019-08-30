"""
Graph test case
"""
import unittest

from src.data_structures.graph.undirected_graph import UndirectedGraph


class TestGraph(unittest.TestCase):
    def test_undirected_graph(self):
        """
        A --  B
        | \  |  \
        C -- D -- E
        """
        graph = UndirectedGraph()
        vert_list = {
            'A': ['B', 'C', 'D'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'D'],
            'D': ['A', 'B', 'C', 'D', 'E'],
            'E': ['B', 'D'],
        }

        for src in vert_list:
            for dest in vert_list[src]:
                graph.add_edge(src, dest)

        self.assertEqual(graph.adjacency('A'), ['B', 'C', 'D'])
        self.assertEqual(graph.degree('A'), 3)
