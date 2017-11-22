#!/urs/bin/env python
# coding=utf-8

class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node

    def getData(self):
        return self.data

    def getNext(self):
        return self.next_node

    def setNext(self, new_next):
        self.next_node = new_next

class Stack:
    def __init__(self, head = None):
        self.head = head

    def push(self, data):
        new_node = Node(data)
        new_node.setNext(self.head)
        self.head = new_node

    def pop(self):
        if self.head is None:
            raise Exception('underflow')
        new_head = self.head.getNext()
        data = self.head.getData()
        self.head = new_head
        return data



