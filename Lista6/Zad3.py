# Hubert Jackowski
from Graph import Graph


G = Graph(["A", "B", "C", "D", "E", "F", "G", "H"])
print("-"*5, "Graph", "-"*5)
G.print()
G.draw()

print("-"*20, "Kruskal's Algorithm", "-"*20)
G.kruskal()

print("-"*20, "Prim's Algorithm", "-"*20)
G.prim()
