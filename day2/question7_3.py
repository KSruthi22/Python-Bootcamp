#7.3:-you are given with a space separaed integer list,find number of even and odd elements
list3=list(map(int,input("enter comma separated numbers").split(",")))
even=0
odd=0
for i in range(len(list3)):
    if list3[i]%2==0:
        even+=1
    else:
          odd+=1
print(even) 
print(odd)
