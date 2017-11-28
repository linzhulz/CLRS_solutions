# urs/bin/env python
# coding = utf-8
import random
import unittest

class TreeNode:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

    def printTree(node):
        while node is not None:
            print node.key
            printTree(node.left)
            printTree(node.right)

class ProblemTestCase(unittest.TestCase):
    def testCase(self):
        node = TreeNode(1, TreeNode(2), TreeNode(3))
        printTree(node)

if __name__ == '__main__':
    unittest.main()