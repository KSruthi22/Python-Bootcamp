#lcm*gcd=a*b
num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
n1=num1
n2=num2
while num2!=0:
     num1,num2=num2,num1%num2
res=(n1*n2)/num1
print("lcm of two numbers is : ",res)
