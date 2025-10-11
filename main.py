import os
import zipfile
import shutil
import funstuff as f

scrunchfile = input("choose the path of the .sb3 file you want to convert: ")
if not scrunchfile.endswith(".sb3"):
    print("error: not an sb3 file!!")
    f.die()
elif not os.path.exists(scrunchfile):
    print("error: not a valid path or file!!")
    f.die()

output = input("enter output path: ")
if not os.path.exists(output):
    print("error: not a valid path or file!!")
    f.die()

title = input("insert new title: ")

input("weeeee")
os.chdir(output)
os.mkdir(title)
# COPY SB3 IN DIR
# RENAME IT
# EXTRACT IT
