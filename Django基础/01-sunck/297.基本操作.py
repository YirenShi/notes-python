"""
基本操作
    1.设计表结构
        a.班级表结构
            1.表名  grades
            2.字段
                a.班级名称 gname
                b.成立时间 gdate
                c.女生总数 ggirlnum
                d.男生总数 gboynum
                e.是否删除 isDelete
        b.学生表结构
            1.表名  students
            2.字段
                a.姓名   sname
                b.性别   sgender
                c.年龄   sage
                d.简介   scontend
                e.所属班级 sgrade
                f.是否删除 isDelete
    2.配置数据库
        a.注意:Django默认使用SQlite数据
        b.在settings.py文件中，通过DATABASES选项进行数据库配置
        c.配置MySQL
            1.python3.x安装的是PyMYSQL
            2.在__init__.py文件中写入两行代码
            import pymysql
            pymysql.install_as_MySQLdb()
            3.
            'default': {
            'ENGINE': 'django.db.backends.mysql',  #修改为mysql
            'NAME': "sunck",    #数据库名
            'USER':'root',      #用户名
            'PASSWORD':'123',   #数据库密码
            'HOST':'localhost', #数据库服务器ip
            'PORT':'3306' ,      #端口  mysql 默认端口3306
           }

    3.创建应用
        a.在一个项目中，可以创建多个应用，每个应用进行一种业务处理
        b.打开黑屏终端，进入01-sunck目录下的project目录
        c.执行<python manage.py startapp myApp>
        d.myApp 目录说明
            1.admin.py    站点配置
            2.models.py   模型
            3.views.py    视图

    4.激活应用
        a.在settings.py文件中，将myApp应用加入到 INSTALLED_APPS 选项中
        b.      INSTALLED_APPS = [
                                    'django.contrib.admin',
                                    'django.contrib.auth',
                                    'django.contrib.contenttypes',
                                    'django.contrib.sessions',
                                    'django.contrib.messages',
                                    'django.contrib.staticfiles',
                                    'myApp'  #应用名称
                                    ]

    5.定义模型
        a.概述：有一个数据表，就对应有一个数据模型
        b. 在models.py文件中定义模型
            1.引入 from django.db import models
            2.模型类要继承models.Model类
            3.说明：不需要定义主键，在生成时自动添加，并且值为自动增加
            4.
from django.db import models

# Create your models here.

class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntergerField()
    gboynum = models.IntergerField()
    isDelete = models.BooleanFiled()

class Student(models.Model):
    sname = models.CharField(max_length = 20)
    sgender = models.Booleanfield(default = True)
    sage = models.IntegerField()
    scontend = models.CharField(max_lengeth = 20)
    isDelete = models.BooleanFiled(default = False)
    #关联外键方式变化，采用下面一行
    #sgrade = models.ForeignKey("Grades")
    # 英雄出现的书　一对多设计　多方持有一方的外键
    # hbook = models.ForeignKey(BookInfo)
    #hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    sgrade = models.ForeignKey('Grades', on_delete=models.CASCADE)


    6.在数据库中生成数据表
        a.生成迁移文件
            1.执行  <python manage.py makemigrations>   在migrations目录下生成迁移文件，此时数据库中还没有生成数据表
        b.执行迁移
            1.执行<python manage.py migrate>
            相当于执行mysql语句创建数据表

    7.测试数据操作
        a.进入到python shell
            1.执行<python manage.py shell>
            2.引入包
                a. from myApp.models import Grades,Student
                b.from django.utils import timezone
                c.from datetime import *
            3.查询所有数据
                a.Grades.objects.all()
                  格式类名.objects.all()
            4.添加数据
                a.本质：创建一个模型类的对象实例
                b.grade1 = Grades()
                c.grade1.gname = "python04"
                d.grade1.gdate = datetime(year = 2017,month = 7 ,day = 17)
                e.grade1.ggirlnum = 3
                f.grade1.gboynum = 70
                g.grade1.save()

            5.查看某个对象
                a.Grades.objects.all()
                b.g = Grades.objects.get(pk = 2)
            6.修改数据
                grade2.gboynum = 20
                grade2.save()
            7.删除数据
                a.模型对象deleted（）
                grade2.delete(0
                注意：物理删除，数据库中的表里的数据被删除了

            8.关联对象
                a.
                stu = Student()\
                stu.sname = "yiren"
                ....
                stu.sgrade =  grade2
                stu.save()

                b.获得关联对象的集合
                    1.获取python04班级的所有学生
                    关联的对象名小写——set.all()
                    grade2.student_set.all()

                c.需求：创建曾志伟，属于python04班级
                    stu3 =grade2.student_set.create(sname = u"曾志伟" ,sgender = True,scontend = u'我叫曾志伟',sage = 45)
                    注意：直接添加到数据库中了

    8.启动服务器
        a.格式
            1.python manage.py runserver ip:port
            2.说明  ip可以不写，不写的话说明代表本机ip
            3.端口号默认是8000
            4.python manager.py runserver   /      python manage.py runserver 127.0.0.1:8000
        b.说明
            1.这是一个python写的轻量级web服务器，仅仅在开发测试中使用

    9.Admin站点管理
        a.概述
            1.内容发布： 负责添加，修改，删除内容
            2.公告访问：
        b.配置Admin应用  在settings.py文件中的INSTALL_APP中添加   'django.contrib.admin'    默认是已经添加好
        c.创建管理员用户
            python manager.py createsuperuser
            Username :默认使用电脑名 sunck
            Email address:
            password:  1234567890a
        d.汉化
            settings.py 文件中最后修改
            LANGUAGE_CODE = 'zh-Hans'

            TIME_ZONE = 'Asia/Shanghai'
302
        e.管理数据表
            1.修改admin.py文件   添加
                from .models import Grades,Student
                #注册
                admin.site.register(Student)

                admin.site.register(Grades)
            2.自定义管理页面   admin.py 文件中添加
                class GradesAdmin(admin.ModelAdmin):
                #列表页属性
                list_display = []  #显示字段
                list_filter = []   #过滤字段
                search_fields = [] #搜索字段
                list_per_page = 5 #分页数  5行一页

                #添加，修改页属性
                fields = ['ggirlnum','gboynum','gname','gdate','isDelete']        #规定属性的先后顺序
                fieldsets = []    #给属性分组
                注意：fields 与 filedsets 不能同时使用

                #添加GradesAdmin至admin.site
                admin.site.register(Grades,GradesAdmin)
                class StudentAdmin(admin.ModelAdmin):
                list_display = ['pk','sname','sage','sgender','scontend','sgrade','isDelete']
                ist_per_page = 3
                admin.site.register(Student,StudentAdmin)
            3.关联对象
                a.需求：在创建一个新班级时可以直接添加几个学生
from .models import Grades,Student
#注册
class StudentInfo(admin.TabularInline):#  StackedInline 效果相同，页面显示不同而已
    model = Student
    extra = 2

class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentInfo]
    #列表页属性
    list_display = ['pk','gname','gdate','gdate','ggirlnum','gboynum','isDelete']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5

    #添加，修改页属性
    #fields = ['ggirlnum','gboynum','gname','gdate','isDelete']
    fieldsets = [
        ("num",{"fields":['ggirlnum','gboynum']}),
        ("base",{"fields":['gname','gdate','isDelete']})
    ]

admin.site.register(Grades,GradesAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['pk','sname','sage','sgender','scontend','sgrade','isDelete']
    list_per_page = 5
admin.site.register(Student,StudentAdmin)

---------------------------------------------------
            4.布尔值显示问题
class StudentAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女 "
    #修改页面列的名称
    gender.short_description = "性别"    #调用函数
    list_display = ['pk','sname','sage',gender,'scontend','sgrade','isDelete']
    list_per_page = 5
----------------------------------
            5.执行动作的位置
class StudentAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女 "
    #修改页面列的名称
    gender.short_description = "性别"   #调用函数
    list_display = ['pk','sname','sage',gender,'scontend','sgrade','isDelete']
    list_per_page = 5
    #执行动作的位置
    actions_on_top = False    ***
    actions_on_bottom = True   *******


admin.site.register(Student,StudentAdmin)

-----------------------
        使用装饰器完成注册
@admin.register(Student)    #******  等同于#admin.site.register(Student,StudentAdmin)
class StudentAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女 "
    #修改页面列的名称
    gender.short_description = "性别"   #调用函数
    list_display = ['pk','sname','sage',gender,'scontend','sgrade','isDelete']
    list_per_page = 5
    #执行动作的位置
    actions_on_top = False
    actions_on_bottom = True


#admin.site.register(Student,StudentAdmin)

------------------
视图的基本使用
    1.概述
        a.在django中，视图对web请求进行回应
        b.视图就是一个python函数，在views.py文件中定义

    2.定义视图

"""