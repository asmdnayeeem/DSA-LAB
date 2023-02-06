class Queue:
    def __init__(self, n):
        self.items = []
        self.front = -1
        self.n = n
        self.rear = -1

    def isEmpty(self):
        if (self.front == -1 and self.rear == -1):
            return True
        return False

    def isFull(self):
        if self.rear == self.n-1:
            return True
        return False

    def isSingle(self):
        if self.front == self.rear:
            return True
        return False

    def enque(self, ele):
        if self.isFull():
            print("Stack Overflow")
        elif self.isEmpty():
            self.front = self.front+1
            self.rear = self.rear+1
            self.items.insert(self.rear, ele)
        else:
            self.rear = self.rear+1
            self.items.insert(self.rear, ele)

    def deque(self):
        if self.isEmpty():
            print("Q underflow")
        else:
            self.items.pop(0)
          

            self.front = self.front+1

    def show(self):
        return self.items


if __name__ == "__main__":
    n = int(input("Enter the size of Queue:"))
    neq = Queue(n)

    while True:
        inp = int(input(
            "Chose the opration\n1.Enque\n2.Deque\n3.Show\n4.Quit the operation Mode\n"))
        if inp == 1:
            y = input("Enter the no of elements to insert:")
            for i in range(int(y)):
                x = input("Enter the Element:")
                neq.enque(x)
        elif inp == 2:
            neq.deque()
        elif inp == 3:
            print(neq.show())
        elif inp == 4:
            break
        else:
            print("Invalid operation")
