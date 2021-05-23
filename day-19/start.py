import turtle as turtle_module

tim = turtle_module.Turtle()
screen = turtle_module.Screen()


def move_forwards():
    tim.forward(10)


def up():
    tim.setheading(90)


def down():
    tim.setheading(270)


def left():
    tim.setheading(180)


def right():
    tim.setheading(0)


def clear():
    tim.clear()
    tim.penup()
    tim.home()

screen.listen()
screen.onkey(key='space', fun=move_forwards)
screen.onkey(key='Up', fun=up)
screen.onkey(key='Down', fun=down)
screen.onkey(key='Left', fun=left)
screen.onkey(key='Right', fun=right)
screen.onkey(key='c', fun=clear)
screen.exitonclick()