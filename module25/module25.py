 
# Displaying Daytime Working Directory and File Metadata

from datetime import date
from datetime import time
from datetime import datetime

today = date.today()
date_time = datetime.now()

print("Todays date is: ", today)
print("All together now: ", date_time)


import os 

dirpath = os.getcwd()
print("Your current directory is: ", dirpath)

foldername = os.path.basename(os.getcwd())
print("The directory name is: ", foldername)


# print(os.stat("module25.py"))

x = 16.89
print(int(x))

nums = [1,2,3,4,5]
print(nums[2:4])

a = 1
while(a < 4):
    print(a)
    a += 1
