import turtle as trtl
wn = trtl.Screen()

#change the screen size 
wn.setup(width=800, height=800)

#all the fonts
font_setup_title = ("Arial", 50, "bold")
main_menu_font = ("Arial", 32, "bold")

#prepare turtle for the title
main_menu_text = trtl.Turtle()
main_menu_text.hideturtle()
main_menu_text.penup()
main_menu_text.speed("fastest")

#main menu title
title_color_list = ["blue", "orange", "green"]
tictactoe_list = ["Tic", "Tac", "Toe"]
title_distance = -138

for i in range(len(tictactoe_list)):
    main_menu_text.goto(title_distance,135)
    main_menu_text.color(title_color_list[i])
    main_menu_text.write(tictactoe_list[i], font=font_setup_title, align="center")
    title_distance+=138

#play button
play_button = trtl.Turtle()
play_button.hideturtle()
play_button.speed("fastest")
play_button.shape("square")
play_button.shapesize(5)
play_button.penup()

play_button.goto(0,25)
play_button.write("Play", font=main_menu_font, align="center")

#match log button
matchlog_button = trtl.Turtle()
matchlog_button.hideturtle()
matchlog_button.speed("fastest")
matchlog_button.shape("square")
matchlog_button.shapesize(5)
matchlog_button.penup()

matchlog_button.goto(0,75)
matchlog_button.write("Play", font=main_menu_font, align="center")







#Game board
'''board_draw = trtl.Turtle()

board_draw.speed("fastest")
line_draw = -150
for i in range(2):
    board_draw.penup()
    board_draw.goto(line_draw,300)
    board_draw.pendown()
    board_draw.goto(line_draw,-300)'''

wn.mainloop()