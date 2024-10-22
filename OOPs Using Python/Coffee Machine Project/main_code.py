
import coffee_maker
import menu
import money_machine


coffee_maker=coffee_maker.CoffeeMaker()
menu=menu.Menu()
money_machine=money_machine.MoneyMachine()
run_machine=True
while run_machine:
    options=menu.get_items()
    user_input=input(f"What would you like? ({options}): ").lower()
    if user_input=="off":
        run_machine=False
    elif user_input=="report":
       coffee_maker.report()
       money_machine.report()

    else:
        drink= menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
