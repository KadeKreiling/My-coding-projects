MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "money": 0,
}
coffee_machine_on = True
import sys
import os
def coffee_machine():
    coffee_choice = input("What kind of coffee would you like? (espresso/cappuccino/latte) ")
    if coffee_choice == "off":
        sys.exit()
    if coffee_choice == "report":
        print(resources)
    else:
        water = MENU[coffee_choice]["ingredients"]["water"]
        milk = MENU[coffee_choice]["ingredients"]["milk"]
        coffee = MENU[coffee_choice]["ingredients"]["coffee"]
        if coffee_choice == "espresso" or "cappuccino" or "latte":
            if water > resources["water"] or milk > resources["milk"] or coffee > resources["coffee"]:
                if water > resources["water"]:
                    print("Sorry there is not enough water.")
                elif milk > resources["milk"]:
                    print("Sorry there is not enough milk.")
                else:
                    print("Sorry there is not enough coffee.")
            else:
                num_quarters = float(input("How many quarters? ")) * .25
                num_dimes = float(input("How many dimes? ")) * .1
                num_nickels = float(input("How many nickels? ")) * .05
                num_pennies = float(input("How many pennies? ")) * .01
                total = round(num_pennies + num_dimes + num_nickels + num_quarters, 2)
                if total < MENU[coffee_choice]["cost"]:
                    print("Sorry that is not enough money. Refunded money")
                else:
                    resources["water"] -= water
                    resources["milk"] -= milk
                    resources["coffee"] -= coffee
                    resources["money"] += MENU[coffee_choice]["cost"]
                    change = round(total - MENU[coffee_choice]["cost"], 2)
                    print(f"Here is your {coffee_choice}! Enjoy!")
                    print(f"Here is your change. ${change}")
    coffee_machine()





coffee_machine()