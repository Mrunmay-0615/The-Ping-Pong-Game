from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Verdana", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.color("white")
        self.draw_separation()
        self.goto(0, 275)

        self.update_scoreboard()

    def draw_separation(self):
        self.penup()
        self.goto(0, 290)
        self.setheading(270)
        self.pendown()
        for i in range(15):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()

        self.penup()
        self.goto(0, 275)

    def update_scoreboard(self):
        self.clear()
        self.draw_separation()
        self.write(f"{self.l_score}        {self.r_score}", move=False, font=FONT, align=ALIGNMENT)