class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node

    def getData(self):
        return self.data

    def getNext(self):
        return self.next_node

    def setNext(self, new_node):
        self.next_node = new_node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.head.setNext(new_node)
            self.head = new_node
#         print 'head after enqueue', self.head.getData()
#         print 'tail after enqueue', self.tail.getData()
#         print '##'

    def dequeue(self):
        if self.tail is None and self.head is None:
            raise Exception('underflow')
        data = self.tail.getData()
        next = self.tail.getNext()
        if next is None:
            self.head = None
        self.tail = next
#         print 'head after dequeue', self.head.getData()
#         print 'tail after dequeue', self.tail.getData()
#         print 'dequeue', data
#         print '##'
        return data
