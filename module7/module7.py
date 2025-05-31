
# Sorting and Reversing Lists

colors = ['blue','red','yellow','green']
print(colors)

colors.sort()
print(colors)

colors.sort(reverse=True)
print(colors)

colors.reverse()
print(colors)

colors = ['blue','red','yellow','green']
print("\nHere is the sorted list without it being changed")
print(colors)
print(sorted(colors))
print(colors)

#1. 
list = ['charlie','alpha','delta','bravo','elephant']
print("\n", list)
print(sorted(list))

#2.
print("\n", list)
list.sort(reverse=True)
print(list)