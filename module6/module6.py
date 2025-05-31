
# Modifying Lists

employees = ["Sara","tammy","Debbie","John","Carrie"]
print(employees)

employees[0] = "Mark"
print(employees)

employees += ["Jim"]
print(employees)

employees.insert(1, "Dave")
print(employees)

del employees[2]
print(employees)

employees.remove("Carrie")
print(employees)

for x in employees:
    print(x)

if "Mark" in employees:
    print("Mark is in the list")

print(len(employees))

#1. 
list = ['1','2','3','4','5']
print(list)

list[2] = "New item"
print(list)

#2.
list = ['1','2','3','4','5']
print(list)

del list[1] 
print(list)

#3. 
list = ['1','2','3','4','5']
print(list)

list.insert(2, "New item")
print(list)