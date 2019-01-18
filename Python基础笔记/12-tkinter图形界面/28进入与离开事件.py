import  tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("sunck")
#设置大小和位置
win.geometry("400x400+200+200")

label = tkinter.Label(win,text = "sunck is a good man",bg = "red")
label.pack()


def func(event):
    print(event.x,event.y)
#<Enter> 鼠标光标进入控件时触发

label.bind("<Enter>",func)
label.bind("<Leave>",func)

win.mainloop()















