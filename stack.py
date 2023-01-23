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
        self.items.pop()

stack=Stack()
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)
stack.push(8)
stack.show()        
stack.peek()
stack.pop()
stack.show()
stack.peek()
stack.size() 
newstack=Stack()
newstack.push(2)
newstack.show()       