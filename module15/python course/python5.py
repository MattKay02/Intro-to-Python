
import shutil
import os

src = "demo.txt"
dst = "16Demo.txt"

shutil.copy(src, dst)

os.rename("16Demo.txt", "LeaveMeAlone.txt")

x = open("LeaveMeAlone.txt", "r")
print(x.read())
x.close()

os.remove("LeaveMeAlone.txt")
