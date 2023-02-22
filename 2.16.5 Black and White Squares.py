speed(8)
penup()
backward(125)
pendown()


def draw_square(even):
    if even % 2 == 0:
        begin_fill()
    for i in range(4):
        forward(30)
        left(90)
    end_fill()
    
for i in range (6):
    pendown()
    draw_square(i)
    penup()
    forward(40)
    print(i)
