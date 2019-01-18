import  tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("sunck")
#设置大小和位置
#win.geometry("400x400+200+200")

#EXTENDED 可以是listbox支持shift和control多选
lb = tkinter.Listbox(win,selectmode = tkinter.EXTENDED)


for item in ["good","nice","handsome","vb","vg","vn",
             "good1", "nice1", "handsome1", "vb1", "vg1", "vn1","good2","nice2","handsome2","vb2","vg2","vn2"]:
    #按顺序添加
    lb.insert(tkinter.END,item)
# 按住shift，可以实现连选
# 按住control可以实现多选
#滚动条
sc = tkinter.Scrollbar(win)
sc.pack(side = tkinter.RIGHT,fill = tkinter.Y)
lb.configure(yscrollcommand = sc.set)
lb.pack(side = tkinter.LEFT,fill = tkinter.BOTH)
sc['command'] = lb.yview

win.mainloop()

