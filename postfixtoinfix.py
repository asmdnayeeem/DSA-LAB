import stack
inp=input("Enter the postfix expression:").split(" ")
inp=list(inp)
n=len(inp)
nstack=stack.Stack(n)
newstack=stack.Stack(n)
for i in inp:
    nstack.push(i)
a=nstack.show()
print(a)
for i in a:
    try:
        if (type(int(i))==int) :
            newstack.push(int(i))
    except ValueError:
     if i=="+":
         x=newstack.pop()
         y=newstack.pop()
         z=newstack.push(int(y+x))
         
     if i=="-":
         x=newstack.pop()
         y=newstack.pop()
         z=newstack.push(int(y-x))
     if i=="*":
         x=newstack.pop()
         y=newstack.pop()
         z=newstack.push(int(y*x))
     if i=="/":
         x=newstack.pop()
         y=newstack.pop()
         z=newstack.push(int(y/x))
     if i=="&":
         x=newstack.pop()
         y=newstack.pop()
         z=newstack.push(int(y)&int(x))
     if i=="^":
         x=newstack.pop()
         y=newstack.pop()
         z=newstack.push(int(y)^int(x))
     if i=="&&":
         x=newstack.pop()
         y=newstack.pop()
         z=newstack.push((y and x))
     if i=="||":
         x=newstack.pop()
         y=newstack.pop()
         z=newstack.push((y or x))

print(newstack.show())
        


