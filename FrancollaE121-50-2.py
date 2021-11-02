"""
PLTW 1.2.1 Project
@author: Ethan Francolla
"""

######Imports######
#Import Turtle library for drawing and display function
import turtle as trtl

#Import Random function to generate random numbers
import random as rand


######Game-Config######
#Spot attribute variables
spot_color = "red"
spot_shape = "circle"
spot_size = 2

#Define score tracking variable and set it to 0
score = 0

#Define font to write on screen
font_setup = ("Times New Roman", 20, "normal")

#Define countdown variables and their attributes
timer = 60 #Initial value for timer, 30 seconds
counter_interval = 1000 #1000 is 1 normal second
time_up = False #Set the timer up variable to false while it is still counting down

#Define grade out of 100, setting it to 0 as the initial value
grade = 0

#Define list of possible colors
colors = ["blue", "red", "yellow", "green", "white", "orange"]

#Define list of possible shape sizes
shape_sizes = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]


######Initialize-Turtle######
#Create and define spot object that can be clicked
spot = trtl.Turtle()
spot.fillcolor(spot_color)
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.speed(0)

#Create and define a turtle to write the score on the screen
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(50, 140)
score_writer.pendown()

#Create and define a turtle to display the time elapsed on screen
counter = trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-120, 140)
counter.pendown()

#Create and define a turtle to give a final grade when the game is over
grader = trtl.Turtle()
grader.hideturtle()
grader.penup()
grader.goto(-27, -140)
grader.pendown()


######Game-Functions######
#Define function to change the color of the spot each time it's clicked
def change_color():
    global spot_color
    spot_color = str(rand.choice(colors))
    spot.fillcolor(spot_color)

#Define a function to change the size of the spot each time it's clicked
def new_shape_size():
    global spot_size
    spot_size = float(rand.choice(shape_sizes))
    spot.shapesize(spot_size)

#Define function with x and y positions for when the spot is clicked
def spot_clicked(x,y):
    #Check if game has finished
    if time_up == False:
        #Call function to change position
        change_position()

        #Call the function to update the score
        update_score()

        #Call the function to change the color of the spot
        change_color()

        #Call function to change the size of the spot
        new_shape_size()

    #End the game and calculate the users grade and display it
    else:
        #Prevent game from being played further by removing the spot
        spot.hideturtle()

        #Grade score
        grade_score()
        grader.write("Grade: " + str(grade), font=font_setup)

#Function to change the position of the spot after it is clicked
def change_position():
    #create random numbers to create a new position for the spot
    new_xpos = rand.randint(-170, 170)
    new_ypos = rand.randint(-110, 110)

    #Move the turtle to the new location
    spot.penup()
    spot.hideturtle()
    spot.goto(new_xpos, new_ypos)
    spot.pendown()
    spot.showturtle()

#Function to update the score tracker variable
def update_score():
    #Increase the score tracker variable by 1 each time the spot is clicked
    global score #Set score to be a global variable so it can be accessed in this function
    score += 1

    #Write new score
    score_writer.clear() #Erase old score
    score_writer.write("Score: " + str(score), font=font_setup)

#Function to update a timer counting down
def countdown():
    global timer, time_up #Define these variables as global variables to access them in other parts of the program
    counter.clear() #Erase old time display before creating a new one

    #Check if time has run out, if not proceed with normal countdown
    if timer <= 0:
        counter.write("Time's Up!", font = font_setup)
        time_up = True
        
    #Proceed to countdown as normal
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)

def grade_score():
    #Set grade based on score
    global grade, score
    if (score > 96.5):
        grade = "A+"
    elif (score > 93.5):
        grade = "A"
    elif (score > 89.5):
        grade = "A-"
    elif (score > 86.5):
        grade = "B+"
    elif (score > 83.5 ):
        grade = "B"
    elif (score > 79.5):
        grade = "B-"
    elif (score > 76.5):
        grade = "C+"
    elif (score > 73.5):
        grade = "C"
    elif (score > 69.5):
        grade = "C-"
    elif (score > 66.5):
        grade = "D+"
    elif (score > 63.5):
        grade = "D"
    elif (score > 59.5):
        grade = "D-"
    else:
        grade = "F"


######Events######
#Define Screen and its attributes
wn = trtl.Screen()
wn.bgcolor("beige")

#Start the game
spot.onclick(spot_clicked)
wn.ontimer(countdown, counter_interval) #Control timer
wn.mainloop()