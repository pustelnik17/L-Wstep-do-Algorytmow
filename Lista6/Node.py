# Hubert Jackowski

class Node:
    def __init__(self, value=None):
        self.value = value
        self.neighbours = []

    def addNeighbours(self, *neighbours):
        for neighbour in neighbours:
            if not (neighbour in self.neighbours):
                self.neighbours.append(neighbour)

    def getValue(self) -> str:
        return self.value

    def getNeighbours(self) -> list:
        return self.neighbours
