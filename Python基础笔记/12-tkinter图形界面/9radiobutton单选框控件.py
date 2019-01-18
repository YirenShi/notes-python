import  tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("sunck")
#设置大小和位置
win.geometry("400x400+200+200")

def updata():
    print(r.get())



#绑定变量,一组单选框要绑定同一个变量
r = tkinter.IntVar()
radio1 = tkinter.Radiobutton(win,text = "one",value = "1",variable = r,command = updata)
radio1.pack()
radio2 = tkinter.Radiobutton(win,text = "two",value = "2",variable = r,command = updata)
radio2.pack()


r = tkinter.StringVar()
radio3 = tkinter.Radiobutton(win,text = "three",value = "good",variable = r,command = updata)
radio3.pack()
radio4 = tkinter.Radiobutton(win,text = "four",value = "nice",variable = r,command = updata)
radio4.pack()

win.mainloop()