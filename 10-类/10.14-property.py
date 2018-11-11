
class Person(object):
    def __init__(self,name,age):
        #属性直接对外暴露
        #self.age = age
        #限制访问
        self.__name = name
        self.__age = age

        """
    def getAge(self):
        return self.__age
    def setAge(self,age):
        if age < 0:
            age = 0
        self.__age = age
        """
    #方法名为受限制的变量去掉下划线
    @property
    def age(self):  #set方法
        return self.__age
    @age.setter   #去掉下划线.setter
    def age(self,age):   #get方法
        if age <0:
            age = 0
        self.__age = age

    @property
    def name(self):  # set方法
        return self.__name

    @age.setter  # 去掉下划线.setter
    def name(self, name):  # get方法
        self.__name = name


#不安全，没有数据的过滤
per = Person("sunck",-18)
#print(per.age)

#使用限制访问，需要自己写set&get方法才能访问
#per.setAge(15)
#print(per.getAge())

per.age = -100 #相对于调用setAge
print(per.age)#相对于调用

print(per.name)

#property：可以让你受限制访问的属性使用的语法







