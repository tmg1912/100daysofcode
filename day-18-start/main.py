from turtle import Turtle, Screen, colormode
import random

tim = Turtle()

tim.shape("turtle")
tim.color("green")
colormode(255)


def draw_shape(num_of_sides):
    for _ in range(0, num_of_sides):
        tim.forward(100)
        angle = 360/num_of_sides
        tim.right(angle)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


tim.speed('fastest')

# draw shapes with increasing no. of sides
# sides = 3
# while sides <= 10:
#     draw_shape(sides)
#     sides += 1


# random walk
def random_walk(steps):
    tim.pensize(10)
    angles = [0, 90, 180, 270]

    for _ in range(0, steps):
        tim.color(random_colour())
        angle = random.choice(angles)
        tim.setheading(angle)
        tim.forward(30)


# spirograph
def draw_spirograph(gap):
    for _ in range(int(360/gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + gap)


draw_spirograph(3)
screen = Screen()
screen.exitonclick()
