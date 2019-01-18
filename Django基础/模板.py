"""
2.定义模板
    1.变量：
        视图传递给模板的数据
        注意：要遵守标识符规则
        语法：{{varible}}
        注意：如果使用的变量不存在，则插入的是空字符串
        在模板中使用点语法
            字典
            属性或者方法
            数字索引
        在模板中调用对象的方法
            注意：在模板里不能传递参数
    2.标签
        a.语法      ｛%tag%｝
        b.作用
            在输出中创建文本
            控制逻辑和循环
        c.if
            格式：  {%if 表达式%}
                    语句
                    {%endif%}

                    {%if 表达式1%}
                    语句1
                    {%else %}
                    语句2
                    {%endif%}



                    {%if 表达式1%}
                    语句1
                    {%elif 表达式2%}
                    语句2
                    {%else %}
                    语句n

                    {%endif%}
            示例：
                    {%if num %}
                    <h1>sunck is a hgood man </h1>          num = 10 显示
                    {%endif%}


        d. for
            格式：
                {%for 变量 in 列表 %}
                语句
                {%endfor %}

                {%for 变量 in 列表 %}
                语句1
                {%empty %}
                语句2
                {%endfor %}
                注意：列表为空或者不存在时，执行语句2

                {{forloop.counter}}
                    表示当前是第几次循环


            示例:
    <ul>
        {%for students in student%}
            <li>
                {{forloop.counter}}--{{students.sname}}--{{students.sgrade}}
            </li>
        {% empty %}
            <li>目前没有学生</li>
        {% endfor %}
    </ul>


        e. comment
            格式：{%comment%}
                   注释的内容     多行注释
                   {%endcomment%}
        f. lfequal, ifnotequal
            作用：判断是否相等或者不相等
            格式：       {%ifequal 值1 值2 %}
                        语句
                        {%endifequal%}

                {% ifequal 'sunck' 'sunck'%}
                    <h1>sunck is a handsome man</h1>           #如果相等执行语句
                { % endifequal %}

        g. include
            作用：加载模板并以标签内的参数渲染
            格式：{% include 模板目录 参数1 参数2%｝
        h. url
            作用：反向解析
            格式：{%url'namespace:name' p1  p2%}
        i. csrf_token
            作用：用于跨站请求伪造保护的
            格式：{% csrf_token%}
        j. block, extends
            作用：用于模板的继承
        k. autoescape
            作用：用于html转义


    3.过滤器
        语法   {{var|过滤器}}
        作用：在变量被显示前修改它
        <h1>{{str|upper}}</h1>    将小写转换为大写，不修改内容

        lower  小写
        upper 大写
        过滤器可以传递参数，参数用引号引起来
            join
                格式：  {{列表|join：'#'}}
                示例： <h1>{{list|join:'#'}}</h1>

        如果一个变量没有被提供，或者值为false，空，可以使用默认值
            default
                格式：     {{var|default:'默认值'}}
                示例:     <h1>{{test|default:'没有'}}</h1>

        根据给定格式转换日期为字符串
            date
                格式：{{dateVal|date:'y-m-d}}

        HTML转义
            escape

        加减乘除
            <h1>num ={{num}}</h1>
            <h1>num ={{num|add:10}}</h1>
            <h1>num ={{num|add:-5}}</h1>
            <!--num/1*5-->
            <h1>num ={% widthratio num 1 5%}</h1>

            <!--num/5*1-->
            <h1>num ={% widthratio num 5 1%}</h1>
    4.注释
        单行注释
            语法：  {# 注释内容#｝
        多行注释：
            comment
                格式：{%comment%}
                       注释的内容     多行注释
                       {%endcomment%}

    5.反向解析
        myApp\url.py
        url 外加     app_name='app'     必须
        url(r'^good/(\d+)/$',views.good,name = 'good'),

        project\url.py
        url(r'^sunck/',include('myApp.urls',namespace = 'app')),

        index.html
        <a href = "{% url 'app:good' 1  %}">链接</a>
    6.  模板继承
        作用：模板继承可以减少页面的内容的重复定义，实现页面的重用

        block标签 ：
            1.在父模板中预留区域，子模板去填充
            2.语法  {%block 标签名 %}
                    {endblock 标签名%}

        extends标签：
            1.继承模板，需要写在模板文件的第一行
            2.语法：  ｛%extends '父模板路劲

        示例：
            定义父模板
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        #header{
            width:100%;
            height:100px;
            background-color:blue;
        }
    </style>
</head>
<body>
    <div id = "header">header</div>

    <div id  = "main">
        {%block  main%}


        {%endblock main%}
        <hr/>
        {% block mian2 %}         #无法实现

        {%endblock main2 %}

    </div>

    <div id = "footer">header</div>
</body>
</html>

            定义子模板
{%extends 'myApp/base.html'%}

{% block main %}
    <h1>sunck is a good man</h1>

{%endblock main%}

{% block mian2 %}

    <h1>kaige  is a good man</h1>        无法实现

{%endblock main2 %}


    7.HTML转义
        index.html     {{code}}
        views.py
def index(request):
    student = Student.objects.get(pk = 1)
    print(student)
    return render(request,'myApp/index.html',{"code":"<h1>sunck is a very good man <h1>"})

    直接将接受到的code当成普通字符串渲染
    将接受到的字符串当成HTML代码渲染
        1.{{code|safe}}
        2.      {% autoescape off %}      关闭自动转义
                {{code}}
                {% endautoescape %}


    8.CSRF
        跨站请求伪造
            某些恶意的网站包含链接、表达、按钮、js，利用登陆用户在浏览器中认证，从而攻击服务
        防止CSRF
            1.在settings.py文件中的  MIDDLEWARE  增加  'django.middleware.csrf.CsrfViewMiddleware',
            2.  postfile.py  加入   {% csrf_token %}

    9.验证码
        作用：
            1. 在用户注册、登录页面的时候使用，为了防止暴力请求，减轻服务器的压力
            2. 防止csrf一种方式

336#10
"""