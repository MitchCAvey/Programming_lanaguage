from menu import Menu, MenuItem
from coffeeMaker import CoffeeMaker
from moneyMachine import MoneyMachine


menu = Menu()
#menuItems = MenuItem()
makeDrink = CoffeeMaker()
paymentProcessing = MoneyMachine()
is_on = True



while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        makeDrink.report()
        paymentProcessing.report()
    else:
        drink = menu.find_drink(choice)
        if makeDrink.is_resource_sufficient(drink):
            if paymentProcessing.make_payment(drink.cost):
                makeDrink.make_coffee(drink)


        #print(drink)
