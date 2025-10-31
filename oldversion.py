import os
import zipfile
import shutil
import funstuff as f
from colorama import Fore

inputpath = input("write the path of the .sb3 file you want to unpack: ")
inputpath.replace("/", "//")

if inputpath.endswith(".sb3") or inputpath.endswith(".sb2"):
    filename1 = os.path.basename(inputpath)
    if filename1.endswith(".sb3"):
        filename2 = filename1.replace(".sb3", "")
    elif filename1.endswith(".sb2"):
        filename2 = filename1.replace(".sb3", "")
    elif not os.path.exists(inputpath):
        print(Fore.RED + "error: not a valid path or file!!")
        f.die()
else:
    print(Fore.RED + "error: not an sb3 file!!")
    f.die()

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