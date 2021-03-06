import os
"""
os：包含了普遍的操作系统的功能


"""
#nt---windows系统    posix---linux，Unix或Mac OS X
#获取操作系统 类型
print(os.name)


#print(os.unname)--打印操作系统详细的信息，windows不支持

#获取操作系统中的环境变量
print(os.environ)
#获取指定环境变量
print(os.environ.get("appdata"))

#获得当前目录    ./a/
print(os.curdir)

#获取当前工作目录，即当前python脚本所在的目录
print(os.getcwd())

#以列表的形式返回指定目录下所有文件
print(os.listdir(r"C:\Users\Zhangyadi\Desktop"))

#在当前目录下创建新目录
#os.mkdir("sunck")

#删除目录
#os.rmdir("sunck")

#获取文件属性
#print(os.stat("sunck"))

#重命名

#os.rename("sunck","kaige")

#删除普通文件
#os.remove("hello.py.txt")


#运行shell命令---记事本
#os.system("notepad")
#os.system("write")-写字板
#os.system("mspaint")--画板
#os.system("shutdown-s-t 500")-自动关机
#os.system("shutdown-a")-取消
#os.system("taskkill/f /im notepad.exe")--关闭




#有些方法存在os模块里，还有写存在与os.path
#查看当前的绝对路径
print(os.path.abspath("kaige"))

#拼接路径
p1 = r"C:\Users\Zhangyadi\Desktop\project"
p2 = "sunck"
#注意：参数2里开始不要有斜杠\
#C:\Users\Zhangyadi\Desktop\project\sunck
print(os.path.join(p1,p2))

p3 = "/root/sunck/home"
p4 = "kaige"
print(os.path.join(p3,p4))


#拆分路径
path2 = r"C:\Users\Zhangyadi\Desktop\project\kaige"
print(os.path.split(path2))
#获取扩展名
print(os.path.splitext(path2))

#判断是否是目录
print(os.path.isdir(path2))

#判断文件是否存在
path3 = r"C:\Users\Zhangyadi\Desktop\56fil6.txt"
print(os.path.isfile(path3))


#判断目录是否存在
print(os.path.exists(path2))

#获得文件大小(字节）
print(os.path.getsize(path3))

#获得文件的目录
print(os.path.dirname(path3))
print(os.path.basename(path3))#获取文件名



