def colored_circle(color_choice):
    color(color_choice)
    pendown()
    begin_fill()
    circle(20)
    end_fill()
    penup()
    
speed(8)
penup()
backward(140)

for i in range(2):
    colored_circle("blue")
    forward(40)
    colored_circle("green")
    forward(40)
    colored_circle("yellow")
    forward(40)
    colored_circle("red")
    forward(40)
