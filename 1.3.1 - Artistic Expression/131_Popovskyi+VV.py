#MILESTONE 1: Ask name and age
import turtle as trtl
import random as randit

wn = trtl.Screen()

name = trtl.textinput("Your name", "What is your name?")
age = trtl.textinput("Your age", "How old are you?")

letter_open = 123123
while letter_open != "y" or "n":
    letter_open = trtl.textinput("You got a letter!", "Do you want see it (y/n)?")

    if letter_open == "y":
        letter_draw = trtl.Turtle()
        letter_draw.speed("fastest")
        letter_draw.penup()
        letter_draw.goto(-150,-200)
        letter_draw.pendown()
        letter_draw.left(90)

        for i in range(4):
            if i%2 == 0:
                letter_draw.forward(200)
                letter_draw.right(90)
            if i%2 == 1:
                letter_draw.forward(300)
                letter_draw.right(90)
        #triangle up
        letter_center = -100
        letter_draw.pendown()
        letter_draw.goto(-100,0)
        letter_draw.goto(-35,letter_center)
        
        #triangle down
        
            

    elif "n": 
        break
    
    break

wn.mainloop()
        
