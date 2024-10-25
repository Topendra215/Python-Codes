import turtle
import random


timmy=turtle.Turtle()
turtle.colormode(255)
timmy.speed("fastest")
timmy.hideturtle()
color_list=[(224, 233, 227), (207, 159, 82), (54, 89, 130), (146, 91, 39), (140, 26, 48), (222, 206, 107), (132, 177, 203), (158, 46, 83), (46, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 69), (186, 94, 106), (185, 140, 172), (84, 120, 180), (59, 39, 31), (87, 157, 91), (78, 153, 164), (195, 79, 72), (161, 201, 219), (80, 74, 44), (45, 74, 77), (57, 127, 123), (218, 176, 187), (168, 207, 167), (220, 182, 168)]
x_coord,y_coord=map(int,input("Enter the Coordinate, where to start from (x,y): ").split(","))
dot_gap=int(input("Enter the gap between the dots: "))
length=int(input("Enter the Length of the Canvas: "))
breadth=int(input("Enter the Breadth of the Canvas: "))


def make_dot(position_x,position_y,):
    for x in range(0,breadth):
        timmy.penup()
        timmy.goto(position_x, position_y)
        position_y += dot_gap

        for _ in range(0,length):

            timmy.color(random.choice(color_list))
            timmy.dot(15,random.choice(color_list))
            timmy.penup()
            timmy.forward(dot_gap)

make_dot(x_coord,y_coord)

screen=turtle.Screen()
screen.exitonclick()
