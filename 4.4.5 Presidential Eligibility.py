age= int(input("Age: "))
citizen= str(input("born in the U.S? (Yes/No): "))
how_long= int(input("Years of residency: "))

print(age)
print(citizen)
if age <=34:
    print("You are not eligible to run for president.")
elif citizen == "Yes":
    print("you are eligible to run for president.")
else:
    print("You are not eligible to run for president")
