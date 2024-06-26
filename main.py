from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# BOARD WIDTH AND HEIGHT
WIDTH = 300
HEIGHT = 300
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
        scoreboard.add_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() < 280:
        scoreboard.game_over()

screen.exitonclick()
