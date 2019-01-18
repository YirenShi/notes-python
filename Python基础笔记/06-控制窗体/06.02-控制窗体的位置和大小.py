import win32con
import win32gui
import time
import random
#找出窗体的编号
#                            窗口类名        窗口标题
QQwin = win32gui.findwindow("TXGuiFoundation","QQ")
#参数1：控制的窗体
#参数2：大致方位
#参数3：位置x
#参数4：位置y
#参数5：长度
#参数6：宽度

while True:
    x = random.randrange(900)
    y = random.randrange(600)
    win32gui.SetWindowPos(QQwin ,win32.con.HWND_TOPMOST,x,y,300,300,win32conSWP_SHOWWINDOW)

























