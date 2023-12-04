from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

#TODO: First of all we need to create objects from Screen and Turtle classes and set up the screen size,
# make background color black user tracer() function to make movement smooth

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# This lines of codes is for to manage the movement of the snake there are methods in the Snake() class
#screen.listen() function is for to take order from user and onkey() function is responsible for key
snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.dawn, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#TODO: game body should be created with while loop because we don't know how long is this game continue.
# Inside the while loop we can make movement of segments by user object from the class
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        is_game_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

























screen.exitonclick()