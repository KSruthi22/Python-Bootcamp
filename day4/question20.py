#password verifier
#Mr.X is trying to create a new password for his instagram account.THese are the require conditions
# for creating a new password:
# conditions: 1)minimum lenght is 8,max length is 15
#2) only @,/ is allowed in the password
#3)no spaces are allowed
#4)only alpha numerics are allowed
#You are supposed to print weak if length is exact 8,medium if length is between 8-12.strong if length is between 2-15 
password=input("enter the password")
length=len(password)
spl_string="@/"
count=0
if length<8 or length>15:
    print("please follow instructions")
for i in password:
    if i in (spl_string[0] or spl_string[1]) and i!=" ":
        count+=1
        break
    if count>=1:
        if length==8:
            print("weak")
            break
        elif length>=8 or length<=12:
            print("medium")
            break
        elif length>=12 or length==15:
            print("strong")
            break


        

