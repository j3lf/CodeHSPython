speed(10)

def draw_circle():
    penup()
    forward(100)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    penup()
    backward(100)
    left(10)
    
for i in range(12):
    color("blue")
    draw_circle()
    color("red")
    draw_circle()
    color("purple")
    draw_circle()
