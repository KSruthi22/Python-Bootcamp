#find the missing element in a list
n=10
my_list=list(map(int,input("enter list elements").split(" ")))
total=n*(n+1)//2
sum=0
for i in range(len(my_list)):
    sum+=my_list[i]
print(total-sum)    