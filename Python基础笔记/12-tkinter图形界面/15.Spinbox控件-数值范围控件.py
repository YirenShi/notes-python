import  tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("sunck")
#设置大小和位置
win.geometry("400x400+200+200")

"""
数值范围控件
increment   步长  默认为1
"""
def updata():
    print(v.get())

#绑定变量
v = tkinter.StringVar()

#command只要值改变就会执行对应的方法
#values 最好不要与from = 0，to = 100  同时使用。values = (0,2,4,6,8) 仅选用内部的值
sp = tkinter.Spinbox(win,from_=0,to = 100,increment = 1,textvariable = v,command = updata)
sp.pack()

#设置值
v.set(20)

#取值
print(sp.get())






win.mainloop()

















