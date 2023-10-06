from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("The Sneak Game")
screen.tracer(0)


Snake=Snake()
food=Food()
Scoreboard=Scoreboard()

screen.listen()
screen.onkey(Snake.up, "Up")
screen.onkey(Snake.down, "Down")
screen.onkey(Snake.left, "Left")
screen.onkey(Snake.right, "Right")


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    Snake.move()

    if Snake.head.distance(food)<15:
        food.refresh()
        Snake.extend()
        Scoreboard.increase_score()


    if Snake.head.xcor()>280 or Snake.head.xcor()< -280 or Snake.head.ycor()>280 or Snake.head.ycor()< -280:
        Scoreboard.reset()
        Snake.reset()


    for segments in Snake.segments:
        if segments==Snake.head:
            pass
        elif Snake.head.distance(segments)<10:
            Scoreboard.reset()
            Snake.reset()







screen.exitonclick()