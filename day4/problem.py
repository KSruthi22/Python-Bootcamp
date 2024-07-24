#write a program to find prime number in between two numbers
num1=int(input("enter 1st numner"))
num2=int(input("enter 1st numner"))
for i in range(num1,num2+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ") 

#try using square root method     
num1=int(input("enter 1st numner"))
num2=int(input("enter 1st numner"))
for i in range(num1,num2+1):
    for j in range(2,i**0.5+1):
        if i%j==0:
            break
    else:
        print(i,end=" ")    