


while True:
    choice = int(input("Type 1 for Arithmetic and 2 for Geometry: "))
    
    if choice==1 :
        while True:
            num1= int(input("type first number: "))
            num2= int(input("type second number: "))
            op= str(input("choose an operator [+,-,*,/,^,e] e to exit to main menu : "))

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
            elif op == '^':
                total = num1 ** num2
                print (num1, "^", num2, "=", total)

            elif op=='e':
                break
                     
            else:
                print ("invalid operator")
                continue
                
    elif choice==2 :
        while True:
            areaop= int(input("Type 1 for area of right triangle, 2 for rectangle and 9 to exit: "))
            if areaop==1:
                num1= int(input("type first number: "))
                num2= int(input("type second number: "))
                triangle= float((num1*num2)/2)
                print ("area of right triangle is ",triangle)

            elif areaop==2:
                num1= int(input("type first number: "))
                num2= int(input("type second number: "))
                square= float(2*(num1+num2))
                print ("area of rectangle is ", square)
                       
            elif areaop==9:
                break
            else :
                continue
   
    else:
        continue

