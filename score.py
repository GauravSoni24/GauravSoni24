from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.color('White')
        self.show_score()

    def show_score(self):
        self.write(f"                          Score : {self.score}                            ",
                   align='center', font=('Courier', 20, 'underline' and 'bold'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=('Courier', 40, 'bold'))