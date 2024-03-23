# Hubert Jackowski
from Node import Node


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

    def getLeaf(self, value: int) -> Node or None:
        targetNode = None

        def _DFS(node: Node):
            nonlocal targetNode
            if node.value == value:
                targetNode = node
            if node.left is not None:
                _DFS(node.left)
            if node.right is not None:
                _DFS(node.right)

        _DFS(self.root)
        return targetNode

    def reroot(self, leaf: Node):
        if leaf.right is not None and leaf.left is not None:
            raise Exception("Too Many Children")

        currentNode = leaf
        parent = currentNode.parent
        while currentNode != self.root:
            grandParent = parent.parent

            if currentNode.left:
                currentNode.right = currentNode.left

            currentNode.left = parent
            parent.parent = currentNode
            if parent.left == currentNode:
                parent.left = None
            elif parent.right == currentNode:
                parent.right = None

            currentNode = parent
            parent = grandParent

        leaf.parent = None
        self.root = leaf

    @staticmethod
    def formList(lst: list[int]):
        def _buildTree(values, index=0, parent=None) -> Node:
            currentRoot = Node(values[index], parent)
            if 2 * index + 1 < len(values):
                currentRoot.left = _buildTree(values, 2 * index + 1, currentRoot)
            if 2 * index + 2 < len(values):
                currentRoot.right = _buildTree(values, 2 * index + 2, currentRoot)

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

        treeRoot = _buildTree(lst)
        _cutBlankBranches(treeRoot)
        return BinaryTree(treeRoot)

    @staticmethod
    def height(currentNode: Node):
        if currentNode.parent is None:
            return 0
        return BinaryTree.height(currentNode.parent) + 1

    def numberOfVertices(self) -> dict:
        numberOfVertices = dict()

        if self.root is None:
            numberOfVertices[0] = 0
            return numberOfVertices
        queue = [self.root]

        while len(queue) > 0:
            node = queue.pop(0)
            height = BinaryTree.height(node)
            try:
                numberOfVertices[height] += 1
            except KeyError:
                numberOfVertices[height] = 1
            # print(_height(node), node.value, " ")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return numberOfVertices

    def shortestPathToRoot(self):
        if self.root is None:
            return
        queue = [self.root]

        while len(queue) > 0:
            node = queue.pop(0)
            if node.left is None and node.right is None:
                return BinaryTree.height(node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    def getLeavesValueByHeight(self, height):
        leavesOnHeight = []
        if self.root is None:
            return
        queue = [self.root]

        while len(queue) > 0:
            node = queue.pop(0)
            if BinaryTree.height(node) == height:
                leavesOnHeight.append(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return leavesOnHeight
