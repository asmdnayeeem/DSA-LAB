class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class DList:
    def __init__(self, size):
        self.head = None
        self.size = size
        self.n = 0

    def sizel(self):
        dat = self.head
        while dat != None:
            dat = dat.right
            self.n += 1
        return self.n

    def isFull(self):
        self.sizel()
        if self.n == self.size-1:
            return True
        else:
            return False

    def show(self):
        dat = self.head
        while dat != None:
            print(dat.data, end=" <-> ")
            dat = dat.right
        print(dat)

    def binsert(self, val):
        new = Node(val)
        if self.head == None:
            self.head = new
        else:
            new.right = self.head
            self.head.left = new
            self.head = new

    def eninsert(self, val):
        new = Node(val)
        head = self.head
        while head.right != None:
            head = head.right
        head.right = new
        new.left = head

    def insert(self, mid, val):
        new = Node(val)
        if mid > self.size-1:
            print("List is Full")
            return
        if self.isFull():
            print("List is Full")
            return

        if mid == 0:
            self.binsert(val)
            return
        self.n = 0
        dat = self.head
        while dat != None:
            dat = dat.right
            self.n += 1
        if mid == self.n:
            self.eninsert(val)
            return
        temp = self.head
        i = 0
        while i != mid-1:
            temp = temp.right
            i += 1
        new.left = temp
        new.right = temp.right
        temp.right = new

    def delete(self, key):
        if key == 0:
            temp = self.head
            self.head = temp.right
            temp.right = None
            return
        dat = self.head
        i = 0
        while dat.right != None:
            dat = dat.right
            i = i+1
        if key > i:
            print("Key out of range")
            return
        if key == i:
            dat.left.right = None
            return
        temp = self.head
        for i in range(key):
            temp = temp.right
        temp.left.right = temp.right
        temp.right.left = temp.left

    def update(self, key, data):
        dat = self.head
        j = 0
        while dat.right != None:
            dat = dat.right
            j = j+1
        if key > j:
            print("Update Key out of range")
            return
        temp = self.head
        for i in range(key):
            temp = temp.right
        temp.data = data


if __name__ == "__main__":
    new = DList(6)
    new.binsert(1)
    new.insert(1, 2)
    new.show()
    new.insert(0, 3)
    new.show()
    new.eninsert(10)
    new.show()
    new.insert(1, 5)
    new.insert(5, 5)
    new.show()
    new.delete(0)
    new.delete(4)
    new.show()
    new.delete(6)
    new.update(10, 10)
    new.show()
