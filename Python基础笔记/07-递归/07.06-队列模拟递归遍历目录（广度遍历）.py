import os
import collections

def getalldir(path):
    queue = collections.deque()
    #进队
    queue.append(path)

    while len(queue) != 0:
        #出队数据
        dirpath = queue.popleft()
        #找出所有的文件
        fileslist = os.listdir(dirpath)

        for filename in fileslist:
            #j绝对路径
            fileabspath = os.path.join(dirpath,filename)
            #判断是否是目录，是目录就进队，不是就打印
            if os.path.isdir(fileabspath):
                print("目录："+filename)
                queue.append(fileabspath)
            else:
                print("普通文件："+ filename)

getalldir(r"C:\Users\Zhangyadi\Desktop\project\venv\Lib\site-packages\pip-10.0.1-py3.7.egg\pip\_internal")



































