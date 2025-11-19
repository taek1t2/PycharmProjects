from turtle import Turtle
ALIGNMENT = "center"
FONT = ('courier', 14, 'bold')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as hs:
            self.high_score = (hs.read())
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.ht()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", move=False, align=ALIGNMENT, font= FONT)

    def reset(self):

        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as hs:
                hs.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


    def track_score_after_nom(self):
        self.score += 1
        self.update_scoreboard()










    # def game_over(self):
    #     self.goto(0,0)
    #     self.color("white")
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)