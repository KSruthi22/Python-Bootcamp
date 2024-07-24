#5 7 13 24 37
my_list=list(map(int,input("enter list elemnts").split(" ")))
for i in range(1,len(my_list)-1):
    if my_list[i]>my_list[i+1] and my_list[i-1]<my_list[i]:
        print(my_list[i],end=" ")    

#if last element is the peak element
my_list=list(map(int,input("enter list elemnts").split(" ")))
for i in range(1,len(my_list)-1):
    if my_list[i]>my_list[i+1] and my_list[i-1]<my_list[i]:
        count=i
if my_list[-1]>my_list[-2] and my_list[-1]>count:
    count=len(my_list)-1
print(my_list[count])    
        