"""
概念：能处理比定义时更多的参数

"""
#加了星号（*）的变量存放所有未命名的变量参数，如果在函数调用时没有指定参数，
#他就是一个空元组
def fun (name,*arr):
    print(name)
    for x in arr:
        print(x)
fun("sunck","is","a")

def mysum(*l):
    sum = 0
    for i in l:
        sum += i
    return sum
print(mysum(1,2,3,4))


#  **代表键值对的参数字典，和*所代表的意义类似
def fun2(**args):#不确认使用args
    print(args)
    print(type(args))

#fun2(1,2,3)#必须使用关键字参数，key-value
fun2(x = 1,y = 2,z = 3)

def fun3(*args,**kjhkj):
    pass#代表一个空语句



















