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
    
def draw_face():
    draw_body()
    draw_smile()
    eyes()

happy = input("Draw the face(yes/no): ")

if happy == ("yes"):
    draw_face()
