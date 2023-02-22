speed(0)

def green_check():
    color("green")
    pensize(10)
    left(135)
    forward(50)
    backward(50)
    right(90)
    forward(100)
    backward(100)


user_input = int(input("guess a number 1-10: "))
secret_number = 1

while user_input != secret_number:
    user_number = int(input("Incorrect, Try again (1-10): "))
    
green_check()
