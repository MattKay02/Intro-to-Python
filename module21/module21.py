
# Using default arguments

def student(firstname, lastname = "Bigger", major = "Information Technology"):
    print(firstname, lastname, "majors in", major)

student("Tony")
student("Tony", "Stark")
student("Tony", "Stark", "Physics")
