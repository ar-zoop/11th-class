a = int (input("enter a : "))
b = int (input("enter b : "))
c = int (input("enter c : "))

big = a
if b>big:
    big = b
if c>big:
    big = c

print ("The biggest number is : ", big)
