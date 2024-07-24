#replace the elements in an array with average of maximum and minimum elements
my_list=list(map(int,input("enter list values").split(" ")))
maxi=my_list[0]
for i in range(len(my_list)):
      if my_list[i]>maxi:
         maxi=my_list[i]
mini=my_list[0]
for i in range(len(my_list)):
      if my_list[i]<mini:
         mini=my_list[i] 
average=(maxi+mini)//2
for i in range(len(my_list)):
     my_list[i]=average
print(*my_list)     
     
