my_list=list(map(int,input("enter list elemnts").split(" ")))
maxi=my_list[0]
for nums in range (len(my_list)):
    if my_list[nums]>maxi:
        maxi=my_list[nums]
print("maximum element: ",maxi)    