# Hubert Jackowski
from __future__ import annotations


class Node:
    def __init__(self, value=None):
        self.value = value
        self.neighbours = []
        self.weights = []

    def addNeighbour(self, neighbour):
        if not (neighbour[0] in self.neighbours):
            self.neighbours.append(neighbour[0])
            self.weights.append(neighbour[1])

    def getValue(self) -> str:
        return self.value

    def getNeighbours(self) -> list[tuple[Node, int]]:
        return [(self.neighbours[i], self.weights[i]) for i in range(len(self.neighbours))]
