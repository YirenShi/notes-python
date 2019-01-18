import  tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("sunck")
#设置大小和位置
win.geometry("400x400+200+200")
#绑定变量
lbv = tkinter.StringVar()
#1.创建一个listbox，添加几个元素
#SINGLE与BORWSE 相似，但是不支持鼠标按下后移动选中位置
#1.创建一个listbox，添加几个元素
lb = tkinter.Listbox(win,selectmode = tkinter.SINGLE,listvariable = lbv)
lb.pack()

for item in ["good","nice","handsome"]:
    #按顺序添加
    lb.insert(tkinter.END,item)
#在开始添加
lb.insert(tkinter.ACTIVE,"COOL")
#将列表当成一个元素添加的
lb.insert(tkinter.END,["VERY GOOD","VERY NICE"])

#打印当前列表中的选项
print(lbv.get())
#设置选项---改变所有
#lbv.set(("1","2","3"))

#绑定事件
def myPrint(event):
    print("*******")
    print(lb.get(lb.curselection()))
    #     双击---按钮--左键
lb.bind('<Double-Button-1>',myPrint)

win.mainloop()































