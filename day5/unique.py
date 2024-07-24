#print unique characters in a string
str=input("enter the string")
ans=""
abc="abcdefghijklmnopqrstuvwxyz"
count=0
inp=str.lower()
for i in inp:
    if i not in ans:
        ans+=i
print(ans)
         