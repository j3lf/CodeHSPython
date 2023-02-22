# Write your function for converting Celsius to Fahrenheit here.
# Make sure to include a comment at the top that says what
# each function does!


def to_F(c):
    return float(1.8 * c) + 32
    
def to_C(f):
    return float(f - 32) / 1.8
    

# Now write your function for converting Fahrenheit to Celsius.




# Now change 0C to F:
print(to_F(0))

# Change 100C to F:
print(to_F(100))

# Change 40F to C:
print(to_C(40))

# Change 80F to C:
print(to_C(80))
