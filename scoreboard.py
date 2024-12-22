from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    # Draw the screen divider
    def screen_divider(self):
        self.goto(0, 300)
        self.setheading(270)
        self.pendown()
        for _ in range(30):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
        self.penup()
        self.hideturtle()

    # Update the scoreboard
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    # Increase left paddle score
    def increase_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    # Increase right paddle score
    def increase_r_score(self):
        self.r_score += 1
        self.update_scoreboard()