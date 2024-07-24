#Find the element that is present in k+nth index position 
k=int(input("enter k value"))
n=int(input("enter n value"))
list1=list(map(int,input("enter list values").split(" ")))
length=len(list1)
if k+n>length:
     print("ERROR")
else:
    for i in range (len(list1)):
         print(list1[k+n])
         break
     
          

