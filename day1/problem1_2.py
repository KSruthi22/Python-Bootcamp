#problem statemet:a boy has an amount of 700 to buy n number of apples,n dozen bananas and n number 
#of oranges and the cost of each apple is 15/-,one banana is 4/- and orange is 5/-.Find if the boy gets cheated 
#if the total amount invested is greater than the total amount he had. 
napples=int(input("number of apples to buy"))
nbananas=int(input("number of bananas to buy"))
dozen=12
noranges=int(input("number of oranges to buy"))
cost_apples=15
cost_bananas=4
cost_oranges=5
amount=700
if (napples*cost_apples)+(nbananas*dozen*cost_bananas)+(noranges*cost_oranges) <= amount :
    print("the boy isnt cheated")
else:
   print("the boy got cheated") 