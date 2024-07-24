#write a code to print all the capital letter in a given string
'''str1=input("enter the string")
ans=""
for i in str1:
    if ord(i)>=65 and ord(i)<=90:
        ans+=i
print(ans)  '''
#91 93 40 41 123 125
#remove all the braces in the given algebraic expression
str1=input("enter algebraic expression")
str2=""
for i in str1:
    if (ord(i)!=91 or ord(i)!=93 or ord(i)!=40 or ord(i)!=41 or ord(i)!=123 or ord(i)!=125):
        str2+=i
print(str2) 


str1=input("enter algebraic expression")
for i in str1:
    if (ord(i)==91 or ord(i)==93 or ord(i)==40 or ord(i)==41 or ord(i)==123 or ord(i)==125):
        pass  
    else:
        print(i,end=" ")
        