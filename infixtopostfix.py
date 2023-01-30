import stack

inp=input("Enter the infix expression:").split(" ")
inp=list(inp)
n=len(inp)
newstack=stack.Stack(n)
opend= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
oper=["(",")","*","/","+","-","&","^","&&","||"]
out=""
for i in inp:
    if i in opend:
        out=out+i
    if i in oper:
        if newstack.isEmpty(): 
            newstack.push(i)
        else:    
            if i==oper[0]:
                newstack.push(i)
            elif i==oper[4] and newstack.top()!=oper[5] or newstack.top()==oper[6] or newstack.top()==oper[7] or newstack.top()==oper[8] or newstack.top()==oper[9] and newstack.top()!=oper[4]:
                newstack.push(i)
            else:
                y=newstack.pop()
                out=out+y
                newstack.push(i)
            if i==oper[5] or newstack.top()==oper[6] or newstack.top()==oper[7] or newstack.top()==oper[8] or newstack.top()==oper[9] and newstack.top()!=oper[5] and newstack.top()!=oper[4]:
                newstack.push(i)
            else:
                y=newstack.pop()
                out=out+y
                newstack.push(i)
            if i==oper[2] or newstack.top()==oper[4] or newstack.top()==oper[5] or newstack.top()==oper[6] or newstack.top()==oper[7] or newstack.top()==oper[8] or newstack.top()==oper[9] and newstack.top()!=oper[2] and newstack.top()!=oper[3]:
                newstack.push(i)
            else:
                y=newstack.pop()
                out=out+y
                newstack.push(i) 
            # if i==oper[3] or newstack.top()==oper[4] or newstack.top()==oper[5] or newstack.top()==oper[6] or newstack.top()==oper[7] or newstack.top()==oper[8] or newstack.top()==oper[9] and newstack.top()!=oper[2] and newstack.top()!=oper[3]:
            #     newstack.push(i)
            # else:
            #     y=newstack.pop()
            #     out=out+y
            #     newstack.push(i)     
            
            if i==oper[1]:
                while i!="(":
                    x=newstack.pop()
                    out=out+x
                    i=x
                out=out[:-2]  
         
print(out)
print(newstack.show())