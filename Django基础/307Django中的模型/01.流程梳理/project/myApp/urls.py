from . import views
from django.conf.urls import url
urlpatterns = [
    url(r'^$',views.index,name = "index"),
    url(r'^students/$',views.students),
    url(r'^addstudent/$',views.addstudent),
    url(r'^addstudent2/$',views.addstudent2),
    url(r'^students2/$',views.students2),
    url(r'^students3/$',views.students3),
    url(r'^stu/(\d+)/$',views.stupage),
    url(r'^studentssearch/$',views.studentssearch),
    url(r'^grades/$',views.grades)
]