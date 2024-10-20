import art
print(art.logo)


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


price=0
again=True
while again:
    user_input=input("What would you like? (espresso/latte/cappuccino): ")
    if user_input=="espresso":
        if MENU['espresso']['ingredients']['water']>resources['water']:
            print("Sorry there is not enough water")
        elif MENU['espresso']['ingredients']['coffee']>resources['coffee']:
            print("Sorry there is not enough Coffee")
        elif resources['water']>= MENU['espresso']['ingredients']['water']and resources['coffee']>=MENU['espresso']['ingredients']['coffee']:
            quarter=int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            price_t = float((0.25 * quarter) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies))
            price = round(price_t, 2)
            if price>=1.5:
                print(f"Here is ${price-1.5} in change.")
                print(f"Here is your {user_input} ☕. Enjoy!")
                price = 1.5
                resources['water'] -= MENU['espresso']['ingredients']['water']
                resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
            else:
                print("Sorry that's not enough money. Money refunded.")

    elif user_input=="latte":
        if MENU['latte']['ingredients']['water']>resources['water']:
            print("Sorry there is not enough water")
        elif MENU['latte']['ingredients']['coffee']>resources['coffee']:
            print("Sorry there is not enough Coffee")
        elif MENU['latte']['ingredients']['milk']>resources['milk']:
            print("Sorry there is not enough Milk")
        elif resources['water']>=MENU['latte']['ingredients']['water'] and resources['coffee']>=MENU['latte']['ingredients']['coffee'] and resources['milk']>=MENU['latte']['ingredients']['milk']:
            quarter = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            price_t = float((0.25 * quarter) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies))
            price = round(price_t, 2)
            if price>=2.5:
                print(f"Here is ${price-2.5} in change.")
                print(f"Here is your {user_input} ☕. Enjoy!")
                price = 2.5
                resources['water'] -= MENU['latte']['ingredients']['water']
                resources['milk'] -= MENU['latte']['ingredients']['milk']
                resources['coffee'] -= MENU['latte']['ingredients']['coffee']
            else:
                print("Sorry that's not enough money. Money refunded.")

    elif user_input=="cappuccino":
        if MENU['cappuccino']['ingredients']['water']>resources['water']:
            print("Sorry there is not enough water")
        elif MENU['cappuccino']['ingredients']['coffee']>resources['coffee']:
            print("Sorry there is not enough Coffee")
        elif MENU['cappuccino']['ingredients']['milk']>resources['milk']:
            print("Sorry there is not enough Milk")
        elif resources['water']>=MENU['cappuccino']['ingredients']['water'] and resources['coffee']>=MENU['cappuccino']['ingredients']['coffee'] and resources['milk']>=MENU['cappuccino']['ingredients']['milk']:
            quarter = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            price_t = float((0.25 * quarter) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies))
            price=round(price_t,2)
            if price>=3:
                print(f"Here is ${price-3} in change.")
                print(f"Here is your {user_input} ☕. Enjoy!")
                price = 3
                resources['water'] -= MENU['cappuccino']['ingredients']['water']
                resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
                resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
            else:
                print("Sorry that's not enough money. Money refunded.")


    elif user_input=="report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney:${price}")
    elif user_input=="off".lower():
        again=False
    else:
        print("Please Enter the Valid input")





