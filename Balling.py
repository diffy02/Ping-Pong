import turtle
import random

color_list = ['green','blue','red','yellow','magenta','brown','cyan','grey']
class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.move_x = 12
        self.move_y = 10

    def move(self):
        ball_x = self.xcor() + self.move_x
        ball_y = self.ycor() + self.move_y
        self.goto(ball_x, ball_y)

    def barrier(self):
        if self.ycor() >= 250 or self.ycor() <= -250:
            self.move_y *= -1
            # self.sety(self.ycor() + self.move_y)
            self.color(random.choice(color_list))