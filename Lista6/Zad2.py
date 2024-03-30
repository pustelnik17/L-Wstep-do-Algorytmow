# Hubert Jackowski
from Graph import Graph

print("-"*20, "Dijkstra's Algorithm", "-"*20)
G = Graph(["A", "B", "C", "D", "E", "F", "G", "H"])
print("-"*5, "Graph", "-"*5)
G.print()
G.dijkstra()
G.draw()
