stack=[]
def isEmpty():
    if stack==[]:
        return True
    return False
def push(ele):    
    return stack.append(ele)
def pop():
    if isEmpty():
        return None
    stack.pop()
def show():
    print(stack)
def lenght():
    print(len(stack))
def top():
    print(stack[-1])

push(2)
show()
pop()
show()
pop()