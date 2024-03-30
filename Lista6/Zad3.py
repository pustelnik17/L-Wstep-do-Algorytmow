# Hubert Jackowski
from Graph import Graph

print("-"*20, "Kruskal's Algorithm", "-"*20)
G = Graph(["A", "B", "C", "D", "E", "F", "G", "H"])
print("-"*5, "Graph", "-"*5)
G.print()
G.draw()
G.kruskal()
