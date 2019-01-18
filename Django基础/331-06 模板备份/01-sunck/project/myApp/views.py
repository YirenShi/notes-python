from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect

#请求体
def index1(request):
    return HttpResponseRedirect("/sunck")
from .models import Student
def index(request):
    student = Student.objects.get(pk = 1)
    print(student)
    return render(request,'myApp/index.html',{"num" : 0})  #,"stu":student,



def attribles(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse("attribles")

#获取get传递的数据
def get1(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    return HttpResponse(a + " " + b + " " + c )
def get2(request):
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get('c')
    return HttpResponse(a1 + " " + a2 + " " + c)


#POST
def showregist(request):
    return render(request,'myapp/regist.html')

def regist(request):
    name = request.POST.get("name")
    gender = request.POST.get("gender")
    age = request.POST.get("age")
    hobby = request.POST.getlist("hobby")
    print(name)
    print(gender)
    print(age)
    print(hobby)
    return HttpResponse("safdsdf")

#response
def showresponse(request):
    res = HttpResponse()
    res.content = b'good'
    print(res.content)
    print(res.charset)
    print(res.status_code)
    print(res.content-type)
    return res

#cookie   324  未理解
def cookie(request):
    res = HttpResponse()
    cookie = request.COOKIES
    res.write("<h1>"+cookie["sunck"]+"</h1>")
    #cookie = res.set_cookie("sunck","good")  设置cookie值
    return res


#重定向

from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import redirect
def redirect1(request):
    #return HttpResponseRedirect('/sunck/redirect2')
    return redirect('sunck/redirect2')
def redirect2(request):
    #if request.is_ajax():
    #a = JsonResponse({})
    return HttpResponse("我是重定向后的视图")

#session
def main(request):
    #取session值
    username  = request.session.get('name',"游客")
    #print(username)
    return render(request,'myApp/main.html',{'username' : username})
def login(request):
    return render(request,'myApp/login.html')
def showmain(request):
    print("*****")
    username = request.POST.get('username')
    print("username = ", username)
    # 存储session
    request.session['name'] = username
    # return  render('showmain.html',{'A':request.session['name'] })
    #request.session.set_expiry(10)
    return redirect('/sunck/main/')
    #return render(request,'myApp/showmain.html',{'A':request.session['name'] })

from django.contrib.auth import logout
def quit(request):
    #清除session
    logout(request)
    #request.session.clear()
    #request.session.flush()
    return redirect('/sunck/main/')




def detail(request,num):
    return HttpResponse("detail-%s"%num)

from .models import Grades
def grades(request):
    #去模版里取数据
    gradesList = Grades.objects.all
    #将数据传递给模版,模版再渲染页面，将渲染好的页面返回给浏览器
    return  render(request,'myApp/grades.html',{"grades":gradesList})

from .models import Student
def student(request):
    studentsList = Student.objects.all()
    return render(request,'myApp/student.html',{'student':studentsList})

def gradesStudents(request,num):
    #获得对应的班级对象
    grade = Grades.objects.get(pk = num)
    #获得班级下的所有学生对象列表
    studentsList = grade.student_set.all()
    return render(request,'myApp/student.html',{"student":studentsList})





