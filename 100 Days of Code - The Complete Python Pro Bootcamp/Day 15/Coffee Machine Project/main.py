MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def resource_check(order_ingredients):
    """checks for enough ingredients to make the drink, else returns false"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True

# TODO nest this so that AFTER the user selects a drink, this can be a running deduction from the price. If they pick a $3 drink, show the amount they still owe after the first coins are put in.
def money_ingestion():
    print("Please insert coins: ")
    total = int(input("How many Quarters?: ")) * 0.25
    balance = MENU[user_choice]["cost"] - total
    print(f"You still owe {balance}.")
    total += int(input("How many Dimes?: ")) * 0.1
    print(f"You still owe {balance}.")
    total += int(input("How many Nickles?: ")) * 0.05
    print(f"You still owe {balance}.")
    total += int(input("How many Pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    global profit
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    elif money_received == drink_cost:
        profit += drink_cost
        return True
    else:
        print("Sorry, that is not enough money. Money is refunded.")
        return False

def make_drink(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

is_on = True

while is_on:
    user_choice = input("Welcome to the world of coffee!!!! What drink would you like? An espresso? A Latte? Or a cappuccino?")
    if user_choice.lower() == "off":
        is_on = False
    elif user_choice.lower() == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        if resource_check(drink["ingredients"]):
            payment = money_ingestion()
            if is_transaction_successful(payment, drink["cost"]):
                make_drink(user_choice, drink["ingredients"])




"""def money_sufficient(money):
I don't like her solution, need to figure a better way to do this
since the example uses a coin-operated machine, this is a necessity for this example only
"""

# TODO need to add a funciton to print current resourcese if we type 'report'. Also, off to turn off the machine

# TODO nest this in a while loop to call the machine 'on' or 'off'

# TODO capture user inputs (report prints current state of resources, 3 coffee options call prices, anything else is an error)

"""
check if money is adequate
then intake choice for drink
then term the loop
"""