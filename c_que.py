class c_que:
    def __init__(self,n) -> None:
        self.n=n
        self.front=-1
        self.rear=-1
        self.items=[None for i in range(n)]
    def isEmpty(self):
        if (self.first == -1 and self.last == -1) or (self.first == self.n and self.last == self.n-1):
            return True
        return False
    