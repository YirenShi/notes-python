import tkinter
#from tkinter import  ttk
import os
from treeWindows import TreeWindows
from inforWindows import InforWindows
win = tkinter.Tk()
win.title("sunck")
win.geometry("900x400+200+50")

path = r"C:\Users\Zhangyadi\Desktop\project"
infoWin = InforWindows(win)
treeWin = TreeWindows(win,path,infoWin)


























win.mainloop()