import  tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("sunck")
#设置大小和位置
win.geometry("400x400+200+200")

label = tkinter.Label(win,text = "sunck is a good man",bg = "red")
#设置焦点---给win不需要设置焦点，其他必须要
label.focus_set()
label.pack()


def func(event):
    print("event.char = ",event.char)
    print("event.keycode = ",event.keycode)
#<Enter> 鼠标光标进入控件时触发

label.bind("<Key>",func)


win.mainloop()















