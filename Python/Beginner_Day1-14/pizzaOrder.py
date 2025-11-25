
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N: ") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N: ") # Do you want extra cheese? Y or N
bill = 0
extrasCost = 0

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        extrasCost = 2
        if extra_cheese == "Y":
           extrasCost += 1
           bill += extrasCost
           #print(f"Cost of extras, ${extrasCost}")
        elif extra_cheese == "N":
            bill += extrasCost  
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            extrasCost = 1
            bill += extrasCost
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        extrasCost = 3
        if extra_cheese == "Y":
           extrasCost += 1
           bill += extrasCost
        elif extra_cheese == "N":
            bill += extrasCost  
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            extrasCost = 1
            bill += extrasCost
else:
    bill = 25
    if add_pepperoni == "Y":
        extrasCost = 3
        if extra_cheese == "Y":
           extrasCost += 1
           bill += extrasCost
        elif extra_cheese == "N":
            bill += extrasCost  
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            extrasCost = 1
            bill += extrasCost


print(f"Your Total Bill is: {bill}")
"""
    if size == "M":
        bill = 20
        if size == "L":
            bill = 25
"""