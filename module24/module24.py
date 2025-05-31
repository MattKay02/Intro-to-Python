
# Using Math and Random Modules

import math
import random

num = int(input("Give me a number to find the sqaure root for \n"))
print("Sqaure root of", num, ":   ", math.sqrt(num))

print("Printing a random number:   ", random.random())

print("Printing a random integer from 1 - 999:   ", random.randint(0, 1000))

print("Printing a random integer 1 - 9:   ", random.randrange(0, 10))

print("Printing a random even integer 1 - 500:   ", random.randrange(0, 500, 2))

