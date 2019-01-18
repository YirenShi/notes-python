import  tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("sunck")
#设置大小和位置
win.geometry("400x400+200+200")


label = tkinter.Label(win,text = "sunck is a good man")
label.pack()
def func(event):
    print(event.x,event.y)

#< B1 - Motion > 左键移动
#< B2 - Motion > 中键移动
#< B3 - Motion > 右键移动
label.bind("<B1-Motion>",func)

win.mainloop()




















