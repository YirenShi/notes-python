import  tkinter

def func():
    print("sunck is a good man")
win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+200+200")

"""
输入空间
用于显示简单的文本内容
"""

#绑定变量
e = tkinter.Variable()
#show  密文显示   show = "*"
entry = tkinter.Entry(win,textvariable = e)
entry.pack()

#e就代表输入框这个对象
#设置值
e.set("sunck is a good man")
#取值
print(e.get())
print(entry.get())


win.mainloop()








































