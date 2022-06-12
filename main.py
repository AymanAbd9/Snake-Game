from turtle import Screen
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collisison with the food
    if snake.head.distance(food) < 15:
        snake.extend()
        scoreboard.increase_score()
        food.refresh()

    # Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collsion head with body 
    for square in snake.squares[1:]: # Exclude the head in the list (squares[0])
        if snake.head.distance(square) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.mainloop()
