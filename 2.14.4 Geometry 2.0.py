speed(0)

penup()
setposition(0,-150)
pendown()
radius = 20

for i in range (7):
    circle(radius,360,i)
    radius = radius + 20
