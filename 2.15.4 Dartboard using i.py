speed(0)
penup()
setposition(0,25)

for i in range (25,101,25):
    pendown()
    circle(i)
    penup()
    right(90)
    forward(25)
    left(90)
    print(i)
