# Hubert Jackowski
import BinaryTree

print("-"*20, "TREE", "-"*20)
tree = BinaryTree.BinaryTree.formList([0, 1, 2, None, 4, 5, 6, None, None, 9, 10, 11, 12, 13, 14, None, None, None,
                                       None, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
tree.print()
print("-"*20, "Number Of Vertices", "-"*20)
print(tree.numberOfVertices())
print("-"*20, "Shortest Path To Root", "-"*20)
print(tree.shortestPathToRoot())
print("-"*20, "Get Leaves Value By Height", "-"*20)
print(tree.getLeavesValueByHeight(tree.shortestPathToRoot()))
