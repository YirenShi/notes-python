"""
概念：允许i函数调用时参数的顺序与定义时不一致

"""
def myprint(str , age):
   print(str , age)
a = 18
#使用关键字参数
myprint(age =a ,str = "sunck is a good man")


"""
默认参数
概念：调用函数时，如果没有传递参数，则使用默认参数
"""
def myprint(str="sunck is a good man" , age="18"):
   print(str , age)

myprint()
#要使用默认参数，最好将默认参数放在最后
def myprint(str , age =  17):
   print(str , age)
myprint(17)