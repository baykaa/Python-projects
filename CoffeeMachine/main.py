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

# TODO 1. Print report of resources

print("RESOURCES:")
for items in resources:
    print(f"{items}: {resources[items]}")

# TODO 2. Check resources

order = input("What would you like? (espresso/latte/cappuccino): ")
menu = ["espresso", "latte", "cappuccino"]
#
# def resource_checker(order_name):
#     if order == order_name:
sufficient = True

if order in menu:
    if order == "espresso":
        for menu_item in MENU["espresso"]["ingredients"]:
            if menu_item in resources:
                resources[menu_item] - MENU["espresso"]["ingredients"][menu_item]
            a = MENU["espresso"]["ingredients"].get(menu_item)
            if resources["water"] - a < 0:
                sufficient = False
            elif resources["milk"] - a < 0:
                sufficient = False
            elif resources["coffee"] - a < 0:
                sufficient = False

            print(menu_item , a)
            # return sufficient

# TODO 3. Process coins
# TODO 4. Check transaction successful?
# TODO 5. Make coffee