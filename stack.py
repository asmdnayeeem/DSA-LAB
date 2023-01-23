class Stack:
    def __init__(self,n):
        self.items=[]
        self.n=n
    def isEmpty(self):
        if self.items==[]:
            return True
        return False
    def top(self):
        if self.isEmpty():
            return None
        print(self.items[-1])
    def push(self,ele):
        if len(self.items)==self.n:
            print("Stack is full")
        else:    
            self.items.append(ele)
    def size(self):
        print(len(self.items))
    def show(self):
        return (self.items)
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.items.pop()
if __name__=="__main__":
    n=int(input("Enter the size of stack:"))
    stack=Stack(n)
    while True:
        print("1.Push")
        print("2.Pop")
        print("3.isEmpty")
        print("4.Show")
        print("5.size")
        print("6.end")
        inp=int(input("Select the opearion:"))
        if inp==1:
            for i in range(n):
                x=input("Enter the element to push:")
                stack.push(x)
        if inp==2:
            stack.pop()
        if inp==3:
            print(stack.isEmpty())
        if inp==4:
            print(stack.show())
        if inp==5:
            stack.size()
        if inp==6:
            break
        if inp>6:
            print("invalid operation")

