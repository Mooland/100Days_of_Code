from turtle import Turtle, Screen, color
import random


screen = Screen()
screen.setup(width=500,height=400)

user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter the color: ")

colors=['red','orange','yellow','green','blue','purple']

all_turtles = []

step=0
for turtle_index in colors:
    new_turtle=Turtle(shape='turtle')
    new_turtle.color(colors[step])
    new_turtle.pu()
    new_turtle.goto(x=-230,y=(-100+(step*40)))
    all_turtles.append(new_turtle)
    step+=1

if user_bet:
    is_race_on = True

is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The winnier turtle is {winning_color}")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

# def turtle_creator():
#     item=Turtle(shape='turtle')
#     item.color(colors[step])
#     item.pu()
#     item.goto(x=-230,y=(-100+(step*20)))

# red_t = Turtle(shape='turtle')
# red_t.pu()
# red_t.goto(x=-230, y=-100)


# def move_forward():
#     tim.forward(10)

# def move_backward():
#     tim.back(10)

# def move_left():
#     tim.left(360/36)


# def move_right():
#     tim.right(360/36)

# def clear_screen():
#     tim.home()
#     tim.clear()
    

# screen.listen()
# screen.onkeypress(key="w", fun=move_forward)
# screen.onkeypress(key="s", fun=move_backward)
# screen.onkeypress(key="a", fun=move_left)
# screen.onkeypress(key="d", fun=move_right)
# screen.onkey(key='c', fun=clear_screen)
screen.exitonclick()