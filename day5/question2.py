str1=input("enter the string")
check="0123456789"
ans=0
for i in str1:
    if i in check:
        ans+=int(i)
print(ans)        
