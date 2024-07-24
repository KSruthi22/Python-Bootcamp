#take a space seperated input from a user nd print alternate elements
list1=list(map(int,input("enter numbers").split(" ")))
for i in range(0,len(list1),2):
    print(list1[i])
