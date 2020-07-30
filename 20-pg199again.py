abc = str(input("enter a line : "))
sub = str(input("enter a phrase to count how many times it occurs in the line : "))
strlen = len(abc)
count = 0
found_loc = 0
from_point = 1

while found_loc != -1:
    found_loc = abc.find(sub,from_point,strlen)
    if found_loc != -1:
        count +=1
        from_point = found_loc + 1

        

print (count)
