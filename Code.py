from turtle import Screen,Turtle
from snake import Snake
from Food import Food
from ScoreBoard import ScoreBoard
import time
screen = Screen()

screen.setup(height = 600,width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreBoard = ScoreBoard()
screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.left,"a")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        scoreBoard.refresh()
        
    if( snake.head.xcor() > 280 or snake.head.xcor()< -280 or snake.head.ycor()>280 or snake.head.ycor()<-280):
        scoreBoard.gameover()
        game_is_on = False
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on = False
            scoreBoard.gameover()
        
    
screen.exitonclick()