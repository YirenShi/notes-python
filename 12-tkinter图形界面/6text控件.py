import  tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("sunck")
#设置大小和位置
win.geometry("400x400+200+200")

"""
文本控件，用于显示多行文本
"""
#height  显示的行数
text = tkinter.Text(win,width = 30,height = 4)
text.pack()
str  = """What would you do if you failed? Many people may choose to give up. However, the surest way to success is to keep your direction and stick to your goal.On your way to success, you must keep your direction. It is just like a lamp, guiding you in darkness and helping you overcome obstacles on your way. Otherwise, you will easily get lost or hesitate to go ahead."""

text.insert(tkinter.INSERT,str)

win.mainloop()