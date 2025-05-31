
# Using keyword and positional arguments

def greet(name, msg = "How are you today?"):
    print("Hey", name + ", " + msg)

greet(msg = "How do you do?", name = "Dave")
greet("Matt")