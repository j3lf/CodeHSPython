speed(0)
radius = 100

def draw_circle_move_up():
    pendown()
    color_choice = input("What color should be used?: ")
    color(color_choice)
    begin_fill()
    circle(radius)
    end_fill()
    penup()
    left(90)
    forward(25)
    right(90)
    pendown()
    
    
penup()
setposition(0,-100)
for i in range(4):
    draw_circle_move_up()
    radius = radius - 25
    print(radius)
