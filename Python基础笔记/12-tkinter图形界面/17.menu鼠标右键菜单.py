import  tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("sunck")
#设置大小和位置
win.geometry("400x400+200+200")

#菜单条
menubar = tkinter.Menu(win)

#菜单
menu = tkinter.Menu(menubar,tearoff = False)

#添加内容
for item in["python","c","c++","oc","swift","c#","shell","Java","JS","退出"]:
    menu.add_command(label = item)
menubar.add_cascade(label = "语言",menu = menu)

def showMenu(event):
    menubar.post(event.x_root,event.y_root)

win.bind("<Button-3>",showMenu)





win.mainloop()