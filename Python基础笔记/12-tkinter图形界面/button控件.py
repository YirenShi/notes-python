import  tkinter

def func():
    print("sunck is a good man")
win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+200+200")
#创建按钮                                   命令：不用加引号跟括号
button1 = tkinter.Button(win,text = "按钮",command = func,width = 10,height = 10)
button1.pack()
#                                               直接写
button2 = tkinter.Button(win,text = "按钮",command = lambda:print("sunckis a good man"))
button2.pack()

button3 = tkinter.Button(win,text = "按钮",command = win.quit)
button3.pack()










win.mainloop()






















