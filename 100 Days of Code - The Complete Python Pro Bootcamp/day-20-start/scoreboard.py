from turtle import Turtle
ALIGNMENT = "center"
FONT = ('courier', 14, 'bold')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.ht()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def track_score_after_nom(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font= FONT)