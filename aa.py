def push(stk,digit):
    a=stk.append(digit)
    print ("the number has been successfully added")
    for i in range (0, len(stk)):
        print (stk[i])
    top=len(stk)
    return stk

def isempty(stk):
    if len(stk)==0:
        return True
    else:
        return False

def pop(stk):
    if isempty(stk):
        return("underflow")
    else:
        a=stk.pop()
        if len(a)==0:
            top=none
        else:
            top=len(stk)-1



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
          pop(stk)

    elif ch==3:
        
        a= isempty(stk)
        if a==True:
            print ("yes")

                              
        

    elif ch==4:
          pass

    elif ch==5:
          pass

    else:
          continue
