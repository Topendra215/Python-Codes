import turtle
import random


screen=turtle.Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make Your Guess",prompt="Which turtle will win the race? Enter a color: ")
colors=["red","orange","yellow","blue","green","purple"]
y=-100
color_position=-1
is_race_on=False

all_turtle=[]
for x in range(0,6):
    y+=25
    color_position+=1
    hari=turtle.Turtle(shape="turtle")
    hari.color(colors[color_position])
    hari.penup()
    hari.goto(-230,y)
    all_turtle.append(hari)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"Hurray you have won the Race. {winning_color} got to the destination at the first")
            else:
                print(f"You lose, {winning_color} won the race")


        rand_dist=random.randint(0,10)
        turtle.forward(rand_dist)
screen.listen()
screen.exitonclick()










