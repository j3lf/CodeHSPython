speed(0)

penup()
setposition(0,-200)

radius = int(input("What radius for circle? "))

def grey_circle():
    color("grey")
    pendown()
    begin_fill()
    circle(radius)
    end_fill()
    left(90)
    penup()
    forward(radius*2)
    right(90)
    
for i in range(3):
    grey_circle()
    radius = radius/2
