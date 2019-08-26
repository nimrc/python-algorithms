"""
Binary Tree
"""


class Leaf:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

    def __str__(self):
        return self.value


class BinaryTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return self.pre_order(self.root)

    def invert(self, node):
        if node is not None:
            node.left, node.right = node.right, node.left
            if node.left is not None:
                node.left = self.invert(node.left)
            if node.right is not None:
                node.right = self.invert(node.right)

        return node

    def pre_order(self, node):
        return node.value + self.pre_order(node.left) + self.pre_order(node.right) \
            if node is not None else ""

    def in_order(self, node):
        return self.in_order(node.left) + node.value + self.in_order(node.right) \
            if node is not None else ""

    def post_order(self, node):
        return self.post_order(node.left) + self.post_order(node.right) + node.value \
            if node is not None else ""
