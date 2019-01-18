"""
1.将static静态文件添加到static文件夹中----为前端制作完成

2.将register.html文件放入templates文件夹下

3.views.py
def register(request):
    ""显示注册页面""
    return render(request,'register.html')

4.配置url
from user import views

urlpatterns = [
    url(r'^register$',views.register,name = 'register'),#注册

5.无法显示全部页面，须在register.html中增加
{% load staticfiles %}
并修改静态文件目录

{% load staticfiles %}
<head>
	<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
	<title>天天生鲜-注册</title>                  #修改处
	<link rel="stylesheet" type="text/css" href="{% static 'css/reset.css' %} ">
	<link rel="stylesheet" type="text/css" href="{% static 'css/main.css' %}">
	<script type="text/javascript" src="{% static 'js/jquery-1.12.4.min.js'%}"></script>
	<script type="text/javascript" src="{% static 'js/register.js'%}"></script>
</head>
<body>
	<div class="register_con">
		<div class="l_con fl">              ##修改处
			<a class="reg_logo"><img src="{% static 'images/logo02.png'%}"></a>


6.
<form method = "post" action = "user/register_handle">
	{%csrf_token%}



"""