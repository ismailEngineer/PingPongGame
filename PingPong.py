# Turtle Graphics Game

import time
import turtle

from pygame import mixer
import pygame

# config fenetre
wn = turtle.Screen()
wn.title("PING-PONG GAME")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# scores
score_1 = 0
score_2 = 0

# config padle 1
padle_1 = turtle.Turtle()
padle_1.speed(0)
padle_1.shape("square")
padle_1.shapesize(stretch_wid=5, stretch_len=1)
padle_1.color("white")
padle_1.penup()
padle_1.goto(-350, 0)

# config padle 2
padle_2 = turtle.Turtle()
padle_2.speed(0)
padle_2.shape("square")
padle_2.shapesize(stretch_wid=5, stretch_len=1)
padle_2.color("white")
padle_2.penup()
padle_2.goto(350, 0)

# config Ball
ball = turtle.Turtle()
ball.speed(0)  # speed of animation
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0, 0)

ball.dx = 2
ball.dy = -2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))


# fonctions
def padle_1_up():
    y = padle_1.ycor()
    y += 20
    padle_1.sety(y)


def padle_1_down():
    y = padle_1.ycor()
    y -= 20
    padle_1.sety(y)


def padle_2_up():
    y = padle_2.ycor()
    y += 20
    padle_2.sety(y)


def padle_2_down():
    y = padle_2.ycor()
    y -= 20
    padle_2.sety(y)


# keyboard
wn.listen()
wn.onkeypress(padle_1_up, "z")
wn.onkeypress(padle_1_down, "s")
wn.onkeypress(padle_2_up, "Up")
wn.onkeypress(padle_2_down, "Down")

# initialisation module pygame
pygame.init()
# initialisation du son
effet_son = mixer.Sound('kick.mp3')

# Boucle principale du jeux
while True:
    time.sleep(0.015)
    wn.update()

    # Déplacement de la balle
    ball.setx(ball.xcor() + ball.dx)

    ball.sety(ball.ycor() + ball.dy)

    # Vérification des bordure
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < padle_2.ycor() + 40 and ball.ycor() > padle_2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        # lancer un effet sonore
        effet_son.play()

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < padle_1.ycor() + 40 and ball.ycor() > padle_1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        # lancer un effet sonore
        effet_son.play()
