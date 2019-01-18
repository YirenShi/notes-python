
import os
def getalldirde(path):
    stack = []
    stack.append(path)

    #处理栈：当栈为空的时候结束循环
    while len(stack) != 0:
        #从栈里取出数据
        dirpath = stack.pop()
        #目录下所有文件
        fileslist = os.listdir(dirpath)
        #处理每一个文件，如果是普通文件则打印出来，如果是目录，则将该目录的地址压栈

        for filename in fileslist:
            fileabspath = os.path.join(dirpath,filename)
            if os.path.isdir(fileabspath):
                #是目录就压栈
                print("目录："+filename)
                stack.append(fileabspath)
            else:
                #d打印普通文件
                print("普通："+filename)

getalldirde(r"C:\Users\Zhangyadi\Desktop\project\venv\Lib\site-packages\pip-10.0.1-py3.7.egg\pip\_internal")
































