bill=input("welcome to the tip calculatopr \nWhat was the total bill? $")
people=input("How many people to split the bill?")
tips=input("What percentage tip would you like to give? 10,12 or 15?")
result=(float(bill)+((float(bill)/100)*float(tips)))/int(people)
print(f'Each person should pay: ${round(result,1)}')