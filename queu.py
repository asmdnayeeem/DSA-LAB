class queue:
    def __init__(self, n) -> None:
        self.first = -1
        self.items = [None for i in range(n)]
        self.last = -1
        self.n = n

    def isEmpty(self):
        if (self.first == -1 and self.last == -1) or (self.first == self.n and self.last == self.n-1):
            return True
        return False

    def isFull(self):
        if self.last == self.n-1:
            return True
        return False

    def enque(self, val):
        if self.isEmpty():
            self.first += 1
        if self.isFull():
            print("overflow")
        else:
            self.last += 1
            self.items[self.last] = val

    def deque(self):
        if self.isEmpty():
            return print("underflow")
        self.first += 1
        self.items = self.items[self.first-1:self.last]
        return self.items

    def show(self):
        print(self.items)


if __name__ == "__main__":
    new = queue(3)
    new.enque(1)
    new.enque(2)
    new.enque(2)
    new.enque(2)
    new.show()
    new.deque()
    new.show()
    new.deque()
    new.show()
    new.deque()
    new.deque()
    new.deque()
    new.show()
