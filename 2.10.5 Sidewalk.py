speed(0)


def draw_square():
    for i in range(4):
        forward(50)
        left(90)


def draw_sidewalk():
    pendown()
    for i in range(7):
        draw_square()
        forward(50)
    penup()
    forward(50)
    left(90)
    
    
    
    
penup()
setposition(-200, 200)
for i in range(4):
    draw_sidewalk()
