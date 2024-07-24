#7.2:-#count the number of even numbers
list2=list(map(int,input("enter comma separated numbers").split(",")))
even=0
for i in range(1,len(list2)):
    if list2[i]%2==0:
        even+=1
print(even) 