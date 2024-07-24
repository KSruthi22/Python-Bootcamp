#list:-mutable,ordered
#static input:-
list1=[4,2,6,7]
print(list1)
#without commas:-use end 
#without brackets:-use *
print(*list1)
#appending :default inserting at last:-
list1.append(99)
print(*list1)
print(*list1,end="@\n")
#inserting:-if index exists,inserts at that place else at last
list1.insert(800,99)
print(*list1)
list1.insert(1,99)
print(*list1)
#length:-
print(len(list1))
#pop:-gives the last element
print(list1.pop())
print(*list1)
'''#index out of bound error if:-
print(list1.pop(8))'''
# + doesnt add the elements correspondingly,instead appends
list2=[6,8,2,2]
list3=list1+list2
print(*list3)
#copy:-
new_list=list2.copy()
print(*new_list)
#count:-
print(new_list.count(2))
#sorting:-
new_list.sort()
print(*new_list)
#backend used method:-quick sort-nlogn
#aggregate functions:-count,min,max
