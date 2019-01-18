#编码
path = r"C:\Users\Zhangyadi\Desktop\project\54写文件1.txt"
with open(path,"wb")as f1:
    str = "sunck isa good man开"
    f1.write(str.encode("utf-8"))

with open(path,"rb")as f2:
    data = f2.read()
    print(data)
    print(type(data))
    newdata = data.decode("utf-8")
    print(newdata)
    print(type(newdata))
"""编码与解码格式不同会报错
with open(path,"rb"，"errors = ")as f2:
    data = f2.read()
    print(data)
    print(type(data))
    newdata = data.decode("gbk")
    print(newdata)
    print(type(newdata))
"""