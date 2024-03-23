# Hubert Jackowski
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def print(self):
        def _print(node: Node, indents: int):
            print(node.value, sep="")
            if node.left is not None:
                print("   " * indents, "├─ ", sep="", end="") if node.right is not None else print("   " * indents,
                                                                                                   "└─ ", sep="",
                                                                                                   end="")
                _print(node.left, indents + 1)
            if node.right is not None:
                print("   " * indents, "└─ ", sep="", end="")
                _print(node.right, indents + 1)

        _print(self.root, 0)

    def DFS(self):
        def _DFS(node: Node):
            print(node.value, " ", end="", sep="")
            if node.left is not None:
                _DFS(node.left)
            if node.right is not None:
                _DFS(node.right)

        _DFS(self.root)
        print()

    def BFS(self):
        if self.root is None:
            return
        queue = [self.root]

        while len(queue) > 0:
            node = queue.pop(0)
            print(node.value, " ", end="", sep="")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        print()


def formList(lst) -> BinaryTree:
    def _buildTree(values, index) -> Node:
        currentRoot = Node(values[index])
        if 2 * index + 1 < len(values):
            currentRoot.left = _buildTree(values, 2 * index + 1)
        if 2 * index + 2 < len(values):
            currentRoot.right = _buildTree(values, 2 * index + 2)

        return currentRoot

    def _cutBlankBranches(node: Node):
        if node.left is not None:
            if node.left.value is None:
                node.left = None
            else:
                _cutBlankBranches(node.left)

        if node.right is not None:
            if node.right.value is None:
                node.right = None
            else:
                _cutBlankBranches(node.right)

    treeRoot = _buildTree(lst, 0)
    _cutBlankBranches(treeRoot)
    return BinaryTree(treeRoot)
