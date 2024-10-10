print(r''' 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
******************************************************************************* ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
Enter=input("Please Enter Which way you wanna go? ")
if  Enter=="Right" or Enter =="right":
    print("Oh gosh you chose the wrong way, you were eaten by monster!")
elif Enter=="Left" or Enter=="left":
    print("Congrats yo hav passed the first step:")
    choice1=input("How do you wanna go to the next step: Enter any one of the given choices:\n1.Wait for the boat\n2.Swim across the lake \n")
    if choice1 =="Swim" or choice1 =="swim":
        print("Opps, Game Over! you were Eaten by a Crocodile!")
    elif choice1=="Wait" or choice1=="wait":
        print("yay, You got your, Boat now you can go safely to the door to the treasure ")
        choice2=input("One of the three door has got treasure in it, choose wisely:\n1. Red\n2. Yellow\n3. Blue\n")
        if choice2=="Yellow" or"yellow":
         print("You found the treasure, you won!")
        elif choice2=="Red"or"red":
            print("You were burnt by the fire, game over!")
        elif choice2=="Blue"or"blue":
            print("you were eaten by beasts, game over!")
        else:
            print("Game Over!")
