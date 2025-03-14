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

QUARTER_VALUE = 0.25
DIME_VALUE = 0.10
NICKEL_VALUE = 0.05
PENNY_VALUE = 0.01

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

# Print report of machine's current resources
def print_report():
    global profit
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = profit
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")

#  Function to turn off machine
def turn_off():
    exit()

# Prompt user for type of coffee
def get_user_selection():
    """Prompts user for selection & returns input string lower case."""
    return input("What would you like? (espresso/latte/cappuccino): ").lower()

def get_menu_item(choice):
    """Takes user choice string & returns menu item at index of choice."""
    try:
        item = MENU[choice]
        return item
    except KeyError:
        print("That's not a valid selection. Try again.")
        get_menu_item(get_user_selection())

# Check if resources sufficient for selected coffee
def check_resources(selected_item):
    for key in selected_item['ingredients']:
        if resources[key] < selected_item['ingredients'][key]:
            print(f"Sorry, there is not enough {key}.")
            return False
        else:
            return True

# Prompt coin inputs
def get_coins_and_total_value():
    """Prompts inputs for number of quarters, dimes, nickels & pennies. Returns dollar value of all coins."""
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    error_text = "Invalid number of coins. Please enter an integer."
    try:
        quarters = int(input("How many quarters?: "))
    except ValueError:
        print(error_text)
        quarters = int(input("How many quarters?: "))
    try:
        dimes = int(input("How many dimes?: "))
    except ValueError:
        print(error_text)
        dimes = int(input("How many dimes?: "))
    try:
        nickels = int(input("How many nickels?: "))
    except ValueError:
        print(error_text)
        nickels = int(input("How many nickels?: "))
    try:
        pennies = int(input("How many pennies?: "))
    except ValueError:
        print(error_text)
        pennies = int(input("How many pennies?: "))
    total = (quarters * QUARTER_VALUE) + (dimes * DIME_VALUE) + (nickels * NICKEL_VALUE) + (pennies * PENNY_VALUE)
    return round(total, 2)


# Check if sufficient coins entered for selected coffee price
def check_funds(selected_item):
    """Takes a dictionary item with cost attribute. Compares cost to value returned from get_coins_and_total_value. Returns boolean for sufficient funds."""
    money_added = get_coins_and_total_value()
    if money_added < selected_item['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        refund = round(money_added - selected_item['cost'], 2)
        # Print change if necessary
        if refund > 0:
            print(f"Here is ${refund} in change.")
        return True

# If funds & resources checks pass, make coffee (subtract resources, add money, notify user)
def update_resources_and_profit(selected_item):
    """Takes a dictionary item with this format.
    [item_name]: {
        'ingredients': {
            'water': number,
            'milk': number,
            'coffee': number,
        },
        'cost': number
    }
    Updates resources values subtracting ingredients. Updates profit adding cost."""
    global profit
    for key in selected_item['ingredients']:
        resources[key] -= selected_item['ingredients'][key]
    profit += selected_item['cost']

def run_coffee_machine():
    choice = get_user_selection()
    item = None
    if choice == 'report':
        print_report()
    elif choice == 'off':
        turn_off()
    else:
        try:
            item = get_menu_item(choice)
        except KeyError:
            print("That's not a valid selection. Try again.")
            item = get_menu_item(get_user_selection())

    if item:
        has_enough_resources = check_resources(item)
        if has_enough_resources:
            has_enough_money = check_funds(item)
            if has_enough_money:
                update_resources_and_profit(item)
                print("Here is your espresso ☕️. Enjoy!")
    run_coffee_machine()

run_coffee_machine()