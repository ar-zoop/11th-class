a = int (input ("enter a number : "))
lim = int(a/2)+1
for i in range (2,lim):
    if a%i==0 :
        print ("it aint prime")
        break
else:
    print ('prime')

