
# Slicing Lists

nums = [1,2,3,4,5,6]
print(nums)
print(nums[2:5],"\n")

players = ['Bob','Steve','Michael','Tom','Eli']
print(players)
print("First three players in the team:")
for player in players[:3]:
    print(player.title())
print("\n")

nums = [1,2,3,4,5,6,7,8,9]
print(nums)
print(nums[1:8:2])
print("\n")

#1.
nums = [1,2,3,4,5,6,7,8,9]
print(nums[2:5])

#3.
print(nums[0:10:2])