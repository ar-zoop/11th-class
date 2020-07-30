a = int (input ("enter a number : "))
lim = int(a/2)+1
is_prime = True
for i in range (2,lim):
    if a%i==0 :
        print ("it aint prime")
        is_prime = False
        break
if is_prime:
    print("is prime")
