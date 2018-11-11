import  tkinter


win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+200+200")

"""
Label:标签控件，可以显示文本

"""
#win：父窗体
#text 显示的文本内容
#bg   背景颜色
#fg 字体颜色
#wraplength指定文本中多宽进行换行
#justify   设置换行后的对齐方式
#anchor 位置 n 北 e东  s南 w洗  center居中  ne东北方向  默认center
label = tkinter.Label(win,text = "sunck is a good man",bg = "pink",fg = "red",font = ("黑体",20),
                      width = 10,height = 10,wraplength = 100,justify ="left",anchor = "e" )

#显示出来
label.pack()



win.mainloop()