import  tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("sunck")
#设置大小和位置
win.geometry("400x400+200+200")

"""
供用户通过拖拽指示器改变变量的值，可以水平也可以竖直
tkinter.HORIZONTAL 水平
tkinter.VERTICAL  竖直   默认
length 水平时表示宽度，竖直是表示高度
tickinterval选择值将会为该数的倍数
"""                            #数值
scale1 = tkinter.Scale(win, from_=0, to = 100,orient = tkinter.HORIZONTAL,tickinterval = 10,length = 200)
scale1.pack()

#设置值,初始值
scale1.set(20)


#取值
def showNum():
    print(scale1.get())
tkinter.Button(win,text = "按钮",command  = showNum ).pack()





win.mainloop()





























