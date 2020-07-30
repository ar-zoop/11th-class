def encrypt (a,b):
    return a.join(b)
#def decryption (a,b):
    #return a.split(b)

ss= str(input("enter a string for encrpytion: "))
k= str(input("enter encrption key: "))
enzo= encrypt(ss,k)
print (enzo)
#decryption (yum,x)
