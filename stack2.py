##stack implemetation##

#functions
def push(stk,digit):
    stk.append(digit)
    top=len(stk)
    return stk

def pop(stk):
    if isempty(stk)== True:
        return ("underflow")
    else:
        stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
        return stk   

def isempty(stk):
    if len(stk)==0:
        return True
    else:
        return False

def peek(stk):
    if isempty(stk)== True:
        return "underflow"
    else:
        top= len(stk)-1
        return stk[top]

def display(stk):
    if isempty(stk):
        return "underflow"
    else:
        top=len(stk)-1
        for i in range(top,-1,-1):
            print (stk[i])

    
#main programme

stk=[]
top=None
while True:
    print ("1.push")
    print ("2.pop")
    print ("3.peek")
    print ("4.display stack")
    print ("5.exit")
    ch= int(input("enter your choice of number: "))

    if ch==1:
        data= int(input("enter the number to add to stack: "))
        push(stk, data)
        print ("number added to the stack successfully!")

    elif ch==2:
        a= pop(stk)
        if a=="underflow":
            print ("underflow")
        else:
            print ("the number was deleted")

    elif ch==3:
        a=peek(stk)
        if a=="underflow":
            print ("underflow")
        else:
            print (a)

    elif ch==4:
        a=display(stk)
        if a=="underflow":
            print ("underflow")
        else:
            pass

    elif ch==5:
        print ("you exited")
        break

    else:
        continue
