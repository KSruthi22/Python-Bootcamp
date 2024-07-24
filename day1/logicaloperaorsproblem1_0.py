#Mr. z is selected for olympics participating in swimming competition,Mister x
# and Mr. y are z freinds,,,x is badminton...y is tabletennis...a/c to selection commitee ..the requirements for 
# badminton players are 1)height 140 cm 2)weight factors of 2 3)bodyfat<12% 
#a/c to selection committee ..requirements for tabletennis are 
#1)height min=118cm to 148 cm 
#2)weight=factors of number of medals won by z
#3)bodyfat =14%,
#a/c to previous history,z participated in 14games ..out of which he is having success rate of 
#50%.Write a program whether x,y,z travels in the same plane or not 
x_height=int(input("height eligibilty for badminton"))
x_weight=int(input(" weight eligibilty for badminton"))
x_bodyfat=int(input("bodyfat eligibilty for badminton"))
y_height=int(input("height eligibilty for tabletennis"))
zmedals=(50/100)*14
y_weight=int(input("weight eligibilty for tabletennis"))
y_bodyfat=int(input("bodyfat eligibilty for tabletennis"))
if (x_height>=140) and (x_weight%2==0) and (x_bodyfat<12):
    if (y_height>=118 or y_height<=148) and y_weight%zmedals==0 and y_bodyfat==14: 
        print("x,y,z are travelling in same plane")
    else:
        print("only x,z are travelling in same plane")
else:
     print("only z is travelling in the plane")           
        
      



