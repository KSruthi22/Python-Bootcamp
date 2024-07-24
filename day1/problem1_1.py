#print two wheeleres can be allowed if the age is between 18 and 24 ,four wheeler too
# if the age is between 24 and 45 ,siz wheeler too if the age is above 45
age=int(input("enter the age"))
if(age>=18 and age<24):
    print("only two wheeler")
elif(age>=24 and age<45):
    print("two and four wheeler")   
else:
    print("two,four and six wheeler")    