"""
重写：将函数重新定义写一遍

__str__()    在调用print打印对象时自动调用，是给用户用的，是一个描述对象的方法
__repr__()   给机器用的，在python解释器（cmd）里直接敲对象名在回车后调用的方法
注意：在没有__str__时，且有__repr, __repr__ = __str__
"""

class Person(object):

    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def __str__(self):
        return"%s-%d-%d-%d"%(self.name,self.age,self.height,self.weight)

per = Person("hanmeimei", 20, 170, 80)
#print(per.name,per.age,per.height,per.weight)

print(per)

#优点：当一个对象的属性值很多，并且都需要打印，重写了__str__方法后，简化了代码



#晚间作业，人开枪射击子弹（面向对象）

















