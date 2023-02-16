class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class L_list:
    def __init__(self) -> None:
        self.head = None

    def show(self):
        dat = self.head
        while dat != None:
            print(dat.data)
            dat = dat.next

    def binsert(self, val):
        New = Node(val)
        New.next = self.head
        self.head = New

    def eninsert(self, val):
        now = self.head
        if self.head == None:
            self.head = Node(val)

        while now.next:
            now = now.next
        now.next = Node(val)

    def inbt(self, mid, val):
        if mid.data == None:
            print("Node does not present")
            return
        new = Node(val)
        new.next = mid.next
        mid.next = new

    def RemoveNode(self, Removekey):
        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return None
        while (HeadVal):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return None

        prev.next = HeadVal.next
        HeadVal = None

    def rev(self):
        if (self.head == None or self.head.next == None):
            return
        pre = self.head
        curr = self.head.next
        while (curr):
            next = curr.next
            curr.next = pre
            # update
            pre = curr
            curr = next
        self.head.next = None
        self.head = pre


one = L_list()
one.head = Node(21)
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
one.head.next = e2

# Link second Node to third node
e2.next = e3
one.binsert(223)
one.inbt(e2, 456)
one.eninsert(22222)
one.RemoveNode(223)
one.show()
one.rev()
one.show()
