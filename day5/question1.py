#print all the consonants in a string
str=input("enter string")
abc="bcdfghjklmnpqrstvwxyz"
for i in str:
    if i in abc:
        print(i,end=" ")

#print all the vowels followed by consonants in a string       
str=input("enter string")
vow="aeiou"
abc="bcdfghjklmnpqrstvwxyz"
ans=""
inp=str.lower()
for i in inp:
    if i in vow:
        ans+=i
for i in inp:       
     if i in abc:
         ans+=i  
print(ans)          