#reverse the string
#hello123:321
str1=input("enter the string")
num='0123456789'
ans=""
for i in str1:
    if i in num:
        ans+=i
res=int(ans)
empty=""
while(res>0):
    digit=res%10
    empty+=str(digit)
    res=res//10
print(empty)    
    
