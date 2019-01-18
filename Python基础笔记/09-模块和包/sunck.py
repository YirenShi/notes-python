#一个.py文件就是一个模块

#每一个模块都有一个 __name__ 属性,当其值等于"__mian__"时，表明该模块自身在执行,否则被引入其他文件
#当前文件如果为程序的入口文件，则__name__属性的值为__main__
#sunck   __name__作为文件执行是等于文件名
if __name__ == "__mian__":
    print("这是一个py文件")
else:
    print(__name__)##sunck   __name__作为文件执行是等于文件名
    def saygood():
        print("sunck is a good man")

    def saynice():
        print("sunck is a nice man")

    def sayhandsome():
        print("sunck is a handsome man")


#每一个py文件都有一个__name__属性,当其值等于__main__时，表明该模块自身在执行
#if __name__ =="__main__":
 #   print("这是sunck.py")
#else:
TT  = 100
