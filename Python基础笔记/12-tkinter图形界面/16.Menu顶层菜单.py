import  tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("sunck")
#设置大小和位置
win.geometry("400x400+200+200")
#菜单条
menubar = tkinter.Menu(win)
win.config(menu = menubar)

def func():
    print("sucnk is a good man")

#创建一个菜单选项
menu1 = tkinter.Menu(menubar,tearoff = False)
#给菜单选项添加内容
for item in["python","c","c++","oc","swift","c#","shell","Java","JS","退出"]:
    if item =="退出":
        #添加分割线
        menu1.add_separator()
        menu1.add_command(label=item,command = win.quit)
    else:
        menu1.add_command(label = item,command = func)
#向菜单条上添加菜单选项
menubar.add_cascade(label ="语言",menu = menu1)


menu2 = tkinter.Menu(menubar,tearoff = False)#创建一个菜单选项
menu2.add_command(label = "red")#给菜单选项添加内容
menu2.add_command(label = "blue")#给菜单选项添加内容
menubar.add_cascade(label ="颜色",menu = menu2)#向菜单条上添加菜单选项

win.mainloop()















