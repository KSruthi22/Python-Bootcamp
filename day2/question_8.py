#given an space separated integer list,find the average of elements present in the even index
list1=list(map(int,input("enter numbers").split(" ")))
total=0
count=0
length=len(list1)
for i in range(len(list1)):
     if i%2==0:
          total+=list1[i]
          count+=1
average=total/count
print(average)