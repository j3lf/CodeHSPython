magic_number = 3

# Your code here...
while True:
    guess = int(input("Guess my number: "))
    if guess > magic_number:
        print("too high!")
    elif guess < magic_number:
        print("too low!")
    elif guess == magic_number:
        print("Correct")
        break
    
print("Good Job")
