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

class Student(models.Model):
    sname = models.CharField(max_length = 20)
    sgender = models.BooleanField(default = True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length = 20)
    isDelete = models.BooleanField(default = False)
    #关联外键方式变化，采用下面一行
    #sgrade = models.ForeignKey("Grades")
    # 英雄出现的书　一对多设计　多方持有一方的外键
    # hbook = models.ForeignKey(BookInfo)
    #hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    sgrade = models.ForeignKey('Grades', on_delete=models.CASCADE)
    def __str__(self):
        return self.sname
    def getName(self):
        return self.name