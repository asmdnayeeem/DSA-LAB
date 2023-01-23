class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        if self.items==[]:
            return True
        return False
    def peek(self):
        if self.isEmpty():
            return None
        print(self.items[-1])
    def push(self,ele):
        self.items.append(ele)
    def size(self):
        print(len(self.items))
    def show(self):
        print(self.items)
    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

stack=Stack()
stack.push(4)
stack.push(2)
stack.push(1)
stack.push(5)
stack.show()
stack.size()
stack.peek()     
stack.pop()
stack.show()
stack.size()
stack.peek()     