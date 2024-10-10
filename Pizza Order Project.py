print("Welcome to Python Pizza Deliveries!")
bill=0
size = input("What size pizza do you want? S for small, M for medium or L for large: ")
if size=="S":
    bill=15
elif size=="M":
    bill=20
elif  size=="L":
    bill=25


pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni=="Y":
    if size=="S"or size=="s":
        bill+=2
elif size=="M"or size=="m":
    bill+=3
elif size=="L" or size=="m":
    bill += 3
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese=="Y":
    bill+=1
    print("The Total Bill is","$",bill)


