from turtle import Turtle


class Pong(Turtle):

    def __init__(self, align):

        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        if align == "left":
            self.goto(-380, 0)
        elif align == "right":
            self.goto(380,0)
        self.color("white")

    def up(self):
        y_new = self.ycor() + 20
        x_new = self.xcor()
        self.goto(x_new, y_new)

    def down(self):
        y_new = self.ycor() + -20
        x_new = self.xcor()
        self.goto(x_new, y_new)