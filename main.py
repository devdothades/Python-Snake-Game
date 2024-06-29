from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# BOARD WIDTH AND HEIGHT
WIDTH = 900
HEIGHT = 900
COLOR = "black"

# CONTROLS
UP = "w"
DOWN = "s"
LEFT = "a"
RIGHT = "d"

tk = Turtle()
screen = Screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(COLOR)
screen.title('Snake Game')
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, UP)
screen.onkey(snake.down, DOWN)
screen.onkey(snake.left, LEFT)
screen.onkey(snake.right, RIGHT)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    if snake.head.xcor() > 450 or snake.head.xcor() < -450 or snake.head.ycor() > 450 or snake.head.ycor() < -450:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
