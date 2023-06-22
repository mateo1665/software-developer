import turtle
import os

#de setup voor de game
wn = turtle.Screen()
wn.title("pong van mateo")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# de score
score_a = 0
score_b = 0
# reket A
reket_a = turtle.Turtle()
reket_a.speed(0)
reket_a.shape("square")
reket_a.color("white")
reket_a.shapesize(stretch_wid=5, stretch_len=1)
reket_a.penup()
reket_a.goto(-350,0)

# reket B
reket_b = turtle.Turtle()
reket_b.speed(0)
reket_b.shape("square")
reket_b.color("white")
reket_b.shapesize(stretch_wid=5,stretch_len=1)
reket_b.penup()
reket_b.goto(350, 0)

# de bal
bal = turtle.Turtle()
bal.speed(0)
bal.shape("square")
bal.color("white")
bal.penup()
bal.goto(0, 0)
bal.dx = 0.10
bal.dy = 0.10

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# de functions

def paddle_a_up():
    y = reket_a.ycor()
    y += 20
    reket_a.sety(y)

def paddle_a_down():
    y = reket_a.ycor()
    y -= 20
    reket_a.sety(y)

def paddle_b_up():
    y = reket_b.ycor()
    y += 20
    reket_b.sety(y)

def paddle_b_down():
    y = reket_b.ycor()
    y -= 20
    reket_b.sety(y)

# de keybord settings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# de game loop
while True:
    wn.update()

      # bal laten bewegen
    bal.setx(bal.xcor() + bal.dx)
    bal.sety(bal.ycor() + bal.dy)

# zijkanten checken 

    # de boven en onder kant
    if bal.ycor() > 290:
        bal.sety(290)
        bal.dy *= -1
        os.system("afplay bounce.wav&")
    
    elif bal.ycor() < -290:
        bal.sety(-290)
        bal.dy *= -1
        os.system("afplay bounce.wav&")

    # links en rechts
    if bal.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        bal.goto(0, 0)
        bal.dx *= -1

    elif bal.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        bal.goto(0, 0)
        bal.dx *= -1

    # rekets en bal aanrakingen
    if bal.xcor() < -330 and bal.ycor() < reket_a.ycor() + 10 and bal.ycor() > reket_a.ycor() -  10:
        bal.dx *= -1 
        os.system("afplay bounce.wav&")
    
    elif bal.xcor() > 330 and bal.ycor() < reket_b.ycor() + 10 and bal.ycor() > reket_b.ycor() - 10:
        bal.dx *= -1
        os.system("afplay bounce.wav&")
    
