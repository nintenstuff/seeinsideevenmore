import os
import zipfile
import shutil
import funstuff as f
from colorama import Fore

inputpath = input("write the path of the .sb3 file you want to unpack (don't forget to double the slashes!): ")
if not inputpath.endswith(".sb3"):
    print(Fore.RED + "error: not an sb3 file!!")
    f.die()
elif not os.path.exists(inputpath):
    print(Fore.RED + "error: not a valid path or file!!")
    f.die()
filename1 = os.path.basename(inputpath)
filename2 = filename1.replace(".sb3", "")

output = input("write the output path: ")
if not os.path.exists(output):
    print(Fore.RED + "error: not a valid path or file!!")
    f.die()

title = input("insert new title: ")
if title == (""):
    print(Fore.RED + "error: not a valid folder name!!")
    f.die()
elif os.path.exists(output + "/"+ title):
    print(Fore.RED + "error: path already exists!!")
    f.die()

os.chdir(output)
print("creating folder...")
os.mkdir(title)
print("done!\ncopying file...")
shutil.copy(inputpath, output + "/" + title)
print("done!\nrenaming file...")
os.chdir(output + "/" + title)
os.rename(filename1, filename2 + ".zip")
print("done!\nunpacking file...")
zipfile.ZipFile(output + "/" + title + "/" + filename2 + ".zip", "r").extractall()
print("done!\ndeleting zip...")
os.remove(filename2 + ".zip")
print("\nALL DONE!!")
f.die()