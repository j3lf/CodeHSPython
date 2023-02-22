speed(0)


def draw_x():
    left(45)
    pensize(10)
    color("red")
    for i in range(4):
        forward(100)
        backward(100)
        left(90)

def draw_check():
    left(45)
    color("green")
    pensize(10)
    forward(200)
    backward(200)
    left(90)
    forward(100)

def draw_line():
    pensize(10)
    color("yellow")
    backward(100)
    forward(200)


rating = int(input("Pick a number between 1-10: "))

if rating <= 4:
    draw_x()
elif rating >= 8:
    draw_check()
else:
    draw_line()
