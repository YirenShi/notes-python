import  tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("sunck")
#设置大小和位置
win.geometry("400x400+200+200")

def func(event):
    print(event.x,event.y)
#<Button-1> 鼠标左键
#<Button-2> 鼠标中键    滑轮
#<Button-3> 鼠标右键
#<Double-Button-1> 鼠标左键双击
#<Triple-Button-1> 鼠标左键三击
button1 = tkinter.Button(win,text = "leftMouse button")
#bind 给控件绑定事件
button1.bind("<Button-1>",func)

button1.pack()

















win.mainloop()