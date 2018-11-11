"""def outer(func1):
    def inner(*arge,**jkhgkhj):
        #添加修改的功能
        print("%%%%")
        func1(*args,**jkhgkhj)
        return inner
"""
#say = outer(say)
#@outer
def say(name,age):#函数的次数理论上是无限制的，但实际上最好不要超过6~7个
    print("my name is %s,i am %d years old"%(name,age))
    return(say)
say("sunck",18)