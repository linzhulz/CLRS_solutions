#!/usr/bin/env python
# coding=utf-8

class Queue:
    def __init__(self, size):
        self.q = [0 for _ in xrange(size)]
        self.head = 0
        self.tail = 0

    def enqueue(self, x):
        if (self.tail + 1) % len(self.q) == self.head:
            raise Exception('overflow')
        self.q[self.tail] = x
        print 'q.tail before enqueue', q.tail
        self.tail += 1
        if self.tail == len(self.q):
            self.tail = 0
        print 'q.tail after enqueue', q.tail
        print '###'

    def dequeue(self):
        if self.head == self.tail:
            raise Exception('underflow')
        x = self.q[self.head]
        print 'q.head before dequeue', q.head
        self.head += 1
        if self.head == len(self.q):
            self.head = 0
        print 'q.head after dequeue', q.head
        print '###'
        return x

def Stack:
    def __init__(self, size):
        self.s = [-1 for _ in xrange(size)]
        self.top = 0

    def push(self, x):
        if self.top == (len(self.s) - 1):
            raise Exception('overflow')
        






