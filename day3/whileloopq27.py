  
#find the sum of squares of a digit in a given number
n=int(input("enter n value"))
square=0
while(n>0):
    digit=n%10
    square+=digit**2
    n=n//10
print(square)

