#进程模块
import win32process
#系统
import win32con
import win32gui
import win32api
import ctypes

PROCESS_ALL_ACCESS = (0x000F0000|0x00100000|0xFFF)

#找窗体
win = win32gui.findwindow("mianwindow","植物大战僵尸中文版")
#根据窗体找到进程号
hid,pid = win32process.getwindowthreadprocessid(win)

#以最高权限打开进程
p = win32api.openprocess(PROCESS_ALL_ACCESS,False,pid)
#data = ctypes.c_long()

#加载内核模块
                                                      #内核地址
md = stypes.windll.LoadLibrary("C:\\windows\\system32\\kernel32")

#读取内存
md.ReadProcessMemory(int(p),311944712.ctypes.byref(data))
print("data= ",data)

#新值
newdata = ctypes.c_long(10000)

#修改
md.WriteProcessMemory(int(p),311944712.ctypes.byref(newData),4,None)
















