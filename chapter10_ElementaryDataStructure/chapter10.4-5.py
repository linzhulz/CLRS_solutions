# urs/bin/env python
# coding = utf-8
import random
import unittest

class TreeNode:
    def __init__(self, key, parent = None, left_child = None, right_sibling = None):
        self.key = key
        self.parent = parent
        self.left_child = left_child
        self.right_sibling = right_sibling

def printTree(node):
    if node is not None:
        while node.parent is not None:
            node = node.parent
        while node is not None:
            print node.key
            sibling = node.right_sibling
            while sibling is not None:
                print sibling.key
                sibling = sibling.right_sibling
            node = node.left_child
