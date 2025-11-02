#setup the turtle and wn
import turtle as trtl
wn = trtl.Screen()

#change the screen size 
wn.setup(width=800, height=800)
root = wn.getcanvas().winfo_toplevel()
root.resizable(False, False)

#all the fonts
font_setup_title = ("Arial", 50, "bold")
main_menu_font = ("Arial", 32, "bold")
game_font = ("Arial", 24, "bold")

############################################################### prepare ALL turtles
main_menu_text = trtl.Turtle()
main_menu_text.hideturtle()
main_menu_text.penup()
main_menu_text.speed("fastest")

play_button = trtl.Turtle()
play_button.hideturtle()
play_button.color("black")
play_button.speed("fastest")
play_button.shape("square")
play_button.shapesize(5)
play_button.penup()

matchlog_button = trtl.Turtle()
matchlog_button.hideturtle()
matchlog_button.speed("fastest")
matchlog_button.shape("square")
matchlog_button.shapesize(5)
matchlog_button.penup()

board_draw = trtl.Turtle()
board_draw.speed("fastest")
board_draw.hideturtle()

player_name1_trtl = trtl.Turtle()
player_name1_trtl.hideturtle()
player_name1_trtl.speed("fastest")

player_name2_trtl = trtl.Turtle()
player_name2_trtl.hideturtle()
player_name2_trtl.speed("fastest")

board_draw = trtl.Turtle()
board_draw.speed("fastest")
board_draw.hideturtle()

player_name1_trtl = trtl.Turtle()
player_name1_trtl.hideturtle()
player_name1_trtl.speed("fastest")
player_name1_trtl.penup()

player_name2_trtl = trtl.Turtle()
player_name2_trtl.hideturtle()
player_name2_trtl.speed("fastest")
player_name2_trtl.penup()

# hitbox turtles
squares = []
for _ in range(9):
    t = trtl.Turtle()
    t.hideturtle()
    t.shape("square")
    t.color("white")
    t.shapesize(10)
    t.penup()
    t.speed("fastest")
    # initialize claim/owner attributes
    t.claimed = False
    t.owner = None
    squares.append(t)

################################################################
#main menu title
title_color_list = ["blue", "orange", "red"]
tictactoe_list = ["Tic", "Tac", "Toe"]
title_distance = -138

for i in range(len(tictactoe_list)):
    main_menu_text.goto(title_distance,135)
    main_menu_text.color(title_color_list[i])
    main_menu_text.write(tictactoe_list[i], font=font_setup_title, align="center")
    title_distance+=138

#defines which part of the game is currently on the screen
main_menu = True #defines if it is the main menu on the screen
board_drawing = False #is the gameboard being made
game_going = False #is the game in progress

#match log button

matchlog_button.goto(0,-75)
matchlog_button.write("Match log",font=main_menu_font,align="center")

log_button_x_min = -80
log_button_x_max = 80
log_button_y_min = -105
log_button_y_max = -40

match_log = False

def log_click(x,y):
    if log_button_x_max >= x >= log_button_x_min and log_button_y_max >= y >= log_button_y_min:
        global main_menu
        if main_menu == True:
            wn.clear()
            global match_log
            main_menu = False
            match_log = True
#pull out the names and scores

#write them in order

#play button
play_button.goto(0,25)
play_button.write("Play", font=main_menu_font, align="center")
play_button.color("white")

play_button_x_min = -40
play_button_x_max = 40
play_button_y_min = 20
play_button_y_max = 55

#player names variables
player_name1 = ""
player_name2 = ""

first_turn_rule = "n" #default

def play_click(x,y):
    if play_button_x_max >= x >= play_button_x_min and play_button_y_max >= y >= play_button_y_min:
        global main_menu
        if main_menu == True:
            play_button.clear()
            matchlog_button.clear()
            main_menu_text.clear()
            global player_name1
            global player_name2
            global first_turn_rule
            global board_drawing
            player_name1 = trtl.textinput("Player 1", "Your name is...")
            player_name2 = trtl.textinput("Player 2", "Your name is...")
            first_turn_rule = trtl.textinput("Rule","Each new round, the one who lost goes first(y/n)?")
            main_menu = False
            board_drawing = True

#game board

#setup values
score1 = 0
score2 = 0
# simple turn tracker: 0 -> player A, 1 -> player B
current_turn = 0


def game_board():
    global board_draw
    global board_drawing
    global game_going

    if board_drawing == True:
        board_draw.penup()

        for x in (-131, 131):
            board_draw.goto(x, 350)
            board_draw.pendown()
            board_draw.goto(x,-350)
            board_draw.penup()

        for y in (131,-131):
            board_draw.goto(-350,y)
            board_draw.pendown()
            board_draw.goto(350,y)
            board_draw.penup()

        xs = [(-350 + -131) / 2, 0, (131 + 350) / 2]   # left, middle, right centers
        ys = [(350 + 131) / 2, 0, (-131 + -350) / 2]   # top, middle, bottom centers
        for r in range(3):
            for c in range(3):
                idx = r * 3 + c
                squares[idx].goto(xs[c], ys[r])
                squares[idx].showturtle()

        player_name1_trtl.goto(-370,-370)
        player_name1_trtl.write(str(player_name1) + "   " + str(score1), font=game_font)
        player_name2_trtl.goto(370,370)
        player_name2_trtl.write(str(player_name2) + "   " + str(score2), font=game_font, align="right")
        game_going = True
def hitbox_turtle_click_change(x, y):
# pixel half-size for shapesize(10)
    half = (10 * 20) / 2
    global current_turn
    if game_going:
        for i in range(len(squares)):
            t = squares[i]
            # skip already claimed squares
            sx = t.xcor()
            sy = t.ycor()
            if sx - half <= x <= sx + half and sy - half <= y <= sy + half:
                print("Hitbox clicked: index " + str(i) + " row " + str(i // 3) + " col " + str(i % 3))
                if current_turn == 0:
                    t.shape("square")
                    t.color("red")
                    t.claimed = True
                    t.owner = 0
                    current_turn = 1
                else:
                    t.shape("circle")
                    t.color("blue")
                    t.claimed = True
                    t.owner = 1
                    current_turn = 0
                return i
        return None


def game_events(x,y):
    # remember whether the board was already being drawn before this click
    was_board_drawing = board_drawing

    play_click(x,y)
    log_click(x,y)
    game_board()
    # check hitboxes only if the board was already active before this click
    if was_board_drawing:
        hit = hitbox_turtle_click_change(x, y)
        if hit is not None:
            print(f"Hitbox clicked: index {hit}, row {hit//3}, col {hit%3}")
            # after a successful move, check for a winner or full board
        

wn.onscreenclick(game_events)

#esc button

#check if there's three in a row

#erase the board if true and write score

#change corner scores

#show the winner 

#save the score 

#keep the screen
wn.mainloop()