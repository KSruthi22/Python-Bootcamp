my_list=list(map(int,input("enter the list numbers").split(" ")))
length=len(my_list)
for i in range (length//2):
    temp=my_list[i]
    my_list[i]=my_list[length-i-1]
    my_list[length-i-1]=temp
print(*my_list)    

