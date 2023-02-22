speed(6)


def blue_circle():
    penup()
    setposition(100,50)
    color("blue")
    begin_fill
    circle(60)
    end_fill()
    
def red_square():
    penup()
    setposition(-100,50)
    color("red")
    begin_fill
    circle(60,360,4)
    end_fill
    
def yellow_half_circle():
    penup()
    setposition(-115,150)
    color("yellow")
    begin_fill()
    circle(60,180)
    end_fill
    
def green_pentagon():
    penup()
    setposition(100,-150)
    right(180)
    color("green")
    begin_fill
    circle(60,360,5)
    end_fill()
    
blue_circle()
red_square()
yellow_half_circle()
green_pentagon()
