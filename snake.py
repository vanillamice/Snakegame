import random
import tkinter
import turtle
import time
#
TK_SILENCE_DEPRECATION=1
delay = 0.1
score = 0
high_score = 0

#Creating a window screen

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("orange")

#   The width and heigh can be put as user's choice
wn.setup(width=600, height=600)
wn.tracer(0)

# Head of the snake itself
head = turtle.Turtle()
head.shape("arrow")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Food in the game
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0,100)

pen = turtle.Turtle()
pen.speed(10)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 High Score: 0", align="center",font=("candara", 23,"bold"))
