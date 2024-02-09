from turtle import *
import turtle as turtle
import totalscore as totalscore

screen_width = 500
screen_height = 500

screen = turtle.Screen()
screen.setup(screen_width, screen_height)
screen.tracer(0)
screen.bgcolor("black")

name = turtle.Screen()
name.setup(500, 500)
name = turtle.textinput("Name", "Please enter your name")
print(name)

f = open("highscores.txt", "r+")
f.write(str(name))
f.close()



