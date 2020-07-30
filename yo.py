import math as m
n=7
for line in range (1, n+1):
    c=1
    for i in range (1, line+1):
        print (int (c), end= "")
        c=c*(line-i)/i
    print ("")
