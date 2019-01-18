import sys
import  importlib
importlib.reload(sys)

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManger, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed









def readPDF(path,toPath = ""):
    #以二进制形式打开PDF文件
    f = open(path,"rb")
    #创建一个PDF文档分析器
    parser = PDFParser(f)
    #创建一个PDF文档
    pdfFile = PDFDocument()

    #连接分析器与文档对象
    parser.set_document(pdfFile)
    #提供初始化密码
    pdfFile.initialize()

    #检测文档是否提供txt转换
    if not pdfFile.is_extractable:
        raise PDFTextExtractionNotAllowed  #不能转换，结束
    else:
        #解析数据
        #数据管理器
        manager = PDFResourceManger()
        #创建一个PDF设备的对象
        laparams = LAParams()
        device = PDFPageAggregator(manager,laparams = laparams)
        #解释器对象
        interpreter = PDFPageInterpreter(manager,device)
        #开始循环处理，每次处理一页
        for page in pdfFile.get_pages():
            interpreter.progcess_page(page)
            #处理图层
            layout = device.get_result()
            for x in layout:
                if (isinstance(x ,LTTextBoxHorizontal)):
                    if toPath == "":
                        #处理每行数据
                        print(str)
                    else:
                        #写文件
                        print("将PDF数据写入文件")





path = r"C:\Users\Zhangyadi\Desktop\project\111读写文件\PDF.pdf"
topath = r"C:\Users\Zhangyadi\Desktop\project\111读写文件\a.txt"

readPDF(path)








