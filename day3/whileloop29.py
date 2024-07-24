#sum of even digits in a number
n=int(input("enter n value"))
sum=0
while(n>0):
    digit=n%10
    if digit%2==0:
        sum+=digit
    n=n//10
print(sum)  