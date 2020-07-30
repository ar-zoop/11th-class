def adding(x):
    a=0
    while x>=1:
        
        a=a+(x%10)
        x=x//10
    return a;
c=int (input("enter value:"))
d= adding(c)
print (d);
