

billAmount = float(input("Enter bill amount? "))
splitNum = int(input("How many people are you spliting the bill with? "))
tipAmount = int(input("tip amount you want to give(10, 12, or 15)?"))

#print(f"tip percentage = {(tipAmount / 100) + 1}")
totalTipAmount = ((billAmount / splitNum) * ((tipAmount / 100) + 1))


#print(f"Your tip amount is: {round(totalTipAmount, 2)}")
print(f"Your tip amount is: {totalTipAmount:.2f}")