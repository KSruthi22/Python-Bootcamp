str1=input("enter the string")
ans=0
for i in str1:
    if (ord(i)>=48 and ord(i)<=57):
        ans+=i
print(ans) 