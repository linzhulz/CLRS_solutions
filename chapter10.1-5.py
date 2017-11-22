class Deque:
    def __init__(self, size):
        self.size = size
        self.q = [0] * size
        self.head = -1
        self.tail = 0

    def is_empty(self):
        if self.head == -1 and self.tail == 0:
        return True

    def one_element(self):
        if self.head == 0 and self.tail == 0:

    def frontAdd(self, x):
        if (self.head - 1) % self.size == self.tail:
            raise Exception('overflow')
        if is_empty():
            self.head = 0
            self.q[self.head] = x
        else:
            self.head = (self.head - 1) % self.size
            self.q[self.head] = x

    def endAdd(self, x):
        if (self.tail + 1) % self.size == self.head:
            raise Exception('overflow')
        if is_empty():
            self.q[self.tail] = x
            self.head = 0
        else:
            self.tail = (self.tail + 1) % self.size
            self.q[self.tail] = x

    def frontDelete(self):
        if is_empty():
            raise Exception('underflow')
        if self.head % self.size == self.tail:
            if self.head == 0 and self.tail == 0:
                x = self.q[self.head]
                self.head = -1
            else:
                raise Exception('underflow')
        x = self.q[self.head]
        self.head = (self.head - 1) % self.size
        return x

    def endDelete(self):
        if is_empty():
            raise Exception('underflow')
        if self.tail % self.size == self.tail:
            if self.tail == 0 and self.head == 0:
                x = self.q[self.tail]
            else:
                raise Exception('underflow')
        x = self.q[self.tail]
        self.tail = (self.tail + 1) % self.size
        return x