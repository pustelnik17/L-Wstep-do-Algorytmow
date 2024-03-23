# Hubert Jackowski
import BinaryTree


tree = BinaryTree.BinaryTree.formList([_ for _ in range(31)])
print("-"*20, "TREE", "-"*20)
tree.print()
tree.reroot(tree.getLeaf(30))
print("-"*20, "NEW TREE", "-"*20)
tree.print()
