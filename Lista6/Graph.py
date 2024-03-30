# Hubert Jackowski
from __future__ import annotations

from random import sample, randint
from networkx import DiGraph, draw_networkx_labels, draw_networkx_edge_labels, draw, circular_layout
from matplotlib.pyplot import show
from Node import Node


class Graph:
    def __init__(self, vertices: list[str], connections: list[tuple[str, str, int]] = None):
        self.weightUpper = 9
        self.weightLower = 0
        self.vertices = vertices
        self.G = [Node(vertex) for vertex in vertices]
        self.addRandomEdges((len(self.G) - 1) // 3) if connections is None else self.addEdges(connections)

    def getConnectedSubGraphs(self) -> list[Graph]:
        def _deepFirstSearch(currentNode: Node):
            nonlocal visitedNodesInner

            if currentNode in visitedNodesInner:
                return
            visitedNodesInner.append(currentNode)

            for neighbour in currentNode.getNeighbours():
                _deepFirstSearch(neighbour[0])

        connectedSubGraphs: list[Graph] = []
        visitedNodesOuter: list[Node] = []

        edges = self.getEdges()

        for node in self.G:
            if node not in visitedNodesOuter:
                visitedNodesOuter.append(node)
                visitedNodesInner:  list[Node] = []
                _deepFirstSearch(node)
                visitedNodesInnerValue = [currentNode.getValue() for currentNode in visitedNodesInner]

                G = Graph(visitedNodesInnerValue, [])
                G.addEdges([(origin, target, weight) for origin, target, weight in edges
                            if (origin in visitedNodesInnerValue) and (target in visitedNodesInnerValue)])
                connectedSubGraphs.append(G)
                visitedNodesOuter.extend(x for x in visitedNodesInner if x not in visitedNodesOuter)

        return connectedSubGraphs

    def getNode(self, value: str) -> Node | None:
        for node in self.G:
            if node.getValue() == value:
                return node
        return None

    def addEdges(self, connections: list[tuple[str, str, int]]):
        for origin, target, weight in connections:
            try:
                self.getNode(origin).addNeighbour((self.getNode(target), weight))
                self.getNode(target).addNeighbour((self.getNode(origin), weight))
            except AttributeError:
                raise Exception(f"One of provided nodes does not exist {origin} {target}")

    def addRandomEdges(self, edgeUpper):
        for node in self.G:
            newNeighbours = sample(self.G, k=randint(0, edgeUpper))
            for neighbour in newNeighbours:
                weight = randint(self.weightLower, self.weightUpper)
                node.addNeighbour((neighbour, weight))
                neighbour.addNeighbour((node, weight))

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
        for node in self.G:
            G.add_node(node.getValue())
        for origin, target, weight in self.getEdges():
            G.add_edge(origin, target, weight=weight, color="black")
        pos = circular_layout(G)
        edge_labels = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])
        draw(G, pos, node_color="#000000", edge_color="#000000")
        draw_networkx_labels(G, pos, font_color="#ffffff")
        draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        show()
