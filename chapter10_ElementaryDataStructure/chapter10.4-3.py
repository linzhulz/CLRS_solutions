# urs/bin/env python
# coding = utf-8
import random
import unittest

class TreeNode:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def printTree2(node):
    stack = [node]
    while len(stack) > 0:
        node = stack[-1]
        del stack[-1]
        if node is not None:
            print node.key
            stack.append(node.right)
            stack.append(node.left)

class ProblemTestCase(unittest.TestCase):
    def TestCase(self):
        node = TreeNode(1, TreeNode(2), TreeNode(3))
        printTree2(node)

if __name__ == '__main__':
    unittest.main()