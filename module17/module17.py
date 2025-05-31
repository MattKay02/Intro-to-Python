
# Merging Emails

with open("Hello.txt", "w") as file:
    file.write("Hey there!")

x = open("Hello.txt", "w")
y = x.read()
print(y)
x.close()
