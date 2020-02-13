# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 18:54:55 2020

@author: Swathi
"""

import turtle
import math
import random
import tkinter as TK

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Ball0on Shooting Challenge")


'''Variable Declarations - used through the code'''
#balloon direction - up =1 and down =-1 
balloon_direction=1
#Player speed 
playerspeed = 15
#balloon speed
balloonspeed = 1
#bullet speed - as per the specs
bulletspeed=1.5*balloonspeed
#to count the number of shots to give the missed shots in the end
num_of_shots=0
#bulletfired=0 - Bullet is ready to be fired, bulletfired=1 - bulled is fired
bulletfired=0



'''Different turtle objects declarations and specifications'''

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()	


#Create the player turtle
player = turtle.Turtle()
player.color("white")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(250,0)
player.setheading(180)


#Create the balloon
balloon = turtle.Turtle()
balloon.color("green")
balloon.shape("circle")
balloon.penup()
balloon.speed(0)
balloon.setposition(-250, -250)

#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(180)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()


'''Different Functions used to control the player's action'''

#Move the player left and right
def move_up():
	y = player.ycor()
	y += playerspeed
	if y > 280:
		y =  280
	player.sety(y)
	
def move_down():
	y = player.ycor()
	y -= playerspeed
	if y <- 280:
		y = -280
	player.sety(y)

#Make the bullet ready until fired
def bullet_ready():
    global bulletfired
    global num_of_shots
    if(bulletfired==0):
        bulletfired=1
        num_of_shots=num_of_shots+1
        x = player.xcor()-10
        y=  player.ycor()
        bullet.setposition(x,y)
        bullet.showturtle()
        
#Fire the bullet when hit with space bar
def bullet_fire():
    global bulletfired
    global bulletspeed
    if(bulletfired==1):
        x=bullet.xcor()
        y=bullet.ycor()
        x=x-bulletspeed
        if(x<-300):
            bulletfired=0
            bullet.hideturtle()
        else:
            bullet.setposition(x,y)
            
'''checks the collision of the bullet with the balloon 
       - the distance calculated is the hypotenuse of the traingle formed between the objects'''
def checkCollision(obj1,obj2):
    distance=math.sqrt(math.pow(obj1.xcor()-obj2.xcor(),2)
    +math.pow(obj1.ycor()-obj2.ycor(),2))
    if(distance < 20 ):
        return True
    else:
        return False
    
    
def draw_score_board():
    
    #Draw a score board
    scoreborder_pen = turtle.Turtle()
    scoreborder_pen.speed(0)
    scoreborder_pen.color("white")
    scoreborder_pen.penup()
    scoreborder_pen.setposition(-90,-90)
    scoreborder_pen.pendown()
    scoreborder_pen.pensize(3)
    scoreborder_pen.forward(360)
    scoreborder_pen.left(90)
    scoreborder_pen.forward(200)
    scoreborder_pen.left(90)
    scoreborder_pen.forward(360)
    scoreborder_pen.left(90)
    scoreborder_pen.forward(200)
    scoreborder_pen.left(90)
    scoreborder_pen.hideturtle()
    
    #Inside of a scrore board
    global num_of_shots
    score_pen = turtle.Turtle()
    score_pen.speed(0)
    score_pen.color("white")
    score_pen.penup()
    score_pen.setposition(-50, 0)
    num_of_shots=num_of_shots-1
    scorestring = "Number of Shots You Missed: %s" %num_of_shots
    score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal")) 
    score_pen.hideturtle() 
def a_check(y):
    balloon.sety(y)
    
    
#Create keyboard bindings
turtle.listen()
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")
turtle.onkey(bullet_ready,"space")

#Game starts

while True:
    y=balloon.ycor()
    if(random.randint(0,200)==1):
        if(balloon_direction==-1):
            balloon_direction=1
        else:
            balloon_direction=-1
    
    y=y+balloonspeed*balloon_direction 
    if(y>280):
        balloon_direction=-1
    if(y<-280):
        balloon_direction=1
    a_check(y)
    bullet_fire()
    if(checkCollision(bullet,balloon)):
        balloon.setposition(-280,-280)
        player.setposition(250,250)
        bullet.hideturtle()
        draw_score_board()
turtle.done()
delay = input("Press enter to finsh.")