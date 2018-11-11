class Person(object):
    name = ""
    age = "0"
    height = "0"
    weight = "0"
    def run(self):
        print("run")
    def eat(self,food):
        print("eat " + food)
    def openDoor(self):
        print("我以及打开冰箱门")
    def fillEle(self):
        print("我已经把大象装进冰箱")
    def closeDoor(self):
        print("我已经把门关上")

per = Person()

"""
访问属性
格式：对象名.属性名
赋值：对象名.属性名 = 新值
"""

per.name = "tom"
per.age = 18
per.height = 160
per.weight = 80

print(per.name,per.age,per.height,per.weight)


"""
访问方法
格式：对象名.方法名（参数列表）

"""
per.openDoor()
per.fillEle()
per.closeDoor()

per.eat("apple")

#问题：目前来看person创建的所有对象属性都是一样的


































