

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

coins={"Penny" : 0.01,
"Nickel":0.05,
"Dime":0.10,
"Quarter":0.25}

money=0

def coin_ask():
    pennies = int(input("How much Penny do you have?: "))
    nickels = int(input("How much Nickels do you have?: "))
    dimes = int(input("How much Dimes do you have?: "))
    quarters = int(input("How much Quarters do you have?: "))
    totall_check=(pennies*coins["Penny"]) + (nickels*coins["Nickel"])+ (dimes*coins["Dime"]) + (quarters*coins["Quarter"])
    return totall_check

def coffee_maker(ordered):
    resources["coffee"]-=MENU[ordered]["ingredients"]["coffee"]
    resources["water"]-=MENU[ordered]["ingredients"]["water"]
    resources["milk"]-=MENU[ordered]["ingredients"]["milk"]
    money+=MENU[ordered]['cost']

    

def coffee_machine():
    
    order=input("What would you like? (espresso/latte/cappuccino): ").lower
    if order=='report':
        print(f"Water: {resources['water']}n\
            Milk: {resources['milk']}n\
            Coffee: {resources['coffee']}n\
            Money:${money}")
    else:
        print("Please insert coins")
        if coin_ask()>=MENU[order]['cost']:
            coffee_maker(order)