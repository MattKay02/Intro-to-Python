
# Nesting For Loops

outer = ['outer1','outer2','outer3']
nest = ['nest1','nest2','nest3']

for x in outer:
    for y in nest:
        print(x, y)
    print('\n')


numbers = [1,2,3]
letters = ['A','B','C']

for x in numbers:
    print(x)
    for y in letters:
        print(y)
    print('\n')

#1. 

numbers = [1,2,3,4,5]
letters = ['A','B','C','D','E']

for x in numbers:
    for y in letters:
        print(x,y)
    print('\n')
