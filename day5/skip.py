str1=input("enter string")
n=int(input("enter skip value"))
inp=str1.upper()
empty=""
for i in inp:
    if i>=97 and i<=122:
         empty+=chr(ord(i)+n)
print(empty)
#-26 x=120+3=123-------->a=97
