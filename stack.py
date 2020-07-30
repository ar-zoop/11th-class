#FUNCTIONS
def push(stk,digit):
    a=stk.append(digit)
    print ("the number has been successfully added")
    top=len(stk)
    return stk

def pop(stk):
    if isempty(stk):
        return("underflow")
        
    else:
        a=stk.pop()
        if len (stk)==0:
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
    if isempty(stk):
        return "underflow"
    else:
        top=len(stk)-1
        print(stk[top])

def display(stk):
    top= len(stk)
    for i in range(-1,-top,-1):
        print (stk[i])
    
#main programme
stk=[]
top= None
while True:
    print("1.push")
    print("2.pop")
    print("3.peek")
    print("4.display stack")
    print("5.exit")
    ch=int(input("enter a number of choice: "))
    if ch==1:
          digit= int(input("enter a number to append: "))
          push(stk,digit) 

    elif ch==2:
          b=pop(stk)
          if b=="underflow":
              print ("underflow")
          else:
              print ("popped successfully")

    elif ch==3:
          a=peek(stk)
          if a=="underflow":
              print("underflow")
          else:
              print (a)
               
    elif ch==4:
          display(stk)
          

    elif ch==5:
        print("bye")
        
        break

    else:
          continue
