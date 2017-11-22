#!/usr/bin/env python
# coding=utf-8

class Queue:
    def __init__(self, size):
        self.q = [0 for _ in xrange(size)]
        self.head = 0
        self.tail = 0
        self.size = size

    def enqueue(self, x):
        if (self.tail + 1) % self.size == self.head:
            raise Exception('overflow')
        self.q[self.tail] = x
        # print 'q.tail before enqueue', q.tail
        self.tail += 1
        if self.tail == self.size:
            self.tail = 0
        # print 'q.tail after enqueue', q.tail
        # print '###'

    def dequeue(self):
        if self.head == self.tail:
            raise Exception('underflow')
        x = self.q[self.head]
        # print 'q.head before dequeue', q.head
        self.head += 1
        if self.head == self.size:
            self.head = 0
        # print 'q.head after dequeue', q.head
        # print '###'
        return x


class Stack:
    def __init__(self, size):
        self.s = [-1 for _ in xrange(size)]
        self.top = -1
        self.size = size

    def push(self, x):
        if self.top + 1 == self.size:
            raise Exception('overflow')
        # print 'top before push', self.top
        self.top += 1
        self.s[self.top] = x
        # print 'top after push', self.top

    def pop(self):
        if self.top == 0:
            raise Exception('underflow')
        # print 'top before pop', self.top
        x = self.s[self.top]
        self.top -= 1
        # print 'top after pop', self.top
        # return x

        






