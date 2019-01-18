import csv


def readCsv(path):
    inForList = []
    with open(path,"r") as f:
        allFileInfor = csv.reader(f)
        print(allFileInfor)
        for row in allFileInfor:
            inForList.append(row)
    return inForList

path = r"C:\Users\Zhangyadi\Desktop\project\111读写文件\002.csv"
info = readCsv(path)































