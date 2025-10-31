from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os

def addfile():
    inputfile = filedialog.askopenfilename(filetypes=(("Scratch 3 files", "*.sb3"),("Scratch 2 files", "*.sb2")))
    inputfile.replace("/", "//")
    inputlist.append(inputfile)
    if len(inputlist) != len(set(inputlist)):
        del inputlist[-1]
        messagebox.showwarning(title="Error!!", message="no duplicates!")
    else:
        inputlistgui.insert(inputlistgui.size(),inputfile)
        fn1.append(os.path.basename(inputfile))
        global idx 
        idx += 1
        if fn1[idx].endswith(".sb3"):
            fn2.append(fn1[idx].replace(".sb3", ""))
        else:
            fn2.append(fn1[idx].replace("sb2", ""))
        print(inputlist)
        print(fn1)
        print(fn2)

def addoutput():
    global display 
    display = filedialog.askdirectory()
    global outputdisplay
    outputdisplay.config(text=display)

inputlist = []
fn1 = []
fn2 = []
idx = -1
display = "No file directory"

w = Tk()
w.geometry("420x450")
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

outputdisplay = Label(outputframe, text=display, relief="solid", bd=1)
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

starter = Button(outputframe, text="DO IT!!", command=dothething)
outputbtn.pack()

w.mainloop()