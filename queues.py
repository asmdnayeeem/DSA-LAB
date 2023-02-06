class Queue:
    def __init__(self, n):
        self.items = []
        self.n = n
        self.i = 0

    def isEmpty(self):
        if self.items == []:
            return True
        return False

    def isFull(self):
        if self.i == self.n:
            return True
        return False

    def enque(self, ele):
        if self.isFull():
            print("Queue Overflow")
        else:
            self.i = self.i+1
            return self.items.append(ele)

    def deque(self):
        if self.isEmpty():
            print("Queue Underflow")
            return ("Queue Underflow")
        else:
            return self.items.pop(0)

    def show(self):
        return self.items


if __name__ == "__main__":
    new_queue = Queue(3)
    new_queue.enque(1)
    new_queue.enque(32)
    new_queue.enque(33)
    new_queue.deque()
    new_queue.enque(333)
    print(new_queue.show())
