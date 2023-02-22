speed(0)
penup()

def draw_body():
    setposition(0,-100)
    pendown()
    color("yellow")
    begin_fill()
    circle(100)
    end_fill()
    penup()
    
def draw_smile():
    color("black")
    setposition(-75,0)
    pendown()
    right(90)
    pensize(10)
    circle(75,180)
    penup()
def eyes():
    setposition(-25,40)
    right(90)
    pendown()
    begin_fill()
    circle(5)
    end_fill()
    penup()
    #second eyes
    forward(50)
    pendown()
    begin_fill()
    circle(5)
    end_fill()
    
def frown():
    setposition(60,-50)
    left(90)
    pendown()
    color("black")
    pensize(10)
    circle(60,180)
    penup()

def draw_smiley():
    draw_body()
    draw_smile()
    eyes()
    
def draw_frown():
    draw_body()
    eyes()
    frown()

happy = input("Are you happy?(yes/no): ")

if happy == "yes":
    draw_smiley()
else:
    draw_frown()
