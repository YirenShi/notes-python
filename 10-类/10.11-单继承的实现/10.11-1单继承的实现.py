from student import Student
from person import Person
from worker import Worker

per = Person("a",1,2)
stu = Student("tom",18,1000,110)
print(stu.name,stu.age,stu.stuid)
#stu.stuFunc()    私有属性，会报错
#print(stu.__money)私有属性
print(stu.getMoney())#通过继承过来的共有方法访问所有属性，
print(per.getMoney())
#stu.run()
#stu1 = Worker("tom",18,1000)
#print(stu1.name,stu1.age)


























































