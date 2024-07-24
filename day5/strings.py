#immutable
#string methods are:-
#isalnum
#length
#islower:converts to lowercase
#isupper:converts to uppercase
#isalpha
#isnumeric
#isdigit
#titlecase
#swap case
str=input("enter a string")
print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.title())
print(str.swapcase())
print(str.strip())#eliminates the spaces at first and last 
print(str.replace('o','k'))
print(str.split())
print(str.split('o'))


str="Hello world 123"
print(str.isalpha())
print(str.isnumeric())
print(str.isalnum())
print(str.isascii())
print(str.islower())
print(str.isupper())
print(str.istitle())
print(str.isdigit())