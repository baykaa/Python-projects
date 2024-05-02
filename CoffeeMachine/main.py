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
}


# TODO 2. Check resources

menu = ["espresso", "latte", "cappuccino"]

#
def resource_checker(order_name):
    sufficient = True
    item_ingredient = MENU[order_name]["ingredients"]
    if ((resources["water"] > item_ingredient["water"] and resources["coffee"] > item_ingredient["coffee"])
            or resources["milk"] > item_ingredient["milk"]):
        return sufficient
    else:
        sufficient = False
        return sufficient

def input_checker(input):
    if input in MENU:
        return True
    else:
        return False
# TODO 3. Process coins
def process_coin():
    penny = int(input("Penny: ")) / 100
    nickle = int(input("nickle: ")) * 5 / 100
    dime = int(input("dime: ")) / 10
    quarter = int(input("quarter: ")) / 4
    total_user_coin = penny + dime + nickle + quarter
    return total_user_coin

# TODO 4. Check transaction successful?
def check_transaction(order_name, user_coin):
    item_cost = MENU[order_name]["cost"]
    if user_coin < item_cost:
        return False
    else:
        change = round(user_coin - item_cost, 2)
        return change

# TODO 5. Make coffee
def make_coffee(order_name):
    item_ingredient = MENU[order_name]["ingredients"]
    resources["water"] -= item_ingredient["water"]
    resources["coffee"] -= item_ingredient["coffee"]
    if order_name != "espresso":
        resources["milk"] -= item_ingredient["milk"]
    return "Here is your coffee: ☕"

shop_open = True

while shop_open:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "espresso" or order == "latte" or order == "cappuccino":
        # TODO 1. Print report of resources
        print("RESOURCES:")
        for items in resources:
            print(f"{items}: {resources[items]}")

        if resource_checker(order):
            total_user_coin = process_coin()
            if check_transaction(order, total_user_coin):
                change = check_transaction(order, total_user_coin)
                print(make_coffee(order))
                print(f"Here is your change: {change}")
            else:
                print("Sorry, you money is not enough! Please try again")
        else:
            print("Sorry, our resource is finished we are closed!")
            shop_open = False
    else:
        print("Sorry, we don't have that in our menu. Try again!")

