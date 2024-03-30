# Hubert Jackowski
from Graph import Graph

print("-"*20, "Decompose Graph Into Connected Sub Graphs", "-"*20)
G = Graph(["A", "B", "C", "D", "E", "F", "G", "H"])
print("-"*5, "Graph", "-"*5)
G.print()
G.draw()

for graph in G.getConnectedSubGraphs():
    print("-"*5, "Sub Graph", "-"*5)
    graph.print()
    graph.draw()
