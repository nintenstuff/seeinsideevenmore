from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil
import zipfile

inputlist = []
fn1 = []
fn2 = []
idx = -1
outputdir = "No file directory"

def addfile():
    inputfile = filedialog.askopenfilename(filetypes=(("Scratch 3 files", "*.sb3"),("Scratch 2 files", "*.sb2")))
    inputfile.replace("/", "//")
    inputlist.append(inputfile)
    if len(inputlist) != len(set(inputlist)):
        del inputlist[-1]
        messagebox.showwarning(title="Error!", message="Error: duplicates not allowed!!")
    elif inputfile == "":
        del inputlist[-1]
    inputlistgui.insert(inputlistgui.size(),inputfile)
    fn1.append(os.path.basename(inputfile))
    global idx 
    idx += 1
    if fn1[idx].endswith(".sb3"):
        fn2.append(fn1[idx].replace(".sb3", ""))
    else:
        fn2.append(fn1[idx].replace("sb2", ""))

def addoutput():
    global outputdir 
    outputdir = filedialog.askdirectory()
    global outputdisplay
    outputdisplay.config(text=outputdir)

def dothething():
    global inputlist
    global fn1
    global fn2
    global idx
    global outputdisplay
    global outputdir
    if outputdir != "No file directory":
        if inputlist:
            for i in range(len(inputlist)):
                print(i)
                os.chdir(outputdir)
                if os.path.exists(outputdir + "/" + fn2[i]):
                     messagebox.showwarning(title="Error!", message='Error: cannot add directory "' + fn2[i] + '"!!')
                else:
                    os.mkdir(fn2[i])
                    shutil.copy(inputlist[i], outputdir + "/" + fn2[i])
                    os.chdir(outputdir + "/" + fn2[i])
                    os.rename(fn1[i], fn2[i] + ".zip")
                    zipfile.ZipFile(outputdir + "/" + fn2[i] + "/" + fn2[i] + ".zip", "r").extractall()
                    os.remove(fn2[i] + ".zip")
                    messagebox.showinfo(title="Done!", message="Project " + fn1[i] + " extracted!")
            inputlist = []
            inputlistgui.delete(0,END)
            outputdir = "No file directory"
            outputdisplay.config(text=outputdir)
            fn1 = []
            fn2 = []
            idx = -1
                
        else:
            messagebox.showwarning(title="Error!", message="Error: input list is empty!!")
    else:
        messagebox.showwarning(title="Error!", message="Error: not a valid output path!!")


w = Tk()
w.geometry("385x350")
w.title("See Inside Even More")

icon = PhotoImage(file="docs/logo.png")
w.iconphoto(True,icon)

siemtitle = Label(w, text="See Inside Even More", font=("Segoe UI", 10, "bold"))
siemtitle.pack()

inputframe= Frame(w)
inputframe.pack(side="top", anchor="nw")

inputfilelabel = Label(inputframe, text="Input files:")
inputfilelabel.pack(side="top", anchor="nw")

inputlistgui = Listbox(inputframe, width="50")
inputlistgui.pack(side="left")

newfile = Button(inputframe,text="Add file...",command=addfile)
newfile.pack(side="left")

outputframe = Frame(w)
outputframe.pack(side="top", anchor="nw")

outputlabel = Label(outputframe, text="insert output here:")
outputlabel.pack(anchor="nw")

outputdisplay = Label(outputframe, text=outputdir, relief="solid", bd=1)
outputdisplay.pack(side="left")

outputbtn = Button(outputframe, text="Add output directory...", command=addoutput)
outputbtn.pack(side="right")

assetnamez = IntVar()
assetcheck = Checkbutton(w,
                         text="Name assets according to their name in the project (NOT WORKING)",
                         variable=assetnamez,
                         onvalue=1,
                         offvalue=0)
assetcheck.pack()

beautyfier = IntVar()
beautycheck = Checkbutton(w,
                         text="Beautify JSON (NOT WORKING)",
                         variable=beautyfier,
                         onvalue=1,
                         offvalue=0)
beautycheck.pack()

starter = Button(w, text="DO IT!!", command=dothething)
starter.pack()

w.mainloop()