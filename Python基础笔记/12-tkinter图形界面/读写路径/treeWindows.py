import tkinter
from tkinter import ttk
import os

class TreeWindows(tkinter.Frame):
    def __init__(self,master,path,otherWin):
        frame = tkinter.Frame(master)
        frame.grid(row = 0, column = 0)
        #保存
        self.otherWin = otherWin
        # 创建一个树状结构
        self.tree = ttk.Treeview(frame)
        #                 滚动条
        self.tree.pack(side = tkinter.LEFT,fill = tkinter.Y)
        # os.path.splitext(path)  将路径的最后一级分离出来,windows 系统无法使用
        # print(os.path.splitext(path))
        tempPath = self.getLastPath(path)
                                                        #是否显示，默认显示
        root = self.tree.insert("","end",text = tempPath,open = True,values = (path))
        self.loadTree(root,path)

        #滚动条
        self.sy = tkinter.Scrollbar(frame)
        self.sy.pack(side = tkinter.RIGHT,fill = tkinter.Y)
        #配置
        self.sy.config(command = self.tree.yview)
        self.tree.config(yscrollcommand = self.sy.set)

        #绑定事件
        self.tree.bind("<<TreeviewSelect>>",self.func)

    #设置功能
    def func(self,event):
        self.v = event.widget.selection()
        for sv in self.v:
            file = self.tree.item(sv)["text"]
            self.otherWin.ev.set(file)
            apath = self.tree.item(sv)["values"][0]
            print(apath)



    #遍历目录
    def loadTree(self,parent,parentPath):
        for fileName in os.listdir(parentPath):
            absPath = os.path.join(parentPath,fileName)
            #插入树枝
            treey = self.tree.insert(parent,"end",text = self.getLastPath(absPath),values = (absPath))
            #判断是否是目录
            if os.path.isdir(absPath):
                self.loadTree(treey,absPath)

    def getLastPath(self, path):
        pathList = os.path.split(path)
        #print("***")
        #print(pathList)
        return pathList[-1]

































