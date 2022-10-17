#  Snake Game


from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# creating a object
screen = Screen()

# TODO: create a screen
# setup the screen
screen.setup(width=600, height=600)

# set background color to black
screen.bgcolor("black")

# add title of the screen
screen.title("Snake Game")

# turn off the turtle animation 
screen.tracer(0)

# create snake object
snake = Snake()

# create food object
food = Food()

# create scoreboard object
scoreboard = Scoreboard()

# TODO: control the snake with keypress
# start listen the keypress
screen.listen()

# add arrow keys
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # move the snake
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # TODO: Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_game()
        snake.reset_snake()

    # TODO: Detect collision with tail
    # if head collides with any segment in the tail then trigger game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_game()
            snake.reset_snake()

# exit on click
screen.exitonclick()
