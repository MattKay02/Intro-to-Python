
#Reading Files

a = open("demo.txt", "r")
print(a.read())


a = open("demo.txt", "r")
print(a.readline())
print(a.readline())
a.close()


a = open("demo.txt", "r")
print(a.readline(3))
a.close()


with open("demo.txt") as myfile:  # with closes the file link automatically
    contents = myfile.read()
    print(contents)


a = open("demo.txt", "a")
a.write("\nHere is another line in our text file")
a.close()


a = open("demo.txt", 'w')
a.write("what has happened now?")
a.close() 