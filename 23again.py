#n = 8
#for i in range (n):
 #   for j in range (int((n-i)/2)):
  #      print(" ", end="")
   # for j in range (0, i+1):
    #    print ("*", end="")
    #print ()


bigstr = "ARZOOxyz"
n = len(bigstr)
for i in range (n,0,-1):
    print (int((n-i)/2))

    for j in range (int((n-i)/2)):
        print(" ", end="")
   
    print ()


quit


bigstr = "ARZOOxyz"
n = len(bigstr)
for i in range (n):
    for j in range (int((n-i)/2)):
        print(" ", end="")
    for j in range (0, i+1):
        print (bigstr[j], end="")
    print ()


    

    
