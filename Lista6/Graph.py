# Hubert Jackowski
from random import sample, randint
from networkx import DiGraph, spring_layout, draw_networkx_nodes, draw_networkx_labels, draw_networkx_edges
from matplotlib.pyplot import show
from Node import Node


class Graph:
    def __init__(self, vertices: list[str]):
        self.RT = None
        self.G = [Node(vertex) for vertex in vertices]
        self.addRandomEdges()

    def addRandomEdges(self):
        for node in self.G:
            newNeighbours = sample(self.G, k=randint(0, (len(self.G) - 1) // 2))
            node.addNeighbours(*newNeighbours)
            for neighbour in newNeighbours:
                neighbour.addNeighbours(node)

    def getEdges(self) -> list[tuple]:
        return [(node.getValue(), neighbour.getValue()) for node in self.G for neighbour in node.getNeighbours()]

    def print(self):
        for node in self.G:
            print(node.getValue(), "->", end=" ")
            neighbours = node.getNeighbours()
            for n in neighbours:
                print(n.getValue(), end=" ")
            print()

    def draw(self):
        G = DiGraph()
        G.add_edges_from(self.getEdges())

        pos = spring_layout(G)

        draw_networkx_nodes(G, pos, node_color="#000000")
        draw_networkx_labels(G, pos, font_color="#ffffff")
        draw_networkx_edges(G, pos, edge_color='#000000', arrows=True)

        show()
