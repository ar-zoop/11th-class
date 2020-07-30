###queue implementation###

#function
def push(q,data):
    q.append(data)
    if len(q)==1:
        front=rear=0
    else:
        front=0
        rear=len(q)-1
    return q

def pop(q):
    if isempty(q):
        return "underflow"
    else:
        front=0
        q.pop(front)
        return q

def isempty(q):
    if len(q)==0:
        return True
    else:
        return False

def peek(q):
    if isempty(q):
        return "underflow"
    else:            
        front=0
        return(q[front])

def display(q):
    if isempty(q):
        return "underflow"
    else:
        if len(q)==1:
            front=rear=0
            print (q[front])
        else:
            front=0
            rear=len(q)-1
            for i in range (front, rear+1):
                print (q[i])
        
    

#main programme
q=[]
front=rear=None
while True:
    print ("1.push")
    print ("2.pop")
    print ("3.peek")
    print ("4.display")
    print ("5.exit")
    ch=int(input("enter a number of your choice: "))

    if ch==1:
        data= int(input("enter a number to add to the queue: "))
        push(q,data)
        print ("number added successfully to the queue!")

    elif ch==2:
        a=pop(q)
        if a=="underflow":
            print ("underflow")
        else:
            print ("number deleted successfully")

    elif ch==3:
        a=peek(q)
        if a=="underflow":
            print ("underflow")
        else:
            print (a)
        
    elif ch==4:
        a=display(q)
        if a=="underflow":
            print ("underflow")
        else:
            pass

    elif ch==5:
        break

    else:
        continue
