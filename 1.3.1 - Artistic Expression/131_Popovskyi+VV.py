import turtle as trtl
import random as randit


wn = trtl.Screen()
wn.bgcolor("blue")

#MILESTONE 1: Ask name and age
name = trtl.textinput("Your name", "What is your name?")
age = trtl.textinput("Your age", "How old are you (num only)?")

#wn.addshape("square++", (-12,12), (-12,-12), (12,-12), (12,12))

letter_open = ""
while letter_open != "y" or "n":
    letter_open = trtl.textinput("You got a letter!", "Do you want see it (y/n)?")
    if letter_open == "y":
        break
    if letter_open == "n":
        break
    
if letter_open == "y":
    letter_draw = trtl.Turtle()
    letter_draw.hideturtle()
    letter_draw.speed("fastest")
    letter_draw.penup()
    letter_draw.goto(-150,-200)
    letter_draw.pendown()
    letter_draw.left(90)
    letter_color = "#e5b064"
    letter_draw.fillcolor(letter_color)
    letter_draw.begin_fill()
    for i in range(4):
        if i%2 == 0:
            letter_draw.forward(200)
            letter_draw.right(90)

        if i%2 == 1:
            letter_draw.forward(300)
            letter_draw.right(90)

    letter_draw.end_fill()

    #triangle up
    letter_center = -100
    letter_draw.pendown()
    letter_draw.goto(-150,0)
    letter_draw.goto(-35,letter_center)
    letter_draw.goto(35,letter_center)
    letter_draw.goto(150,0)

    #triangle down
    letter_draw.goto(150,-200)
    letter_draw.goto(35,letter_center)
    letter_draw.goto(-35,letter_center)
    letter_draw.goto(-150,-200)

    #color the letter
    letter_color = "#e5b064"
    letter_draw.fillcolor(letter_color)
    letter_draw.penup()
    letter_draw.goto(-50,letter_center)
    letter_draw.pendown()
    letter_draw.begin_fill()

    letter = trtl.Turtle()
    letter.shape("square")
    letter.shapesize(10)
    letter.color("white")

wn.mainloop()
        
