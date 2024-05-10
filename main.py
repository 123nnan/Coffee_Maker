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


def check_resource(ingredients):
    """Returns True when resources is enough, False if not"""
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f'Sorry there is not enough {item}')
            return False
    return True

def process_coins():
    """Process the coins"""
    print('Please insert coins.')
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = round((0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies), 2)
    return total


def transaction_success(amount_recieve, cost_coffee):
    """Return True when transaction is success"""
    if amount_recieve > cost_coffee:
        change = amount_recieve - cost_coffee
        print(f'Here is ${change} for your change.')
        global profit
        profit += cost_coffee
        return True
    elif amount_recieve == cost_coffee:
        print(f'Thank you for the exact amount! ❤')
        profit = resources['money']
        profit += cost_coffee
        return True
    else:
        print(f"Sorry that's not enough money. ${amount_recieve} refunded")
        return False

def make_coffee(name_drink, ingredient_name):
    """Will deduct the ingredients from resources"""
    for item in ingredient_name:
        resources[item] -= ingredient_name[item]
    print(f'Here is your {name_drink} coffee!. ☕ Enjoy!')


on_machine = True
profit = 0
while on_machine:

    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    if user_choice == 'off':
        on_machine = False

    elif user_choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[user_choice]
        if check_resource(drink['ingredients']):
            payment = process_coins()
            if transaction_success(payment, drink['cost']):
                make_coffee(user_choice, drink['ingredients'])


