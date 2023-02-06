class F_que:
    def __init__(self,n) -> None:
        self.n=n
        self.items=[]
    def isEmpty(self):
        if self.items==[]:
            return True
        return False
    def isFull(self):
        if self.items.__len__==self.n:
            return True
        return False
    def enque(self,ele):
        if self.isFull():
            self.items.pop(0)
            self.items.append(ele)
        else :
            self.items.append(ele)
    def deque(self):
        if self.isEmpty():
            print("Q inderflow")
        return self.items.pop(0)
    def show(self):
        return self.items

if __name__=="__main__":
    n = int(input("Enter the size of Queue:"))
    neq = F_que(n)

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