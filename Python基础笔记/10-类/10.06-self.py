"""
self代表类的实例，而非类
哪个对象调用方法，那么该方法中的self就代表那个对象
self.__class__  代表类名

"""
class Person(object):
    def run(self):
        print("run")
        print(self.__class__)
        p = self.__class__("")
    def eat(self,food):
        print("eat " + food)
    def say(self):
        print("hello!my name is %a,I am %d years old" % (self.name, self.age))
        print(self.__class__)#<class '__main__.Person'>
    #self不是关键字，换成其他标识符也是可以的，但是帅人都是用self
    def play(a):
        print("play " + a.name)
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        pass

per1 = Person("tom",20,160,80)
per1.say()

per2 = Person("li",22,170,90)
per2.say()
per3 = Person("li",22,170,90)
per3.play()

