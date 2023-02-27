class Node:
    def __init__(self, value, pr):
        self.data = value
        self.pri = pr
        self.next = None


class priQueue:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return True if self.head == None else False

    def push(self, value, pri):
        if self.isEmpty() == True:
            self.head = Node(value, pri)
            return 1
        else:
            if self.head.pri > pri:
                newNode = Node(value, pri)
                newNode.next = self.head
                self.head = newNode
                return 1
            else:
                temp = self.head
                while temp.next:
                    if pri <= temp.next.pri:
                        break
                    temp = temp.next
                newNode = Node(value, pri)
                newNode.next = temp.next
                temp.next = newNode

                return 1

    def pop(self):
        if self.isEmpty() == True:
            return
        else:
            self.head = self.head.next
            return 1

    def top(self):

        if self.isEmpty() == True:
            print("Queue is Empty!")
        else:
            print(self.head.data, "\n")

    def traverse(self):

        if self.isEmpty() == True:
            print( "Queue is Empty!")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()


if __name__ == "__main__":

    pq = priQueue()
    pq.push(8, 1)
    pq.push(3, 4)
    pq.push(1, 2)
    pq.push(5, 0)

    pq.traverse()

    pq.pop()
    pq.traverse()
    pq.top()
