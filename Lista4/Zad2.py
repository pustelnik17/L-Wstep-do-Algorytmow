# Hubert Jackowski
import BinaryTree


tree = BinaryTree.BinaryTree.formList([_ for _ in range(31)])
tree.print()
tree.reroot(tree.getLeaf(30))
tree.print()
