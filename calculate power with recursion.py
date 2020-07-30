def exponent (power, base):
    r=power
    if r==0:
        return 1;

    else:
        return base * exponent(power-1,base)
        

a= int(input("enter a base:"))
b= int(input("enter a power"))
d= exponent(b,a)
print (d)

