speed(8)

radius = int(input("what radius for circle? "))

def draw_square(radius):
    color("red")
    begin_fill()
    for i in range(4):
        forward(radius)
        left(90)
    end_fill()

def draw_circle(radius):
    color("blue")
    begin_fill()
    circle(radius)
    end_fill()


penup()
right(90)
forward(radius)
left(90)
backward(radius)
draw_square(radius*2)

forward(radius)
draw_circle(radius)
