 #problem statement :-print even or odd and postiv or negative of a number
number=int(input("enter a number"))
if (number%2==0) and (number>0):
     print("number is even and postive")
elif (number%2!=0) and (number>0): 
      print("number is odd and postive")  
elif (number%2==0) and (number<0): 
     print("number is even and negative") 
else:
     print("number is odd and negative")