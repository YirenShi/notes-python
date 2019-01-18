import  tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("sunck")
#设置大小和位置
win.geometry("400x400+200+200")

#MULTIPLE 支持多选
lb = tkinter.Listbox(win,selectmode = tkinter.MULTIPLE)
lb.pack()

for item in ["good","nice","handsome","vb","vg","vn"]:
    lb.insert(tkinter.END,item)


win.mainloop()





























