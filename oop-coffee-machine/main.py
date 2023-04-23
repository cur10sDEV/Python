from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
options = menu.get_items()
money_machine = MoneyMachine()

to_continue = True

while to_continue:
    customer_choice = input(f"What would you like? ({options}): ")
    if customer_choice == "off":
        to_continue = False
    elif customer_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif customer_choice == "latte" or customer_choice == "espresso" or customer_choice == "cappuccino":
        customer_flavour = menu.find_drink(customer_choice)
        if coffee_maker.is_resource_sufficient(customer_flavour) and money_machine.make_payment(customer_flavour.cost):
            coffee_maker.make_coffee(customer_flavour)
    else:
        print(f"You have no power here..")