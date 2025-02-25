from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
scoreboard = Scoreboard()
screen.setup(width = 800, height = 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

ball = Ball()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


screen.listen()
screen.onkey(r_paddle.go_up, 'Up') # When using a function as a parameter never give parentheses
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down,'s')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() <- 280:
        # needs to bounce
        ball.bounce()
        
    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    # Detect R paddle misses   
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        
    # Detect L paddle misses
    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.r_point()
        


screen.exitonclick()