#sum of the numbers in list:
lst1=list(map(int,input("enter numbers").split(" ")))
sum=0
for i in range(len(lst1)):
    sum+=sum+lst1[i]
print(sum)    
