
# Working with Multiple Assignment Statements

a = b = c = 3

numbers = {"First Num":'1', "Second Num":'2'}

for key, value in numbers.items():
    print(F"Key {key} has a value of {value}")

Name = "Matt"
age = "22"
print(F"His name is {Name} and he is {age} years old")

a, b = 1, 2 

#1. 

num1, num2, num3 = 10, 20, 30

#2.

var = {"var1":'33', "var2":'car', "var3":'2.158', "var4":'hey'}

for i, value in var.items():
    print(F"{i} {value}")

#3. 

NameAge = {"Dave":'41', "Bob":'22', "Mark":'38'}

for i, value in NameAge.items():
    print(F"{i} is {value} years old")
