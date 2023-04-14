from turtle import Turtle
FONT = ("Courier", 24, "normal")
score = 0


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.setposition(-260, 260)
        self.write(f"Score: {self.score}", align="left", font=FONT)
    
    def increase_score(self):
        self.score += 1
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game over 😭", align="center", font=FONT)
        