my_float = 3.3312

# Your code here...

while True:
    guess = float(input("Guess my number: "))
    if guess > my_float:
        print("too high!")
    elif guess < my_float:
        print("too low!")
    elif guess == my_float:
        print("Correct!")
        break
