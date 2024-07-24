#reverse a number
n=int(input())
rev=""
while(n>0):
    revnum=n%10
    rev=rev+str(revnum)
    n=n//10
print(int(rev))  
