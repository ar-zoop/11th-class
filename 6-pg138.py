

while True:
    num1= float(input("type first number: "))
    num2= float(input("type second number: "))
    op= str(input("choose an operator [+,-,*,/] : "))
    if op=='+' :
        total= num1+ num2
        print (num1, "+", num2,"=", total)

    elif op=='-':
        total= num1-num2
        print (num1, "-", num2, "=", total)

    elif op == '*':
        total = num1*num2
        print (num, "*", num2, "=", total)
     
    elif op == '/' :
        if num2!=0:
            total=num1/num2
            print (num1, "/", num2, "=", total)
        else:
            print ("divisor cannot be 0")
        
    else:
        print ("invalid operator")

