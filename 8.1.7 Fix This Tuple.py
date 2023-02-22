my_tuple = (0, 1, 2, "hi", 4, 5)

# Your code here...


string_tuple = (3,)
my_tuple = my_tuple[:3] + string_tuple + my_tuple[4:]

print(my_tuple)
