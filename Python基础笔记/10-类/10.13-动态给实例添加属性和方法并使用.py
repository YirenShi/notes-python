from types import MethodType
#用MethodType将方法绑定到类，并不是将这个方法直接写到类内部，而是在内存中创建一个link指向外部的方法，在创建实例的时候这个link也会被复制
#创建一个空类
class Person(object):
    __slots__ = ("name","age","speak")

#添加属性
per = Person()
#动态添加属性。，这体现了动态语言的特点（灵活）
per.name = "tom"
print(per.name)

#动态添加方法
"""
def say(self):
    print("mu name is " + self.name)
per.speak = say

per.speak()
"""

def say(self):
    print("my name is " + self.name)
per.speak =  MethodType(say,per)
per.speak()


#思考：如果我们想要限制实例的属性怎么办？？
#比如：只允许给对象添加name，age，height，weight属性

#per.height = 170
#print(per.height)




