import time
path = r"C:\Users\Zhangyadi\Desktop\project\54写文件1.txt"

f = open(path,"w")

#写文件
#1.将信息写入缓冲区
#f.write("sunck is a good man")
#2.刷新缓冲区
#直接把缓冲区的数据立刻写入文件，而不是被动的等待自动刷新缓冲区
#关闭文件也可刷新缓冲区写入
#f.flush()
"""
f.write("sunck is a good man")
f.flush()
while True:
    pass

f.close()
"""
while 1:
    f.write("sunck is a good man")
    f.flush()
    time.sleep(0.0001)
f.close()


with open(path,"a")as f2:
    f2.write("good man")


