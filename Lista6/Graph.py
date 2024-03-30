# Hubert Jackowski
from random import sample, randint
from networkx import DiGraph, draw_networkx_labels,draw_networkx_edge_labels, draw
from matplotlib.pyplot import show
from Node import Node
import networkx as nx


class Graph:
    def __init__(self, vertices: list[str]):
        self.RT = None
        self.G = [Node(vertex) for vertex in vertices]
        self.addRandomEdges()

    def addRandomEdges(self):
        for node in self.G:
            newNeighbours = sample(self.G, k=randint(0, (len(self.G) - 1) // 2))
            for neighbour in newNeighbours:
                randomNum = randint(0, 9)
                node.addNeighbour((neighbour, randomNum))
                neighbour.addNeighbour((node, randomNum))

    def getEdges(self) -> list[tuple[str, str, int]]:
        return [(node.getValue(), weight[0].getValue(), weight[1])
                for node in self.G for weight in node.getNeighbours()]

    def print(self):
        for node in self.G:
            print(node.getValue(), "->", end=" ")
            neighbours = node.getNeighbours()
            for n in neighbours:
                print(n[0].getValue(), ": ", n[1], sep="", end=" ")
            print()

    def draw(self):
        G = DiGraph()
        for origin, target, weight in self.getEdges():
            G.add_edge(origin, target, weight=weight, color="black")
        pos = nx.circular_layout(G)
        edge_labels = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])
        draw(G, pos, node_color="#000000", edge_color="#000000")
        draw_networkx_labels(G, pos, font_color="#ffffff")
        draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        show()
