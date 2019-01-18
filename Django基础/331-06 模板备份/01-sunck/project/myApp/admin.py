from django.contrib import admin

# Register your models here.
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

@admin.register(Student)
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