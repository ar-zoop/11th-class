
list1 = [2,3,1,4]
#eval (input ("enter a list : "))

list2 = []

for ele in list1:
    list2.append(ele)
    
list2.sort()
s= list2[0]
print (s, list1.index(s))
