from django.db import models

# Create your models here.



class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default = False)
    def __str__(self):
        return self.gname
    class Meta:
        db_table = "grades"
        ordering = ["-id"]
class StudentsManager(models.Manager):
    def get_queryset(self):
        return super(StudentsManager,self).get_queryset().filter(isDelete = False)
    #创建对象
    def createStudent(self,name,age,gender,contend,grade,isD = False):
        stu  = self.model()  #创建一个学生
        #print(type(grade))   #class.models.Students
        stu.sname = name
        stu.sage = age
        stu.sgender = gender
        stu.scontend = contend
        stu.sgrade = grade
        stu.isDelete = isD
        return stu


class Students(models.Model):
    #定义一个类方法创建对象
    @classmethod
        #         代表students类
    def createStudent(cls,name,age,gender,contend,grade,isD = False):
        stu = cls(sname = name,sage = age,sgender = gender,scontend = contend,sgrade = grade,isDelete = isD)
        return stu
    #自定义模型管理器
    stuObj = models.Manager()
    stuObj2 = StudentsManager()
    #当自定义模型管理器，objects就不存在了

    sname = models.CharField(max_length = 20)
    sgender = models.BooleanField(default = True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length = 20)
    isDelete = models.BooleanField(default = False)
    #关联外键方式变化，采用下面一行
    #sgrade = models.ForeignKey("Grades")    无法执行使用下面选项
    # 英雄出现的书　一对多设计　多方持有一方的外键
    # hbook = models.ForeignKey(BookInfo)
    #hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    sgrade = models.ForeignKey('Grades', on_delete=models.CASCADE)
    def __str__(self):
        return self.sname

    class Meta:
        db_table = "students"
        ordering = ["id"]



