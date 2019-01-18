from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Students,Grades
def index(request):
    return HttpResponse("sunck is a good man")
    #return render(request, 'myApp/index.html')
def students(request):
    studentsList = Students.stuObj2.all()
    return render(request,'myApp/student.html',{"students":studentsList})
def students2(request):
    #报异常
    studentsList = Students.stuObj2.get(sgender = True)
    #return render(request,'myApp/student.html',{"students":studentsList})
    return HttpResponse("sunck is a good man")

#显示前5条同学
def students3(request):
    studentsList = Students.stuObj2.all()[0:5]
    return render(request,'myApp/student.html',{"students":studentsList})

#分页显示学生
def stupage(request,page):
    #0~5  5~10  10~15
    # 1     2       3
    page = int(page)
    studentsList = Students.stuObj2.all()[(page-1)*5:page*5]
    return render(request,'myApp/student.html',{"students":studentsList})

from django.db.models import Max
def studentssearch(request):
    studentsList = Students.stuObj2.filter(sname__contains = "03")
    #studentsList = Students.stuObj2.filter(sname__startswith = "yi")
    #studentsList = Students.stuObj2.filter(pk__in=[2,4,6])
    #studentsList = Students.stuObj2.filter(sage__gt=30)
    #描述中带有“06”的数据是属于哪个班级的
    grade = Grades.objects.filter(students__scontend__contains = "06")
    print(grade)
    #maxAge = Students.stuObj2.aggregate(Max('sage'))
    #print(maxAge)
    #studentsList = Students.stuObj2.filter(~Q(pk__lte = 3))
    return render(request,'myApp/student.html',{"students":studentsList})


def addstudent(request):
    grade = Grades.objects.get(pk = 1)
    stu = Students.createStudent("刘德华",34,True,"我叫刘德华",grade)
    stu.save()
    return HttpResponse("fsdf")

def addstudent2(request):
    grade = Grades.objects.get(pk = 1)
    stu = Students.stuObj2.createStudent("张学友",55,True,"我叫张学友",grade)
    stu.save()
    return HttpResponse("***")
from django.db.models import F,Q
def grades(request):
    #g = Grades.objects.filter(ggirlnum__gt = F('gboynum'))
    #print(g)
    Students.stuObj2.filter(Q(pk__lte = 3)|Q(sage__gt = 50))
    return  HttpResponse("0000")



















# 139183654920
# 15650709367
# 39256783 玉兰香苑4期 1700
#6             13855452689