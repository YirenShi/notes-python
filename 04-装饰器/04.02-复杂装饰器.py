

#def say(name):
#    print("%s is a good man"%(name))

#say("sunck")





def outer(func1):
    def inner(age):
        if age <0:
            age = 0
        func1(age)
    return inner
#使用@符号将装饰器应用到函数
#@python2.4支持使用@符号
@outer   #相当于say = outer((say)
#say = outer(say)
def say(age):
    print("sunck is %d years old"%(age))
say(-10)