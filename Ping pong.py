import turtle
import time
import random
from Dash import DashSystem
from Balling import Ball
from Title_score import Title

screen = turtle.Screen()
turtle.colormode(255)
screen.bgcolor((0, 0, 0))
screen.title('P.O.N.G repaddled')
screen.setup(width=1000, height=500)
screen.tracer(0)
score1 = 0
score2 = 0

dash_sys = DashSystem()
BASE_SPEED = 6
color = ['green','blue','red','yellow','magenta','brown','cyan','grey']
winner = ['Congratulations ;0','good!!! 8-)','You winner :D']
loser = ["You didn't win over there",'Better luck next time!','Train harder!',';(']
commenter1 = ['Wow!','Amazing!','Superb!','Beautiful!','Extraordinary!']
commenter2 = ['Aw...','Too bad.','Ouch!','Yikes!','So uncool!']
RNG1 = [12,13,14,15,16,-10,-11,-12,-13,-14]
RNG2 = [10,11,12,13,14,-10,-11,-12,-13,-14]
front_barrier1 = -460
back_barrier1 = -480
front_barrier2 = 460
back_barrier2 = 480

line = turtle.Turtle()
line.pensize(3)
line.color((255, 255, 255))
line.hideturtle()
line.penup()
line.goto(0, -250)
line.pendown()
for I in range(15):
    line.setheading(90)
    line.forward(20)
    line.penup()
    line.forward(20)
    line.pendown()

title1 = Title((-50,190))
title2 = Title((50,190))

comment = turtle.Turtle()
comment.hideturtle()
comment.penup()
comment.color((255,255,255))
comment.goto(-200,200)
comment_expiration = 0

padel1 = turtle.Turtle()
padel1.goto(-487, 0)
padel1.color((255, 255, 255))
padel1.shape('square')
padel1.shapesize(stretch_len=2.5,stretch_wid=1)
padel1.penup()
padel1.setheading(90)

padel2 = turtle.Turtle()
padel2.goto(480, 0)
padel2.color((255, 255, 255))
padel2.shape('square')
padel2.shapesize(stretch_len=5,stretch_wid=1)
padel2.penup()
padel2.setheading(90)

menu1 = turtle.Turtle()
menu1.hideturtle()
menu1.penup()
menu1.color((255,255,255))

ball = Ball()

move_loop1 = False
move_loop2 = False


def up():
    global move_loop1
    if not move_loop1:
        move_loop1 = True
        moving1()


def stop_up():
    global move_loop1
    move_loop1 = False


def moving1():
    if move_loop1:
        padel1.setheading(90)
        current_speed = dash_sys.get_speed(BASE_SPEED) #This variable will receive the value from the dash class,
        padel1.forward(current_speed) #Before adding it towards the turtle
        screen.ontimer(moving1, 10)


def down():
    global move_loop2
    if not move_loop2:
        move_loop2 = True
        moving2()


def stop_down():
    global move_loop2
    move_loop2 = False


def moving2():
    if move_loop2:
        padel1.setheading(270)
        current_speed = dash_sys.get_speed(BASE_SPEED) #Same goes as this one
        padel1.forward(current_speed)
        screen.ontimer(moving2, 10)


def trigger_dash():
    dash_sys.trigger()

boost = 0
bot_speed = 9
def move_bot():
    global bot_speed
    distance = abs(ball.ycor() - padel2.ycor())

    if distance > 100:
        bot_speed += 5
    elif distance > 20:
        bot_speed = 9
    else:
        bot_speed -= 3

    if boost != 0 and time.time() < boost:
        bot_speed += 8

    if ball.ycor() > padel2.ycor():
        new_y = padel2.ycor() + bot_speed
    else:
        new_y = padel2.ycor() - bot_speed

    padel2.sety(new_y)

    if padel2.ycor() > 200:
        padel2.sety(200)
    elif padel2.ycor() < -200:
        padel2.sety(-200)

screen.listen()
screen.onkeypress(up, 'w')
screen.onkeyrelease(stop_up, 'w')
screen.onkeypress(down, 's')
screen.onkeyrelease(stop_down, 's')

screen.onkeypress(up, 'Up')
screen.onkeyrelease(stop_up, 'Up')
screen.onkeypress(down, 'Down')
screen.onkeyrelease(stop_down, 'Down')

screen.onkeypress(trigger_dash, 'q')

def nothing():
    pass

def draw_menu():
    screen.update()
    menu1.goto(0,100)
    menu1.write('PONG REPADDLED', align='center', font=("Courier New", 45, "bold"))
    menu1.goto(0,-50)
    menu1.write('[press space to play]', align='center', font=("Courier New", 15, "normal"))
    screen.update()

def start_menu():
    menu1.clear()
    screen.onkeypress(nothing, 'space')
    game = True
    global front_barrier1,front_barrier2,back_barrier1,back_barrier2,bot_speed,comment_expiration,boost

    while game:
        screen.update()
        time.sleep(0.05)

        dash_sys.update()
        ball.move()
        ball.barrier()

        if ball.xcor() <= front_barrier1 and ball.xcor() >= back_barrier1:
            if padel1.ycor() - 50 <= ball.ycor() <= padel1.ycor() + 50:
                ball.move_x *= -1
                ball.color(random.choice(color))
                ball.move_x += 1.5
                ball.move_y += 0.5
                bot_speed += 4
                front_barrier1 += 2.5
                back_barrier1 -= 2.5
                ball.setx(front_barrier1 + 1)
                ball.setx(-459)
        if ball.xcor() >= front_barrier2 and ball.xcor() <= back_barrier2:
            if padel2.ycor() - 60 <= ball.ycor() <= padel2.ycor() + 60:
                ball.move_x *= -1
                ball.color(random.choice(color))
                ball.move_x -= 1.5
                ball.move_y -= 0.5
                bot_speed += 4
                front_barrier2 -= 2.5
                back_barrier2 += 2.5
                ball.setx(front_barrier2 - 1)
                ball.setx(459)

        if ball.xcor() >= 500:
            ball.goto(0,0)
            title1.update()
            if title1.score % 3 == 0 and title1.score < 6: #If you don't remember on what the modulo operator does,
                comment.color(random.choice(color))         #It divides the two numbers, and returns the remains from the division
                ball.move_y += 1                            #For example, if 5 were to divide by 4, then it would return 1, instead of the result from the 2 numbers.
                comment.write(f'{random.choice(commenter1)}', align='center', font=("Courier New", 15, "normal"))
                screen.update()
                comment_expiration = time.time() + 1.5 #If you don't know what this variable means, it's that the variable will keep the current timer.
                                                       #For example, if the time.time() is 100, then it would be 101.5, and it would not be counting.
            ball.move_x = random.choice(RNG1)
            ball.move_y = random.choice(RNG2)
            bot_speed += 1
            front_barrier1 = -460
            back_barrier1 = -480
            front_barrier2 = 460
            back_barrier2 = 480
            boost = time.time() + 3

        if ball.xcor() <= -500:
            ball.goto(0,0)
            title2.update()
            comment.color(random.choice(color))
            ball.move_y += 1
            comment.write(f'{random.choice(commenter2)}', align='center', font=("Courier New", 15, "normal"))
            screen.update()
            comment_expiration = time.time() + 1.5

            ball.move_x = random.choice(RNG1)
            ball.move_y = random.choice(RNG2)
            front_barrier1 = -460
            back_barrier1 = -480
            front_barrier2 = 460
            back_barrier2 = 480
            dash_sys.cooldown -= 0.25
            boost = time.time() + 3

        if comment_expiration != 0 and time.time() > comment_expiration: #This statement checks the duration of the text lasts, Before clearing itself.
            comment.clear()
            comment_expiration = 0

        if title1.score == 6:
            timmy = turtle.Turtle()
            timmy.hideturtle()
            timmy.color(random.choice(color))
            timmy.write(f'{random.choice(winner)}', align='center', font=("Courier New", 45, "normal"))
            break

        if title2.score == 3:
            timmy = turtle.Turtle()
            timmy.hideturtle()
            timmy.color(random.choice(color))
            timmy.write(f'{random.choice(loser)}', align='center', font=("Courier New", 45, "normal"))
            break

        move_bot()

draw_menu()
screen.onkeypress(start_menu,'space')

turtle.done()

#this is just a commit change test