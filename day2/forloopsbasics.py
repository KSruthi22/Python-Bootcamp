#METHOD1:-
new_list=list(map(int,input("enter list values").split(" ")))
for i in range(len(new_list)):
    print(new_list[i],end=" ")#prints values in new list
#print(i,end=" ")#prints index of each values
#METHOD2:-
for i in new_list:
     print(i,end=" ")
