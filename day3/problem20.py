#find the minimum element in a given list
my_list=list(map(int,input("enter list values").split(" ")))
mini=my_list[0]
for i in range(len(my_list)):
      if my_list[i]<mini:
         mini=my_list[i]
print(mini)  