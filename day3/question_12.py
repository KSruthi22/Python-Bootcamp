#find the dupilcates in an array
my_list=list(map(int,input("enter array elemnts").split(" ")))
dupli=[]
fresh=[]
for i in my_list: 
    if i not in fresh:
        fresh.append(i)
    else:
        dupli.append(i)
print(dupli)

