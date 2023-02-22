def F2C(temp):
    try:
        return (1.8 * temp) + 32
    except:
        print "ValueError"
def C2F(temp):
    try:
        return (temp - 32) / 1.8
    except:
        print "ValueError"

# Now write your function for converting Fahrenheit to Celsius.




# Now change 0C to F:
print (C2F("0"))

# Change 100C to F:
print(C2F(100))

# Change 40F to C:
print(F2C(40))

# Change 80F to C:
print(F2C(80))
