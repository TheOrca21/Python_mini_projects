import turtle
from turtle import Turtle,Screen
import random
colors = ['red', 'blue', 'gold', 'green', 'orange', 'pink']
scr = Screen()
scr.setup(width=500, height=400)
user_bet = scr.textinput(title="aight bet", prompt='win col?:')
y = [-70, -40, -10, 20,50, 80]
all_turtle = []
for i in range(6):
    new_turtle = Turtle()
    new_turtle.speed("fastest")
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-235, y=y[i])
    new_turtle.pendown()
    all_turtle.append(new_turtle)
race_on = False
if user_bet:
    race_on = True
while race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            race_on = False
            winner = turtle.pencolor()
            print(f'Winner:{winner}')
            if winner == user_bet:
                print('You won!')
            else:
                print('you lost!')
        d = random.randint(0, 20)
        turtle.forward(d)
scr.exitonclick()