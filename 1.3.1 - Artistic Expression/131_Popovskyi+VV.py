import turtle as trtl
import random as randit


wn = trtl.Screen()
wn.bgcolor("blue")

#MILESTONE 1: Ask name and age
name = trtl.textinput("Your name", "What is your name?")
name = str(name)
age = trtl.textinput("Your age", "How old are you (num only)?")
font_letter = "Arial", 15, "bold"

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
    letter.penup()
    letter.speed(1)
    letter.shape("square")
    letter.shapesize(13)
    letter.color("white")
    letter.goto(0,150)

    letter_writer = trtl.Turtle()
    letter_writer.speed("fastest")
    letter_writer.hideturtle()
    letter_writer.penup()
    letter_writer.goto(0,180)
    letter_writer.write("Dear " + name + ",\n we hope you are doing well,\n here is a fun game to play.", font=font_letter, align="center")

    play_button = trtl.Turtle()
    play_button.speed("fastest")
    play_button.penup()
    play_button.goto(-55,35)
    play_button.write("Play", font=font_letter, align="center")
    play_button.goto(-55,75)
    play_button.shape("square")
    play_button.shapesize(2)

    close_button = trtl.Turtle()
    close_button.speed("fastest")
    close_button.penup()
    close_button.goto(55,35)
    close_button.write("Close", font=font_letter, align="center")
    close_button.goto(55,75)
    close_button.shape("square")
    close_button.shapesize(2)
    #  game functions

words_list4 = ["BIKE", "BLUE", "RIDE" "FROG", "BALL", "SNOW", "HAND", "FOOT", "FACE", "BIRD", "RAIN", "WORD"]
words_list5 =["APPLE","CHAIR","BREAD","PLANT","LIGHT","HEART","SMILE","TRUCK","TABLE","HOUSE","GRASS","SOLAR"]
words_list6 = ["ANIMAL","BANANA","FLOWER","SCHOOL","FRIEND","PLANET","FOREST","FAMILY","ORANGE","RABBIT","SUMMER"]

game_board = trtl.Turtle()
x = -200
y = -200
def columns(n):
    global game_board, x, y
    for i in range(n):
        game_board.goto(x,y)
        game_



'''def game_starter():
    if 3<=age<6:
        
    elif 6<age<10:
        ###
    else:
        ###'''



def onclick_playbutton(x,y):
    wn.clear()
    print(x,y)
    

def onclick_closebutton(x,y):
    print(x,y)
    trtl.bye()

play_button.onclick(onclick_playbutton)
close_button.onclick(onclick_closebutton)
wn.mainloop()
        
