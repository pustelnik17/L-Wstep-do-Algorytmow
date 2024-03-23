# Hubert Jackowski
import BinaryTree


tree = BinaryTree.formList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
tree.print()
print("-"*20, "DFS", "-"*20)
tree.DFS()
print("-"*20, "BFS", "-"*20)
tree.BFS()
