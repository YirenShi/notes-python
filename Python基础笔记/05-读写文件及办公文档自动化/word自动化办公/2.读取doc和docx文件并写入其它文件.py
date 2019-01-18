import win32com
import win32com.client

def readWordFileToOtherFile(path,toPath):
    #调用系统word功能，可以处理doc和docx两者文件
    mw = win32com.client.Dispatch("Word.Application")
    #打开文件
    doc = mw.Documents.Open(path)

    #将word的数据保存到另一个文件
    doc.SaveAs(toPath,2)#2表示为txt文件

    #关闭文件
    doc.Close()
    #退出word
    mw.Quit()

path = r"C:\Users\Zhangyadi\Desktop\project\115word自动化办公\115test2.doc"
toPath =  r"C:\Users\Zhangyadi\Desktop\project\115word自动化办公\a.txt"
readWordFileToOtherFile(path,toPath)










































