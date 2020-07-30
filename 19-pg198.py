line = input("enter a line : ")
lowercount = uppercount = spaces = 0
for a in line :
    if a.islower():
        lowercount +=1
    elif a.isspace():
        spaces +=1
    elif a.isupper ():
        uppercount +=1 
    

print ("number of lower chars : ",lowercount)
print ("number of upper chars : ", uppercount)
