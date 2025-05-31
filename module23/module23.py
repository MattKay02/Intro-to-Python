
# Handling exceptions

try: 
    print(0/0)

except ZeroDivisionError:
    print("you cannot divide by zero!")


import sys

try:
    num = int(input("Enter a number betweem 1-10: \n"))

except ValueError:
    print("Please use numbers only")
    sys.exit()

print("You entered the number", num)