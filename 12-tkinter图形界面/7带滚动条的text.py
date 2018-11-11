import  tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("sunck")
#设置大小和位置
#win.geometry("400x400+200+200")

"""
文本控件，用于显示多行文本
"""
#创建滚动条
scroll = tkinter.Scrollbar()


#height  显示的行数
text = tkinter.Text(win,width = 30,height = 4)
#side 放到窗体的哪一侧
scroll.pack(side = tkinter.RIGHT,fill = tkinter.Y)
text.pack(side = tkinter.LEFT,fill = tkinter.Y)
str  = """What would you do 
if you failed? Many people may choose
 to give up. However, th
 e surest way to success is to keep your direction
  and stick to your goal.On your way to success, you must keep your direction. It is just like a lamp, guiding you in darkness and helping you overcome obstacles on your way. Otherwise, you will easily get lost or hesitate to go ahead.Direction means objectives. You can get nowhere without an objective in life.
You can try to write your objective on paper and make some plans to achieve it. In this way, you will know how to arrange your time and to spend your time properly. And you should also have a belief that you are sure to succeed as long as you keep your direction all the time."""
#关联
scroll.config(command = text.yview)#滚动条动控制文本动
text.config(yscrollcommand = scroll.set)#文本动控制滚动条动
text.insert(tkinter.INSERT,str)

win.mainloop()