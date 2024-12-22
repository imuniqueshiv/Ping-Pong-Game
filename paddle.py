from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(position)
        self.move_speed = 20
        self.screen = self.getscreen()
        self.moving_up = False
        self.moving_down = False

    # Start moving up
    def go_up(self):
        if not self.moving_up:
            self.moving_up = True
            self.move_up()

    # Start moving down
    def go_down(self):
        if not self.moving_down:
            self.moving_down = True
            self.move_down()

    # Move up continuously
    def move_up(self):
        if self.moving_up:
            new_y = self.ycor() + self.move_speed
            if new_y < self.screen.window_height() // 2 - 50:
                self.goto(self.xcor(), new_y)
            self.screen.ontimer(self.move_up, 50)

    # Move down continuously
    def move_down(self):
        if self.moving_down:
            new_y = self.ycor() - self.move_speed
            if new_y > -self.screen.window_height() // 2 + 50:
                self.goto(self.xcor(), new_y)
            self.screen.ontimer(self.move_down, 50)

    # Stop moving up
    def stop_moving_up(self):
        self.moving_up = False

    # Stop moving down
    def stop_moving_down(self):
        self.moving_down = False