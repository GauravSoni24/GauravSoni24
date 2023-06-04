import time
from turtle import Screen

from food import Food
from score import Score
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.title('My Snake Game')
screen.bgcolor('black')

snake = Snake()
food = Food()
score = Score()

screen.tracer(n=0)
screen.listen()
screen.onkey(snake.up, key='Up')
screen.onkey(snake.down, key='Down')
screen.onkey(snake.right, key='Right')
screen.onkey(snake.left, key='Left')

while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with Food
    if snake.segments[0].distance(food) < 15:
        print('Collision Occurred, Successful')
        food.refresh()
        score.increase_score()
        snake.add_segment()

    # Detect Collision with Wall.
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -300 or snake.segments[0].ycor() > 270 \
            or snake.segments[0].ycor() < -280:
        score.game_over()
        break

    # Detect Collision with tail
    for segment in snake.segments[2:]:
        if snake.segments[0].distance(segment) < 10:
            snake.stop()
            score.game_over()
            break

screen.exitonclick()