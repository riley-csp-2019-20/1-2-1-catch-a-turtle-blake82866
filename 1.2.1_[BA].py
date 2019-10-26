# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl 
import random 
#-----game configuration----
shape = "turtle"
size = 5
color = "blue"
score = 0

font_setup = ("Arial", 20, "normal")
timer = 30
bennadict_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
thickums = trtl.Turtle(shape = shape)
thickums.color(color)
thickums.shapesize(size)

vanna_white = trtl.Turtle()
vanna_white.penup()
vanna_white.goto(-370,270)
vanna_white.hideturtle()

bennadict = trtl.Turtle()
bennadict.penup()
bennadict.hideturtle()
bennadict.goto(350,270)
#-----game functions--------
def turtle_click(x,y):
    print("thickums was clicked")
    change_position()
    score_counter()
    rad_colors()
    go()

# this is a costumization it makes the turtle change colors when clicked
def rad_colors():
    new_colors = ["red", "orange", "yellow", "green", "blue", "purple", "beige"]
    new_color = random.choice(new_colors)
    thickums.color(new_color)
    if (new_color == "red"):
        wn.bgcolor("green")
    elif (new_color == "orange"):
        wn.bgcolor("blue")
    elif (new_color == "yellow"):
        wn.bgcolor("purple")
    elif (new_color == "green"):
        wn.bgcolor("red")
    elif (new_color == "blue"):
        wn.bgcolor("orange")
    elif (new_color == "purple"):
        wn.bgcolor("yellow")
    else:
        wn.bgcolor("white")     

def change_position():
    thickums.speed(0)
    thickums.penup()
    thickums.hideturtle()
    new_xpos = random.randint(-400,400)
    new_ypos = random.randint(-300,300)
    thickums.goto(new_xpos, new_ypos)
    thickums.showturtle()

def score_counter():
    global score 
    score += 1
    print(score)
    font = ("Arial", 30, "bold")
    vanna_white.clear()
    vanna_white.write(score, font = font)

def countdown():
    global timer, timer_up
    bennadict.clear()
    if timer <= 0:
        game_end()
        timer_up = True
    else:
        bennadict.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        bennadict.getscreen().ontimer(countdown, bennadict_interval) 

def game_end():
    thickums.hideturtle()
    thickums.goto(500,500)
    bennadict.goto(0,0)
    bennadict.write("Time's Up", font=font_setup)
    wn.bgcolor("red")

   # this is a costumization it makes the turtle face, move, and move at random speeds after it appears
def go():
    face = random.randint(0,360)
    thickums.setheading(face)
    speedy = random.randint(1,10)
    thickums.speed(speedy)
    move = random.randint(100,200)
    thickums.forward(move)


#-----events----------------
thickums.onclick(turtle_click)

wn = trtl.Screen()
wn.ontimer(countdown, bennadict_interval) 
wn.mainloop()