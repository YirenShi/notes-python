class Person(object):

    def run(self):
        print(self.__money)
        print("run")

    def eat(self, food):
        print("eat " + food)
    def __init__(self,name,age,height,weight,money):
        self.name = name
        self.__age__ = age
        self._height = height
        self.weight = weight
        self.__money = money#私有属性        _Person__money
        #通过内部的方法，去修改私有属性
        #通过自定义的方法实现对私有属性的赋值与取值
    def setMoney(self,money):
    #数据的过滤
        if money <0:
            money = 0
        self.__money = money
    def getMoney(self):
        return self.__money
per = Person("hanmeimei", 20, 170, 80,1000)

per.age = 10
print(per.age)

#如果要让内部的属性不被外部直接访问
#下划线（  __ ),在python中如果在属性前加两个下划线，那么这个属性就变成了私有属性
#per.__money = 0
#per.run()
#print(per.__money)

per.setMoney(10)
print(per.getMoney())

#不能直接访问per.__money是因为Python解释器把__money变成了Person__money
#仍然可以用 Person__money去访问，但是强烈建议不要怎么干（帅的人都不怎么干）不同版本解释器可能存在解释的变量名不一致
#per.__money
per._Person__money = 1
print(per.getMoney())

#在Python中 __XXX__  属于特殊变量，可以直接访问

print(per.__age__)

#在Python中  _XXX  变量，这样的实例变量，外部也是可以访问的
#但是按照约定的规则，当我们看到这样的变量是，意思是“虽然我可以被访问，但是请把我视为私有变量，不要直接访问我”
print(per._height)










































