my_list=list(map(int,input("enter list elements").split(" ")))
max1=0
max2=0
for num in my_list:
    if num>max1:
        max2=max1
        max1=num
    elif num>max2 and num!=max1:
        max2=num
print("second maximum element is ",max2)            