# Hubert Jackowski
import BinaryTree


tree = BinaryTree.BinaryTree.formList([_ for _ in range(31)])
tree.print()
print("-"*20, "DFS", "-"*20)
tree.DFS()
print("-"*20, "BFS", "-"*20)
tree.BFS()
