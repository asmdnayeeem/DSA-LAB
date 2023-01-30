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
     if i in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
        newstack.push(i)   
     if i=="+":
         x=newstack.pop()
         y=newstack.pop()
         z=newstack.push("+"+y+x)
         
         
     if i=="-":
         x=newstack.pop()
         y=newstack.pop()
         z=newstack.push("-"+y+x)
         
     if i=="*":
         x=newstack.pop()
         y=newstack.pop()
         z=newstack.push(y+"*"+x)
         
     if i=="/":
         x=newstack.pop()
         y=newstack.pop()
         z=newstack.push(y+"/"+x)
         
     if i=="&":
         x=newstack.pop()
         y=newstack.pop()
         z=newstack.push(y+"&"+x)
         
     if i=="^":
         x=newstack.pop()
         y=newstack.pop()
         z=newstack.push(y+"^"+x)
         
     if i=="&&":
         x=newstack.pop()
         y=newstack.pop()
         z=newstack.push(y+"&&"+x)
         
     if i=="||":
         x=newstack.pop()
         y=newstack.pop()
         z=newstack.push(y+"||"+x)
         

final=newstack.show()
final=final[0]
print("Prefix expression is:",final)
