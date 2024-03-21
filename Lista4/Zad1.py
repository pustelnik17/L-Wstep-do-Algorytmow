# Hubert Jackowski
import numpy

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []


class BinaryTree:
    def __init__(self, root=None):
        self.root = Node(root)

    @staticmethod
    def DFS(Node):
        print(Node.value, end=" ")
        for child in Node.children:
            BinaryTree.DFS(child)


def random():
    return numpy.random.randint(1, 10)


def testBFSandDFS():
    tree = BinaryTree(random())
    for i in range(3):
        tree.root.children.append(Node(random()))
        for i in range(3):
            tree.root.children.append(Node(random()))
            for i in range(2):
                tree.root.children.append(Node(random()))
    BinaryTree.DFS(tree.root)
testBFSandDFS()