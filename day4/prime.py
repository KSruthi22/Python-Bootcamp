number=int(input("enter the number"))
count=0
if number<2:
     print("not a prime number")
elif number==2:
     print("prime number")    
for i in range(2,int(number**0.5+1)):
    if(number%i==0):
        count+=1
        break
if(count==0):
    print("prime number")
elif(count>0):
    print("not prime number")     



        
    

