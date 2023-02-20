class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class L_list:
    def __init__(self, size) -> None:
        self.head = None
        self.size = size

    def show(self):
        dat = self.head
        while dat != None:
            print(dat.data, end="->")
            dat = dat.next

        print(dat)

    def binsert(self, val):
        new = Node(val)
        dat = self.head
        i=0
        while dat:
            dat = dat.next
            i = i+1
        if i == self.size:
            print("list is full")
            return
        if self.head == None:
            self.head = new
        else:
            new.next = self.head
            self.head = new

    def eninsert(self, val):
        now = self.head
        i = 0
        dat = self.head
        while dat:
            dat = dat.next
            i = i+1
        if i == self.size:
            print("list is full")
            return
        if self.head == None:
            self.head = Node(val)

        while now.next:
            now = now.next
        now.next = Node(val)

    def inbt(self, key, val):
        new = Node(val)
        dat = self.head
        i=0
        while dat:
            dat = dat.next
            i = i+1
        if i == self.size:
            print("list is full")
            return
        temp = self.head
        temp1 = self.head
        j = 0
        while temp1:
            temp1 = temp1.next
            j += 1
        if key > j:
            print("index out of range")
            return
        for i in range(key-1):
            temp = temp.next
        new.next = temp.next
        temp.next = new

    def delete(self, key):
        temp = self.head
        temp1 = self.head
        j = 0
        while temp1:
            temp1 = temp1.next
            j += 1
        if key > j:
            print("index out of range")
            return
        if key == 0:
            self.head = temp.next
            temp.next = None
            return
        for i in range(key-1):
            temp = temp.next
        temp.next = temp.next.next

    def update(self, key, data):
        temp = self.head
        for i in range(key):
            temp = temp.next
        temp.data = data


one = L_list(2)
one.binsert(1)
one.inbt(1, 3)
one.inbt(2, 4)

one.show()
