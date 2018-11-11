
#有序字典
from collections import OrderedDict
#读取数据
from pyexcel_xls import get_data



def readXlsAndXlsxFile(path):
    dic = OrderedDict()

    #抓取数据
    xdata = get_data(path)

    for sheet in xdata:
        dic[sheet] = xdata[sheet]
    return dic


path = r"C:\Users\Zhangyadi\Desktop\project\115word自动化办公\sunck.xls"
dic = readXlsAndXlsxFile(path)
print(dic)
print(len(dic))













