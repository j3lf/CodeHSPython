speed(10)
penup()
length = 50

def square():
    for i in range (4):
        forward(length)
        left(90)

while length < 400:
    left(90)
    forward(length/2)
    right(90)
    forward(length/2)
    left(180)
    pendown()
    square()
    penup()
    setposition(0,0)
    length = length + 50
    print(length)
