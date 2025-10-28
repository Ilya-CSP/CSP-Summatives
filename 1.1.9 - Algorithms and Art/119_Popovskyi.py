import time
import turtle as trtl
import math

wn = trtl.Screen()
pointer = trtl.Turtle()
wn.setworldcoordinates(0, 0, 11, 8)  # assign coordinates to the graph
trtl.addshape("pointer", ((-2, -8), (2, -8), (2, -4), (2, 1), (4, 1), (0, 6), (-4, 1), (-2, -4)))


pointer.speed(0)
pointer.hideturtle()

# draw x axis
pointer.penup()
pointer.goto(0, 0)
pointer.pendown()
pointer.goto(10, 0)

# draw x axis labels
for horizontal in range(11):
    pointer.penup()
    pointer.goto(horizontal, 0)
    pointer.setheading(90)
    pointer.forward(0.1)
    pointer.pendown()
    pointer.forward(0.2)
    pointer.penup()
    pointer.goto(horizontal, -0.4)
    pointer.write(str(horizontal), align="center", font=("Arial", 10, "normal"))

# draw y axis
pointer.penup()
pointer.goto(0, 0)
pointer.pendown()
pointer.goto(0, 7)

for vertical in range(8):
    pointer.penup()
    pointer.goto(0, vertical)
    pointer.setheading(0)
    pointer.forward(0.1)
    pointer.pendown()
    pointer.forward(0.2)
    pointer.penup()
    pointer.goto(-0.25, vertical - 0.1)
    pointer.write(str(vertical), align="center", font=("Arial", 10, "normal"))
    pointer.hideturtle()
    
retry = "y"
while retry == "y":
    # user inputs
    ball_color = trtl.textinput("Color", "Do you want to change the color of a turtle (y/n)?")
    if ball_color == "y":
        color = trtl.textinput("Color", "Chose color")
        trtl.color(color)

    trtl.penup()
    height = trtl.textinput("Height", "Chose height (can go higher than the label)")
    height = int(height)

    change_shape = trtl.textinput("Shape", "Do you want to choose the shape (y/n, by default a a pointer)?")
    if change_shape == "y":
        shape = trtl.textinput("Shape", "Chose shape")
    else:
        shape = "pointer"

    g = trtl.textinput("Gravity", "How strong is the gravity (m/s^2, no decimals! Can also enter the names of planets)?")
    if g == "earth":
        g = 9.81
    elif g == "sun":
        g = 274
    elif g == "moon":
        g = 1.62
    elif g == "mercury":
        g = 3.7
    elif g == "jupiter":
        g = 24.8
    elif g == "venus":
        g = 8.87
    elif g == "mars":
        g = 3.71
    elif g == "saturn":
        g = 10.44
    elif g == "uranus":
        g = 8.69
    elif g == "neptune":
        g = 11.15
    else: 
        g = int(g)

    path_trace = trtl.textinput("Trace Path", "Trace turtle path (y/n)?")

    q = trtl.textinput("Velocity", "How fast is the ball going across x axis (m/s)?")
    q = int(q)
    v0 = q
    trtl.hideturtle()
    
    # input proccesing

    pointer = trtl.Turtle()

    if ball_color == "y":
        pointer.color(color)
    else:
        pointer.color("black")
            
    pointer.penup()
    pointer.goto(0, height)

    if path_trace == "y":
        pointer.pendown()
    else:
        pointer.penup()

    pointer.shape(shape)
    #  variables
    x0 = 0
    y = height
    vx = v0
    dt = 0.05  # time difference
    t_total = 0
    vy = 0

    while y > 0:
        # kinematics
        x = x0 + vx * t_total
        draw_x = x / 1.4667  # scale to fit the graph
        vy += -g * dt    # increase velocity due to gravity
        y += vy * dt

        # calculate heading
        angle_rad = math.atan2(vy, vx)
        angle_deg = math.degrees(angle_rad)
        pointer.setheading(angle_deg)

        print(f"t={t_total:.2f} s, x={x:.2f}, y={y:.2f}")  # debug
        pointer.goto(draw_x, y) 
        time.sleep(dt)
        t_total += dt
    
    results = [round(t_total, 2), round(draw_x, 2), round(y, 2)]
    retry = trtl.textinput(
        "Retry",
        f"Results: t = {results[0]} s, x = {results[1]}, y = {results[2]}\nDo you want to try again (y/n)?")
    pointer.clear()