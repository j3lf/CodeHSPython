speed(0)

penup()
setposition(-200,-200)
pendown()

def draw_square_row():
    color_value = 0

for i in range (10):
    if color_value %2 == 0:
        begin_fill()
        color("red")

for i in range (4):
    forward(40)
    left(90)
    forward(40)
    color_value = color_value + 1
    end_fill()
    
if color_value %2 == 1:
    begin_fill()
    color("black")

for i in range (4):
    forward(40)
    left(90)
    forward(40)
    color_value = color_value + 1
    end_fill()

def draw_square_row_2():
    color_value = 1

for i in range (10):
    if color_value %2 == 0:
        begin_fill()
        color("red")

for i in range (4):
    forward(40)
    left(90)
    forward(40)
    color_value = color_value + 1
    end_fill()

if color_value %2 == 1:
    begin_fill()
    color("black")

for i in range (4):
    forward(40)
    left(90)
    forward(40)
    color_value = color_value + 1
    end_fill()

def move_up_a_row():
    left(90)
    forward(40)
    right(90)
    backward(400)

for i in range (5):
    draw_square_row()
    move_up_a_row()
    draw_square_row_2()
    move_up_a_row()
