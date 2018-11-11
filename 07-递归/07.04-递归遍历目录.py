import os

def getalldir(path,sp = " "):
    #得到当前目录下所有的文件
    fileslist = os.listdir(path)
    print(fileslist)
    #处理每一个文件
    sp +=" "
    for filename in fileslist:
        #path\filename
        #判断是否是路径（用绝对路径）
        joinpath = os.path.join(path,filename)
        if os.path.isdir(joinpath):
            print(sp + "目录",filename)
            #递归调用
            getalldir(joinpath,sp)
        else:
            print(sp +"普通文件",filename)
getalldir(r"C:\Users\Zhangyadi\Desktop\project\venv\Lib\site-packages\pip-10.0.1-py3.7.egg\pip\_internal")




































