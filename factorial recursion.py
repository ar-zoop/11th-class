def factorial(n):
    r=n
    if n==1:
        return 1
    else:
        return r* factorial(n-1)

a= int(input("enter a number:"))
v= factorial(a)
print (v)
