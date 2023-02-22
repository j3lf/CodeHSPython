def move_to_row(num_circle):
    x_value = -((num_circle*50)/2)
    y_value = -250 +(50*row_value)
    penup()
    setposition(x_value,y_value)
    pendown()

def draw_circle_row(num_circle):
    for i in range(num_circle):
        pendown()
        circle(radius)
        penup()
        forward(diameter)

speed(0)
radius = 25
diameter = radius * 2
row_value = 1
num_circle = int(input("How many circle on the bottom row? (8 or less): "))
penup()

for i in range(num_circle):
    move_to_row(num_circle)
    row_value=row_value+1
    draw_circle_row(num_circle)
    num_circle=num_circle-1
