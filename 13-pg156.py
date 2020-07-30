import random
r = random.randint (10,15)
n=1
while n<6 :
        a = int (input("guess a number between 10 to 15 : "))
        if a==r:
            print ("you win")
            break
            

        else:
            n+=1
if n>5:
    print ("you lose")

