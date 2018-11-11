"""
概念：是一个闭包，把一个函数当作参数,返回一个替代版的函数，本质上就是一个返回函数的函数

"""
#简单的装饰器
def fun1():
    print("sunck is a good man")

def outer(func):
    def inner():
        print("*******")
        func()
    return inner()
f = outer(fun1)