speed(7)

radius = 25

def move_down():
    penup()
    right(90)
    forward(25)
    left(90)
    pendown()
    
for i in range(4):
    circle(radius)
    move_down()
    radius = radius + 25
    print(radius)
