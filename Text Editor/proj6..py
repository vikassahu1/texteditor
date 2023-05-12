# Notepad 
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import random

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1980x800")
        self.title("Untitled - Notepad")
        self.wm_iconbitmap("note.ico")
        self.config(background="black")
        self.statusbar()
        self.menu()
    

    def note_text(self):
        global file
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT,fill=Y)
        self.tex = Text(self,yscrollcommand=scrollbar.set,font="comicsansms 20",undo=True)
        file = None
        self.tex.pack(expand=True, fill=BOTH)
        scrollbar.config(command=self.tex.yview)

    def menu(self):
        mymenu = Menu(self)
        m1 = Menu(mymenu,tearoff=0)
        m1.add_command(label="New",command=self.newFile)
        m1.add_command(label="Open",command=self.openFile)
        m1.add_separator()
        m1.add_command(label="Save",command=self.saveFile)
        m1.add_separator()
        m1.add_command(label="Exit",command=quit)
        mymenu.add_cascade(label="File",menu=m1)

        m2 = Menu(mymenu,tearoff=0)
        m2.add_command(label="Undo",command=self.un_do)
        m2.add_command(label="Redo",command=self.re_do)
        m2.add_separator()
        m2.add_command(label="Cut",command=self.cut)
        m2.add_command(label="Copy",command=self.copy)
        m2.add_command(label="Paste",command=self.paste)
        mymenu.add_cascade(label="Edit",menu=m2)

        m3 = Menu(mymenu,tearoff=0)
        m3.add_command(label="About",command=self.about)
        m3.add_command(label="Tips",command=self.tips)
        mymenu.add_cascade(label="Help",menu=m3)
        
        self.config(menu=mymenu)
    
    def statusbar(self):
        st = StringVar()
        st.set("Ready....")
        Label(self,textvariable=st,anchor=W).pack(side=BOTTOM,fill=X)
    
    def cut(self):
        self.tex.event_generate(("<<Cut>>"))
    
    def copy(self):
        self.tex.event_generate(("<<Copy>>"))
    
    def paste(self):
        self.tex.event_generate(("<<Paste>>"))
    
    def about(self):
        showinfo("Notepad","This a notepad developed by Vikas Kumar Sahu")

    def newFile(self):
        global file 
        self.title("Untitled - Notepad")
        file = None
        self.tex.delete(1.0,END)
    
    def openFile(self):
        global file
        file = askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"),
                            ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            self.title(os.path.basename(file) + " - Notepad")
            self.tex.delete(1.0, END)
            f = open(file, "r")
            self.tex.insert(1.0, f.read())
            f.close()
    

    def saveFile(self):
        global file
        if file == None:
            file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                        filetypes=[("All Files", "*.*"),
                                    ("Text Documents", "*.txt")])
            if file == "":
                file = None
            else:
                f = open(file,"w")
                f.write(self.tex.get(1.0,END))
                self.title(os.path.basename(file) + " - Notepad")
                f.close()
            

    def un_do(self):
        self.tex.edit_undo()

    def re_do(self):
        self.tex.edit_redo()
    
    def tips(self):
        tip = ["Study Everyday","Drink a lot of water everyday","Stay Fit","Be a hustler","There is no replace of hardwork"]
        showinfo("Tip of the day",tip[random.randint(0,len(tip)-1)])


if __name__ =='__main__': 
    window = GUI()
    window.note_text()
    window.menu()
    window.statusbar()
    window.mainloop()
