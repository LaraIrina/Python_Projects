from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_is_on = True

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0) # zero to turn off the animation

scoreboard = Scoreboard() 
#### Create paddle on right side####
right_paddle = Paddle((350,0))
left_paddle = Paddle((-350, 0))

#### Create the ball ####
ball = Ball()

#### Control the paddle ####
screen.listen()
# move right paddle
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(right_paddle.go_left, "Left")
screen.onkey(right_paddle.go_right, "Right")
# move left paddle
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(left_paddle.go_left, "a")
screen.onkey(left_paddle.go_right, "d")


#### Update the screen ####
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collison with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collison with paddles
    if ball.distance(right_paddle) < 50 and right_paddle.xcor() > 320 or ball.distance(left_paddle) < 50 and left_paddle.xcor() < -320:
        ball.bounce_x() 
    # Detect if right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # Detect if left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()