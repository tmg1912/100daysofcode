import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
is_game_on = True

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while is_game_on:
    time.sleep(0.1)
    snake.move()
    screen.update()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        score.game_over()

    # detect collision with tail
    # if head collides with any segment in the tail:
    # trigger game over
    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()