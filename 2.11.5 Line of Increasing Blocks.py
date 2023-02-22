speed(0)
length = 10
penup()
setposition(-150,0)

def draw_block():
    for i in range(4):
        pendown()
        forward(length)
        left(90)
        penup()
    forward(length *2)


for i in range(5):
    draw_block()
    length = length + 10
    print(length)
