
#有序字典
from collections import OrderedDict
#写入数据
from pyexcel_xls import save_data

def makeExcelFile(path,data):
    dic = OrderedDict()
    for sheetName,sheetValue in data.items():
        d = {}
        d[sheetName] = sheetValue
        dic.update(d)

    save_data(path,dic)

path = path = r"C:\Users\Zhangyadi\Desktop\project\115word自动化办公\b.xls"#xlsx不可用
makeExcelFile(path,{"表1" : [[1,2,3],[4,5,6],[7,8,9]],"表2": [[11,22,33],[44,55,66],[77,78,79]]})




























