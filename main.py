from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Ping-Pong")

# Create paddles, ball, and scoreboard
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
scoreboard = Scoreboard()

# Set up key bindings for paddle movement
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeyrelease(r_paddle.stop_moving_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeyrelease(r_paddle.stop_moving_down, "Down")

screen.onkeypress(l_paddle.go_up, "s")
screen.onkeyrelease(l_paddle.stop_moving_up, "s")
screen.onkeypress(l_paddle.go_down, "d")
screen.onkeyrelease(l_paddle.stop_moving_down, "d")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.moving()
    scoreboard.screen_divider()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_l_score()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_r_score()

screen.exitonclick()