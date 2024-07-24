#print the element in a particular index,condition:-cyclic printing
k=int(input("enter k value"))
list1=list(map(int,input("enter list values").split(" ")))
length=len(list1)
for i in range (len(list1)):
     if k>length:
         print(list1[k-length])
         break
     else:
         print(list1[k])
         break

#k=20
#70 54 36 72 76 9999 0089        k=20..length=7
#1   2  3  4  5   6   7          index=6

#k=35
#78 8394 8773 8297 9182 9187 27292 3487      k=35...length=8
# 1   2    3   4     5    6    7     8       index=3

#k=28
#827 873 277 626 76276 178271 271627 271673 8172 827182     k=28..length=10
# 1   2   3   4    5      6     7      8      9     10       index=8
#if many cycle iterations
k=int(input("enter k value"))
list1=list(map(int,input("enter list values").split(" ")))
length=len(list1)
for i in range (len(list1)):
     if k>length:
         print(list1[k%length-1])
         break
     else:
         print(list1[k])
         break
 