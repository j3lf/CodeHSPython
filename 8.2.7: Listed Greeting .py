# fill in this function to greet the user!
user_info = "Info here"

def greeting(user_info):
    greeting = user_info.split()
    return "Hello, " + (greeting[0]) + "! I also enjoy " + (greeting[-1]) + "!"

print (greeting(user_info))
