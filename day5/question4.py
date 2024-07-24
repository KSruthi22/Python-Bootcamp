#hello--------world
#--------hello world
print(ord('-'))
str1=input("enter the string")
str2=""
count=0
for i in str1:
    if (i=="-"):
        count+=1
    else:
        str2+=i
print("-"*count+str2)        


        


