a= int (input ("enter a number : "))
b =int (input ("enter a number : "))
c =int (input ("enter a number : "))

sum1= a+b+c
print ("sum of all numbers is", sum1)

num= a+b+c

if a==b and a==c:
    num = 0

else:
    if a==c:
        num=b

    else:
        if a==b:
          num=c

        else:
            if c==b:
                num=a


print ("the sum of non duplicate numbers is:", num)

      
