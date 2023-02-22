speed(10)

def draw_square():
    pendown()
    for i in range(4):
        forward(square_length)
        left(90)


def move_to_next_corner():
    penup()
    forward(400)
    left(90)


square_length = int(input("what length and width should be used?: "))

penup()
setposition(-200,-200)
for i in range(4):
    draw_square()
    move_to_next_corner()
