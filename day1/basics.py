#datatypes:-int,float,string,sets,boolean,tuple,dictionary ,
var1="python"
print("good morning",var1)
name=input("enter your name")
print(name)
#taking input in nextline:-
name=input("enter your name\n")
print(name)
#static input
age=20
name="kavya"
print(f"hello {name} , you are {age} years old")
#taking integer input from user
num1=int(input())
num2=int(input())
num3=int(input())
total=num1+num2+num3
avg=total/3
print(f"kavya got average marks of {avg}")
#by default string inputs
num1=10
num2=20
num3=30
total=num1+num2+num3
avg=total/3
print(f"kavya got average marks of {avg}")
#space seprated inputs
name="kavya"
print(name,end=" ")
print(name)
#conditional statements:-if,elif,else
num1=int(input("enter your age"))
if(num1>=18):
    print("you are eligible to vote")
else:
    print("you are not eligible to vote") 
