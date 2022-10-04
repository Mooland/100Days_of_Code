

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
    "money" : 0
}

coins={"Penny" : 0.01,
"Nickel":0.05,
"Dime":0.10,
"Quarter":0.25}



def coin_ask():
    pennies = int(input("How much Penny do you have?: "))
    nickels = int(input("How much Nickels do you have?: "))
    dimes = int(input("How much Dimes do you have?: "))
    quarters = int(input("How much Quarters do you have?: "))
    totall_check=(pennies*coins["Penny"]) + (nickels*coins["Nickel"])+ (dimes*coins["Dime"]) + (quarters*coins["Quarter"])
    return totall_check

def coffee_maker(ordered):
    if ordered=='latte' or ordered=="cappuccino":
        resources["coffee"]-=MENU[ordered]["ingredients"]["coffee"]
        resources["water"]-=MENU[ordered]["ingredients"]["water"]
        resources["milk"]-=MENU[ordered]["ingredients"]["milk"]
        resources["money"]+=MENU[ordered]['cost']
    elif ordered=='espresso':
        resources["coffee"]-=MENU[ordered]["ingredients"]["coffee"]
        resources["water"]-=MENU[ordered]["ingredients"]["water"]
        resources["money"]+=MENU[ordered]['cost']
    
   


def coffee_machine():
    order=input("What would you like? (espresso/latte/cappuccino): ")
    
    if order=="report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney:${resources['money']}")
    else:
        if resources["coffee"]<MENU[order]["ingredients"]["coffee"]:
            print("Not enough coffee")
        elif resources["water"]<MENU[order]["ingredients"]["water"]:
            print("Sorry there is not enough water")
        elif order!="espresso" and resources["milk"]<MENU[order]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
        else:   
            print("Please insert coins")
            money_inside=coin_ask()
            if money_inside>=MENU[order]['cost']:
                coffee_maker(order)
                print(f"Here is ${round(money_inside-MENU[order]['cost'],2)} in change")
                print(f"Here is your {order}. Enjoy!")
            else:
                print("Thats not enough money.")
    coffee_machine()
coffee_machine()
