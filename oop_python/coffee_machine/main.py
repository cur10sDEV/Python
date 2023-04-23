coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.1,
    "quarter": 0.25,
}

flavours = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "price": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "price": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "price": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def report(profit):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

def insert_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))*coins["quarter"]
    dimes = int(input("How many dimes?: "))*coins["dime"]
    nickels = int(input("How many nickels?: "))*coins["nickel"]
    pennies = int(input("How many pennies?: "))*coins["penny"]
    total = quarters+dimes+nickels+pennies
    return total

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    
    return True
    
def is_transaction_successful(money, cost_of_flavour):
    if money < cost_of_flavour:
        return False
    return True

def make_coffee(ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is ${round(change, 2)} in change.")
    print(f"Here is your {user_input} Enjoy!")

to_continue = True
while to_continue:
    user_input = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
        report(profit)
        
    elif user_input == "off":
        to_continue = False
        
    elif user_input == "latte" or user_input == "cappuccino" or user_input == "espresso":
        flavour = flavours[user_input]
        ingredients = flavour["ingredients"]
        price = flavour["price"]
        response = check_resources(ingredients)
        
        if response:
            total = insert_coins()
            if is_transaction_successful(total, price):
                change = total - price
                profit += price
                make_coffee(ingredients)
                
            else:
                print("Sorry that's not enough money. Money refunded")
        else:
            continue
    else:
        print(f"Sorry we dont serve this flavour i.e., {user_input}. :(")