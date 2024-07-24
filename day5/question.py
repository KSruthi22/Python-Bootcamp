#check how many vowels are there in a string
str=input("enter the string")
count=0
for i in str:
    if i == 'a' or i=='e' or i=='i' or i=='o' or i=='u':
        count+=1
print(count)     

#check how many consonants are there in a string
str=input("enter the string")
count=0
for i in str:
    if i != 'a' or i!='e' or i!='i' or i!='o' or i!='u':
        count+=1
print(count) 

#length and "not in" is not used(brackets) 

check=['a','e','i','o','u']#can also be initialized as string
abc="bcdfghjklmnpqrstvwxyz"
count_vowels=0
count_cons=0
str="aeroplane"
inp=str.lower()
for i in inp:
    if (i in check):
        count_vowels+=1
for j in inp:
    if (j in abc):
        count_cons+=1
print(count_vowels)
print(count_cons)