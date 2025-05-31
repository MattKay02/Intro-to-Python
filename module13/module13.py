
# Working with While Loops

a = 0

while a < 6:
    a += 1
    if a == 4:
        continue # skips this iteration if condition is true
    print(a)
    
a = 0

while a < 6:
    a += 1
    if a == 4:
        break # terminates loop if condition is true
    print(a)