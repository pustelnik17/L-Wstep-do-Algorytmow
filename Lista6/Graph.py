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
                visitedNodesInner: list[Node] = []
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

    def dijkstra(self):
        def _sortTupleList(tupleList):
            lst = len(tupleList)
            for i in range(0, lst):

                for j in range(0, lst - i - 1):
                    if tupleList[j][1] > tupleList[j + 1][1]:
                        temp = tupleList[j]
                        tupleList[j] = tupleList[j + 1]
                        tupleList[j + 1] = temp
            return tupleList

        def _dijkstra(current, previous):
            nonlocal distance, visitedNodes

            if current in visitedNodes:
                return

            visitedNodes.append(current)
            neighbours = current.getNeighbours()

            for neighbour, weight in neighbours:
                if weight + previous < distance[neighbour.getValue()]:
                    distance[neighbour.getValue()] = weight + previous

            for neighbour, weight in _sortTupleList(neighbours):
                _dijkstra(neighbour, distance[current.getValue()] + weight)

        for subGraph in self.getConnectedSubGraphs():
            print("-" * 5, "Sub Graph", "-" * 5)
            for node in subGraph.G:
                visitedNodes = []
                distance: dict[str | None, int] = {vertex: 10000 for vertex in subGraph.vertices}
                distance[node.getValue()] = 0
                _dijkstra(node, 0)
                print(node.getValue(), "->", distance)

    def kruskal(self):
        def _find(currentOrigin: Node, currentTarget: Node) -> bool:
            visitedNodes = set()
            queue = [currentOrigin]

            while len(queue) > 0:
                node = queue.pop(0)
                if node == currentTarget:
                    return True
                if node not in visitedNodes:
                    visitedNodes.add(node)
                    for neighbour, neighbourWeight in node.getNeighbours():
                        queue.append(neighbour)

            return False

        for subGraph in self.getConnectedSubGraphs():
            G = Graph(subGraph.vertices, [])
            edges = subGraph.getEdges()
            edges.sort(key=lambda x: x[2])

            for origin, target, weight in edges:
                if not _find(G.getNode(origin), G.getNode(target)):
                    G.addEdges([(origin, target, weight)])
            G.draw()

    def prim(self):
        def _prim(graph: Graph, node: Node):
            nonlocal visitedNodeValues, edges
            visitedNodeValues.append(node)
            for edge in [(node.getValue(), neighbour.getValue(), weight)
                         for neighbour, weight in node.getNeighbours()]:
                edges.append(edge)
                edges.sort(key=lambda x: x[2])

            while len(edges) > 0:
                nextEdge = edges.pop(0)
                nextNode = self.getNode(nextEdge[1])
                if nextNode not in visitedNodeValues:
                    graph.addEdges([nextEdge])
                    _prim(graph, nextNode)
                    break

        for subGraph in self.getConnectedSubGraphs():
            G = Graph(subGraph.vertices, [])
            visitedNodeValues: list[Node] = [self.getNode(G.vertices[0])]
            edges: list[tuple[str, str, int]] = []
            _prim(G, self.getNode(G.vertices[0]))
            G.draw()

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
