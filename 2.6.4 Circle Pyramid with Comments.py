"""This program will make a 
pyramid of circle
"""
penup()
setposition(-100,-200)
#Bottom Circle Line
for i in range(3):
    pendown()
    circle(50)
    penup()
    forward(100)
setposition(-50,-100)
#Middle Circle line
for i in range(2):
    pendown()
    circle(50)
    penup()
    forward(100)
    
#Top Circle
setposition(0,0)
pendown()
circle(50)
penup()
forward(100)
