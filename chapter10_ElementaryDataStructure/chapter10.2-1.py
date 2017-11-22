#!/usr/bin/env python
# coding=utf-8

import random
import unittest

class Node:
    def __init__(self, value = None, next_node = None):
        self.value = value
        self.next_node = next_node

    def getData(self):
        return self.value

    def getNext(self):
        return self.next_node

    def setNext(self, new_next):
        self.next_node = new_next

class SingleLinkedList:
    def __init__(self, head = None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.setNext(self.head)
        self.head = new_node
        print self.head.getData()

    def search(self, data):
        current = self.head
        found = False
        while current and (found is False):
            if current.getData() == data:
                found = True
            else:
                current = current.getNext()
        if current is None:
            raise ValueError('Data is not in list')
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and (found is False):
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNext()
        if current is None:
            raise ValueError('Data is not in list')
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        return current.getData()

class ProblemTestCase(unittest.TestCase):
    def test_case(self):
        l = SingleLinkedList(None)
        l.insert(1)
        self.assertEqual(l.head.getData(), 1)

if __name__ == '__main__':
    unittest.main()