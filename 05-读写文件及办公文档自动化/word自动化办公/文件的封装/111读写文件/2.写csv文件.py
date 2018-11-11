import  csv

def writeCsv(path,data):
    with open(path,"w")as f:
        writer = csv.writer(f)
        #默认换行
        for rowData in data:
            print("rowData = ",rowData)
            writer.writerow(rowData)

path = r"C:\Users\Zhangyadi\Desktop\project\111读写文件\003.csv"
writeCsv(path,[["1","2","3"],["4","5","6"],["7","8","9"]])































