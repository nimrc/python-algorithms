"""
Undirected Graph
http://btechsmartclass.com/data_structures/graph-representations.html
"""
from typing import Dict, List


class UndirectedGraph:
    vert_count: int = 0
    edge_count: int = 0
    adj_matrix: Dict = {}

    def add_edge(self, src, dest):
        if src in self.adj_matrix:
            self.adj_matrix[src][dest] = 1
        else:
            self.adj_matrix[src] = {dest: 1}
            self.vert_count += 1

        if dest in self.adj_matrix:
            self.adj_matrix[dest][src] = 1
        else:
            self.adj_matrix[dest] = {src: 1}
            self.vert_count += 1

        self.edge_count += 1

    def adjacency(self, vertex) -> List:
        return list(self.adj_matrix[vertex].keys())

    def vertices(self) -> List:
        return list(self.adj_matrix.keys())

    def degree(self, vertex) -> int:
        return len(self.adj_matrix[vertex]) if vertex in self.adj_matrix else 0
