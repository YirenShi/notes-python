from dealFile import DealFile


d = DealFile

toPath = r"C:\Users\Zhangyadi\Desktop\project\115word自动化办公\读写csv\yiren.csv"
for i in range(3,5):
    path = r"C:\Users\Zhangyadi\Desktop\project\115word自动化办公\读写csv\00" + str(i) + ".csv"
    listInfo = d.readCsv(path)
    d.writeCsv(toPath,listInfo)
allInfor = d.readCsv(toPath)

    #118   24   不能写入self？？？？







