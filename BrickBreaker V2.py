from tkinter import Menubutton, mainloop, scrolledtext
from tkinter.tix import Tree
import turtle as trtl
import random
import time

main_screen = trtl.Screen()
main_screen.title("Brick Breaker Game")
main_screen.setup(width = 500, height = 500)
main_screen.bgcolor('black')
main_screen.listen()
title_screen = True

#Close on escape
def close_game():
    main_screen.bye()
main_screen.onkeypress(close_game, "Escape")

livesleft = 3
scoretotal = 0
totalscore = 0
timer = 0
counter_interval = 1000
timer_up = False

middlehits = 0
lefthits = 0
righthits = 0

middlecollision = True
leftcollision = True
rightcollision = True

count_up = True

brick_colors = ["yellow", "red", "black"]


#Initiate title screen
class titleScreen:
    def __init__(title):
        title_font = "karmatic arcade", 24, "normal"
        title = trtl.Turtle()
        title.speed(0)
        title.pensize(3)
        title.shape('square')
        title.color('aqua')
        title.penup()
        title.hideturtle()
        title.goto(0,180)
        title.write("Ultimate Brick", align = "center", font=(title_font))
        title.goto(0,140)
        title.write("Breaker Showdown!!", align = "center", font=(title_font))

        #Box
        title.penup()
        title.pensize(5)
        title.hideturtle()
        title.color('grey')
        title.speed(0)
        title.goto(-175,-65)
        title.pendown()
        title.forward(350)
        title.left(90)
        title.forward(110)
        title.left(90)
        title.forward(350)
        title.left(90)
        title.forward(110)
        title.hideturtle()

        #Enter to play
        title.speed(0)
        title.pensize(3)
        title.shape('square')
        title.color('aqua')
        title.penup()
        title.hideturtle()
        title.goto(-6,0)
        title.write("Press SPACE", align = "center", font=(title_font))
        title.hideturtle()
        title.goto(0,-50)
        title.write("to play", align = "center", font=(title_font))
        trtl.onkeypress(title.clear,"space")

def score_enter():
    global scoretotal, time, timer, totalscore
    totalscore = scoretotal - timer
    print(str(totalscore) + " equals " + str(scoretotal) + " minus " + str(timer))
    score_font = "karmatic arcade", 24, "normal"
    scoretotal = trtl.Turtle()
    scoretotal.speed(0)
    scoretotal.pensize(3)
    scoretotal.shape('square')
    scoretotal.color('indigo')
    scoretotal.penup()
    scoretotal.hideturtle()
    scoretotal.goto(0,100)
    scoretotal.write(("Your score is " + str(totalscore)), align = "center", font=(score_font))

#Enter your name box
def enter_name():
    global totalscore, count_up
    count_up = False   
    name = trtl.Screen()
    name.setup(500, 500)
    name = trtl.textinput("Name", "Please enter your name")
    print(name)

    f = open("highscores.txt", "r+")
    f.write(str(name) + "," + str(totalscore) + "        ")
    f.close()

class gameOver:
    def __init__(gameover):
        gameover = trtl.Turtle()
        gameover.speed(0)
        gameover.pensize(3)
        gameover.shape('square')
        gameover.color('white')
        gameover.penup()
        gameover.hideturtle()
        gameover.goto(0,0)

def game_mechanics():
    global livesleft, scoretotal, middlehits, lefthits, righthits, time, timer_up, count_up
    #Define movement for left
    def playerleft(): 
      x=player.xcor()
      x=x-30
      player.setx(x)
      player.showturtle()
      if  player.xcor()<-90:
          player.setx(-90)
          player.goto(-90,-185)

    #Definte movement for right
    def playerright():
        x=player.xcor()
        x=x+30
        player.setx(x)
        player.showturtle()
        if  player.xcor()>90:
            player.setx(90)
            player.goto(90,-185)

    #Ball
    ball = trtl.Turtle()
    ball.shape('circle')
    ball.color('limegreen')
    ball.penup()
    ball.goto(0,-60)
    ball.speed(0)
    ball.dx = 6 + random.randint(-2,2)
    ball.dy = 6 + random.randint(-2,2)

    #Time setup
    counter = trtl.Turtle()
    counter.hideturtle()
    counter.pu()
    counter.goto(0,120)
    counter.color("white")
    font_setup = ('karmatic arcade', 12, 'normal')

    #Start time and clear
    def countup():
        global timer, timer_up, count_up
        if count_up == False:
            counter.clear()
            print("this is the time:" + str(timer))
        else:
            counter.clear()
            counter.write("Time:" + str(timer), align = "center", font=font_setup)
            timer += 1
            counter.getscreen().ontimer(countup, counter_interval)
    
    while count_up == True:
        global timer
        countup()
        break

    #Border
    border = trtl.Turtle()
    border.penup()
    border.pensize(5)
    border.hideturtle()
    border.speed(0)
    border.goto(-150,-200)
    border.pendown()
    border.color('red')
    border.goto(150,-200)
    border.left(90)
    border.color('grey')
    turn = 0
    while turn < 3:
        border.forward(300)
        border.left(90)
        turn = turn + 1

    #Score  
    score_font = "karmatic arcade", 18, "normal"
    score = trtl.Turtle()
    score.speed(0)
    score.pensize(2)
    score.shape('square')
    score.color('white')
    score.penup()
    score.hideturtle()
    score.goto(0,150)
    score.write("Score : " + str(scoretotal), align = "center", font=(score_font))

    if scoretotal == 180:
        score.hideturtle()
        score.isvisible()

    #Player 
    player = trtl.Turtle()
    player.speed(0)
    player.shape('square')
    player.color('blue')
    player.shapesize(stretch_wid=0.5, stretch_len=5)
    player.penup()
    player.goto(0,-185)
    player.hideturtle()
    
    #Lives
    lives_font = "karmatic arcade", 20, "normal"
    lives = trtl.Turtle()
    lives.speed(0)
    lives.pensize(3)
    lives.shape('square')
    lives.color('white')
    lives.penup()
    lives.hideturtle()
    lives.goto(0,190)
    lives.write(("Lives left: 3"), align = "center", font=(lives_font))
    

    start_brick_color = "limegreen"
    middle = trtl.Turtle()
    middle.speed(0)
    middle.shape('square')
    middle.color(start_brick_color)
    middle.shapesize(stretch_wid=1, stretch_len=4)
    middle.penup()
    middle.goto(0,0)

    left = trtl.Turtle()
    left.speed(0)
    left.shape('square')
    left.color(start_brick_color)
    left.shapesize(stretch_wid=1, stretch_len=4)
    left.penup()
    left.goto(-70,60)

    right = trtl.Turtle()
    right.speed(0)
    right.shape('square')
    right.color(start_brick_color)
    right.shapesize(stretch_wid=1, stretch_len=4)
    right.penup()
    right.goto(70,60)   

    trtl.onkeypress(playerleft, "a")
    trtl.onkeypress(playerright, "d")
    
    global middlecollision
    global leftcollision
    global rightcollision

    gamemovement = True
    
    def score_writer():
        score.clear()
        score.write("Score: " + str(scoretotal), align = "center", font=(score_font))

    while gamemovement == True:
            #Ball movement
            ball.setx(ball.xcor()+ball.dx)
            ball.sety(ball.ycor()+ball.dy)

            #Side border right
            if ball.xcor()>140:
                ball.setx(139)
                ball.dx = 6
                ball.dx = ball.dx * -1 + random.randint(1,2) 
                
            #Side Border left
            if ball.xcor()<-140:
                ball.setx(-139)
                ball.dx = -6
                ball.dx = ball.dx * -1 + random.randint(1,2)
                
            #Top Border
            if ball.ycor()>90:
                ball.sety(89)
                ball.dy = 6
                ball.dy = ball.dy * -1 + random.randint(1,2) 

                #Bottom border
        
        #Bottom Border Collision
            if ball.ycor()<-200:
                ball.goto(0,-60)
                ball.dy = ball.dy * -1 + random.randint(1,2)
                #Reset ball speed
                ball.dy = 6
                ball.dx = 6
                
                #Lives Counter
                livesleft = livesleft - 1
                lives.write("Lives left: " + str(livesleft), align = "center", font=("karmatic arcade", 20, "normal"))
                lives.clear()
                lives.write("Lives left: " + str(livesleft), align = "center", font=("karmatic arcade", 20, "normal"))
        
            #Player-ball collision
            if (ball.ycor()>-190) and (ball.ycor()<-170) and ball.xcor()<player.xcor()+50 and ball.xcor()>player.xcor()-50:
                ball.sety(-168)
                ball.dy = ball.dy * -1
            
            #Collision for middle bottom
            if middlecollision == True:
                if (ball.ycor()>-15) and (ball.ycor()<-5) and (ball.xcor()>-40) and (ball.xcor()<40):
                    print(middlehits)
                    middlehits = middlehits + 1
                    ball.sety(-18)
                    ball.dy = ball.dy * -1 
                    if middlehits == 1:
                        scoretotal = scoretotal + 10
                        score_writer()
                        middle.color(str(brick_colors[0]))
                    if middlehits == 2:
                        scoretotal = scoretotal + 20
                        score_writer()
                        middle.color(str(brick_colors[1]))
                    if middlehits >= 3:
                        scoretotal = scoretotal + 30
                        score_writer()
                        middle.color(str(brick_colors[2]))
                        middlecollision = False
                                
            #Collision for middle top    
            if middlecollision == True:
                if (ball.ycor()>5) and (ball.ycor()<15) and (ball.xcor()>-40) and (ball.xcor()<40):
                    print(middlehits)
                    middlehits = middlehits + 1
                    ball.sety(18)
                    ball.dy = ball.dy * -1
                    if middlehits == 1:
                        scoretotal = scoretotal + 10
                        score_writer()
                        middle.color(str(brick_colors[0]))
                    if middlehits == 2:
                        scoretotal = scoretotal + 20
                        score_writer()
                        middle.color(str(brick_colors[1]))
                    if middlehits >= 3:
                        scoretotal = scoretotal + 30
                        score_writer()
                        middle.color(str(brick_colors[2]))
                        middlecollision = False
            
            #Collision for middle left
            if middlecollision == True:
                if (ball.ycor()>-13) and (ball.ycor()<13) and (ball.xcor()>-45) and (ball.xcor()<-41):
                    print(middlehits)
                    middlehits = middlehits + 1
                    ball.setx(-48)
                    ball.dx = ball.dx * -1 
                    if middlehits == 1:
                        scoretotal = scoretotal + 10
                        score_writer()
                        middle.color(str(brick_colors[0]))
                    if middlehits == 2:
                        scoretotal = scoretotal + 20
                        score_writer()
                        middle.color(str(brick_colors[1]))
                    if middlehits >= 3:
                        scoretotal = scoretotal + 30
                        score_writer()
                        middle.color(str(brick_colors[2]))
                        middlecollision = False

            #Collision for middle right
            if middlecollision == True:
                if (ball.ycor()>-13) and (ball.ycor()<13) and (ball.xcor()>41) and (ball.xcor()<45):
                    print(middlehits)
                    middlehits = middlehits + 1
                    ball.setx(48)
                    ball.dx = ball.dx * -1 
                    if middlehits == 1:
                        scoretotal = scoretotal + 10
                        score_writer()
                        middle.color(str(brick_colors[0]))
                    if middlehits == 2:
                        scoretotal = scoretotal + 20
                        score_writer()
                        middle.color(str(brick_colors[1]))
                    if middlehits >= 3:
                        scoretotal = scoretotal + 30
                        score_writer()
                        middle.color(str(brick_colors[2]))
                        middlecollision = False

            #Collision for left bottom
            if leftcollision == True:
                if (ball.ycor()>45) and (ball.ycor()<55) and (ball.xcor()>-110) and (ball.xcor()<-30):
                    print(lefthits)
                    lefthits = lefthits + 1
                    ball.sety(42)
                    ball.dy = ball.dy * -1 
                    if lefthits == 1:
                        scoretotal = scoretotal + 10
                        score_writer()
                        left.color(str(brick_colors[0]))
                    if lefthits == 2:
                        scoretotal = scoretotal + 20
                        score_writer()
                        left.color(str(brick_colors[1]))
                    if lefthits >= 3:
                        scoretotal = scoretotal + 30
                        score_writer()
                        left.color(str(brick_colors[2]))
                        leftcollision = False

            #Collision for left top
            if leftcollision == True:
                if (ball.ycor()>63) and (ball.ycor()<71) and (ball.xcor()>-110) and (ball.xcor()<-30):
                    print(lefthits)
                    lefthits = lefthits + 1
                    ball.sety(74)
                    ball.dy = ball.dy * -1
                    if lefthits == 1:
                        scoretotal = scoretotal + 10
                        score_writer()
                        left.color(str(brick_colors[0]))
                    if lefthits == 2:
                        scoretotal = scoretotal + 20
                        score_writer()
                        left.color(str(brick_colors[1]))
                    if lefthits >= 3:
                        scoretotal = scoretotal + 30
                        score_writer()
                        left.color(str(brick_colors[2]))
                        leftcollision = False

            #Collision for left left
            if leftcollision == True:
                if (ball.ycor()>43) and (ball.ycor()<63) and (ball.xcor()>-115) and (ball.xcor()<-111):
                    print(lefthits)
                    lefthits = lefthits + 1
                    ball.setx(-118)
                    ball.dx = ball.dx * -1
                    if lefthits == 1:
                        scoretotal = scoretotal + 10
                        score_writer()
                        left.color(str(brick_colors[0]))
                    if lefthits == 2:
                        scoretotal = scoretotal + 20
                        score_writer()
                        left.color(str(brick_colors[1]))
                    if lefthits >= 3:
                        scoretotal = scoretotal + 30
                        score_writer()
                        left.color(str(brick_colors[2]))
                        leftcollision = False

            #Collision for left right
            if leftcollision == True:
                if (ball.ycor()>43) and (ball.ycor()<63) and (ball.xcor()>-29) and (ball.xcor()<-25):
                    print(lefthits)
                    lefthits = lefthits + 1
                    ball.setx(-22)
                    ball.dx = ball.dx * -1
                    if lefthits == 1:
                        scoretotal = scoretotal + 10
                        score_writer()
                        left.color(str(brick_colors[0]))
                    if lefthits == 2:
                        scoretotal = scoretotal + 20
                        score_writer()
                        left.color(str(brick_colors[1]))
                    if lefthits >= 3:
                        scoretotal = scoretotal + 30
                        score_writer()
                        left.color(str(brick_colors[2]))
                        leftcollision = False    

            if rightcollision == True:
                if (ball.ycor()>45) and (ball.ycor()<55) and (ball.xcor()>30) and (ball.xcor()<110):
                    print(righthits)
                    righthits = righthits + 1
                    ball.sety(42)
                    ball.dy = ball.dy * -1
                    if righthits == 1:
                        scoretotal = scoretotal + 10
                        score.clear()
                        score_writer()
                        right.color(str(brick_colors[0]))
                    if righthits == 2:
                        scoretotal = scoretotal + 20
                        score.clear()
                        score_writer()
                        right.color(str(brick_colors[1]))
                    if righthits >= 3:
                        scoretotal = scoretotal + 30
                        score.clear()
                        score_writer()
                        right.color(str(brick_colors[2]))
                        rightcollision = False 
            
            #Collision for right top
            if rightcollision == True:
                if (ball.ycor()>63) and (ball.ycor()<71) and (ball.xcor()>30) and (ball.xcor()<110):
                    print(righthits)
                    righthits = righthits + 1
                    ball.sety(74)
                    ball.dy = ball.dy * -1 
                    if righthits == 1:
                        scoretotal = scoretotal + 10
                        score_writer()
                        right.color(str(brick_colors[0]))
                    if righthits == 2:
                        scoretotal = scoretotal + 20
                        score_writer()
                        right.color(str(brick_colors[1]))
                    if righthits >= 3:
                        scoretotal = scoretotal + 30
                        score_writer()
                        right.color(str(brick_colors[2]))
                        rightcollision = False
            
            #Collision for right left
            if rightcollision == True:
                if (ball.ycor()>43) and (ball.ycor()<63) and (ball.xcor()>25) and (ball.xcor()<29):
                    print(righthits)
                    righthits = righthits + 1
                    ball.setx(22)
                    ball.dx = ball.dx * -1 
                    if righthits == 1:
                        scoretotal = scoretotal + 10
                        score_writer()
                        right.color(str(brick_colors[0]))
                    if righthits == 2:
                        scoretotal = scoretotal + 20
                        score_writer()
                        right.color(str(brick_colors[1]))
                    if righthits >= 3:
                        scoretotal = scoretotal + 30
                        score_writer()
                        right.color(str(brick_colors[2]))
                        rightcollision = False

            #Collision for right right
            if rightcollision == True:
                if (ball.ycor()>43) and (ball.ycor()<63) and (ball.xcor()>115) and (ball.xcor()<111):
                    print(righthits)
                    righthits = righthits + 1
                    ball.setx(118)
                    ball.dx = ball.dx * -1 
                    if righthits == 1:
                        scoretotal = scoretotal + 10
                        score_writer()
                        right.color(str(brick_colors[0]))
                    if righthits == 2:
                        scoretotal = scoretotal + 20
                        score_writer()
                        right.color(str(brick_colors[1]))
                    if righthits >= 3:
                        scoretotal = scoretotal + 30
                        score_writer()
                        right.color(str(brick_colors[2]))
                        rightcollision = False

            #Detect when all bricks are broken and stop the player and ball
            if (rightcollision == False) and (leftcollision == False) and (middlecollision == False):
                gamemovement = False

            #Detect when score reaches 180 (max score) and remove the score, lives, and border
            if scoretotal == 180:
                score.undo()
                lives.undo()
                border.undo()
                ball.hideturtle()
                ball.isvisible()
                ball.dx = 0
                ball.dy = 0
                player.hideturtle()
                player.isvisible()
                borderturn = 0
                while borderturn < 10:
                    border.undo()
                    borderturn = borderturn + 1
                score_enter()
                enter_name()
                close_game()
                count_up = False
                
                
            #Game over at zero lives
            if livesleft == 0:  
                gamemovement = False   
                score.undo()
                lives.undo()
                border.undo()
                middle.hideturtle()
                middle.isvisible()
                left.hideturtle()
                left.isvisible()
                right.hideturtle()
                right.isvisible()
                ball.hideturtle()
                ball.isvisible()
                ball.dx = 0
                ball.dy = 0
                player.hideturtle()
                player.isvisible()
                count_up = False
                borderturn = 0
                while borderturn < 10:
                    border.undo()
                    borderturn = borderturn + 1
                    print(str(scoretotal)) 
                score_enter()
                enter_name()
                close_game()
                
    
    #When game is over do this
    if gamemovement == False:
        ball.hideturtle()
        ball.isvisible()
        ball.dx = 0
        ball.dy = 0
        player.hideturtle()
        player.isvisible()
        score.hideturtle()
        score.isvisible()
        count_up = False
        

#Launch the title screen once
while title_screen == True:
    titleScreen()
    #Exit game
    escape_font = "arial", 10, "normal"
    escape = trtl.Turtle()
    escape.speed(0)
    escape.color('white')
    escape.penup()
    escape.hideturtle()
    escape.goto(-240,-240)
    escape.write(("Press 'esc' at any time to close the game"), font=(escape_font))
    break

#Start the game
def start_game():
    game_mechanics()

    
trtl.onkeyrelease(start_game,"space")            
trtl.mainloop()