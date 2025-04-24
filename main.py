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

money = 0

# TODO: 3. print report.
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

#TODO: 4. Check resources sufficient?
def check_resources_sufficient(user_choice):
    selected_coffee = MENU[user_choice]

    can_make_coffee = True
    required_ingredients = selected_coffee["ingredients"]
    for ingredient in required_ingredients:
        if resources[ingredient] < required_ingredients[ingredient]:
            can_make_coffee = False
            print(f"Sorry there is not enough {ingredient}.")
            break
    return can_make_coffee

#TODO: 5. Process coins.
def process_coins():
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return  quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

# TODO: 7. Make Coffee.
def make_coffee(user_choice):
    selected_coffee = MENU[user_choice]
    required_ingredients = selected_coffee["ingredients"]
    for ingredient in required_ingredients:
        print(f"{ingredient} spent: {required_ingredients[ingredient]}")
        resources[ingredient] -= required_ingredients[ingredient]
    print("Here is your latte ☕️. Enjoy!")

# TODO: 6. Check transaction successful?
def check_amount_sufficient(user_choice, amt):
    selected_coffee = MENU[user_choice]
    selected_coffee_amount = selected_coffee["cost"]

    is_amount_sufficient = False
    if amt >= selected_coffee_amount:
        is_amount_sufficient = True
        if amt > selected_coffee_amount:
            print(f"Here is ${amount - selected_coffee_amount} dollars in change.")
    else:
        print(f"Sorry that's not enough money. Money refunded. Coin inserted Total amount: ${amt}")
    return is_amount_sufficient

# TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
is_machine_on = True
coffee_list = ["espresso", "latte", "cappuccino"]
while is_machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    # ToDo: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    if choice == "off":
        is_machine_on = False
    elif choice == "report":
        print_report()
    elif choice in coffee_list:
        if check_resources_sufficient(choice):
            amount = process_coins()
            if check_amount_sufficient(choice, amount):
                money += MENU[choice]["cost"]
                make_coffee(choice)
    else:
        print("Invalid selection")