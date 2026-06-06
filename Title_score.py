import turtle

turtle.colormode(255)
class Title(turtle.Turtle):
    def __init__(self,position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color((255,255,255))
        self.goto(position)
        self.score = -1
        self.update()

    def update(self):
        self.clear()
        self.score += 1
        self.write(f'{self.score}', align='center', font=("Courier New", 45, "normal"))
