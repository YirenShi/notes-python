import  csv

import win32com
import win32com.client


class  DealFile(object):
    #读取csv
    def readCsv(self,path):
        infoList = []
        with open (path,"r")as f :
            allFileInfo = csv.reader(f)
            for row in allFileInfo:
                infoList.append(row)
        return infoList
    #写csv
    #[["1","2","3"],["4","5","6"]]
    def writeCsv(self,path,data):
        with open(path,"w") as f:
            writer = csv.writer(f)
            for rowData in data:
                print("rowData = ", rowData)
                writer.writerow(rowData)
    #word
    def readWordFile(self,path):
        # 调用系统word功能，可以处理doc和docx两者文件
        mw = win32com.client.Dispatch("Word.Application")
        # 打开文件
        doc = mw.Documents.Open(path)
        for paragraphs in doc.Paragraphs:
            line = paragraphs.Range.Text
            print(line)
        # 关闭文件
        doc.Close()
        # 退出word
        mw.Quit()

