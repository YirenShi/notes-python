import win32con
import win32gui
import time

#找出窗体的编号
#                            窗口类名        窗口标题
QQwin = win32gui.findwindow("TXGuiFoundation","QQ")

#显示窗体
win32gui.showWindow(QQwin,win32con.SW_SHOW)

#隐藏窗体
win32gui.showWindow(QQwin,win32con.SW_HIDE)

while True:
    QQwin = win32gui.findwindow("TXGuiFoundation","QQ")
    win32gui.showWindow(QQwin, win32con.SW_HIDE)
    time.sleep(1)
    win32gui.showWindow(QQwin, win32con.SW_SHOW)
    time.sleep(1)



































