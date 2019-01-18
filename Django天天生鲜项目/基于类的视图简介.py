"""

介绍——基于类的视图（class-based view）
​刚开始的时候，django只有基于函数的视图（Function-based views）。为了解决开发视图中繁杂的重复代码，基于函数的通用视图（ Class-based generic views）出现了，但是不久它的弊端就显示出来：无法扩展、无法定制。基于函数的通用视图的不灵活导致它在现实世界中的应用受限。基于类的通用视图也是出于同样的目的被开发出来，它提供一个工具箱并支持多重继承，随着它的应用，人们发现它的可扩展性和灵活性远超它的小兄弟——基于函数的通用视图。
基于类的通用视图是基于函数的通用视图的质的飞跃，而不仅仅是改进

使用基于类的视图
一般而言，如果要对不同的HTTP请求做出不同的相应的话，function-based views会在单一的函数中采用判断分支的方法，比如：

1
2
3
4
5
6
7
8
9
from django.http import HttpResponse

def my_view(request):
    if request.method == 'GET':
        # <view logic>
        return HttpResponse('result')
    if request.method == 'POST':
        # <view logic>
        return HttpResponse('result')

而在class-based views中，你可以用不同的类实例的方法来响应不同的HTTP request，如：
1
2
3
4
5
6
7
8
9
10
from django.http import HttpResponse
from django.views.generic.base import View

class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')
    def post(self, request):
        # <view logic>
        return HttpResponse('result')

django的URL解析器需要将request和相应的参数传递给一个可调用的函数，而不是一个类。所以class-based view提供一个类方法：as_view()来解决这个问题，as_view()方法让你可以把类当做函数来调用。as_view创建一个类实例，然后调用它的dispatch方法，dispatch分析出request是GET、POST或者其他，然后将request匹配给相应的函数，比如将POST请求匹配给post()函数，如果给函数没有定义的话，将引发HttpResponseNotAllowed错误。

1
2
3
4
5
6
7
# urls.py
from django.conf.urls import patterns
from myapp.views import MyView

urlpatterns = patterns('',
    (r'^about/', MyView.as_view()),
)

虽然小型的class-based view并不需要依靠类属性来完成它的工作，但是类属性在很多的基于类的设计中都很有用。设置类属性有两个方法。
第一个方法是标准的python方法：在子类中重写类的属性和方法，比如：
1
2
3
4
5
6
7
8
from django.http import HttpResponse
from django.views.generic.base import View

class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)
你可以在子类中这样重写：
1
2
class MorningGreetingView(GreetingView):
    greeting = "Morning to ya"
第二个方法是在URLconf中将类属性作为参数传递给as_view()：
1
2
3
urlpatterns = patterns('',
    (r'^about/', GreetingView.as_view(greeting="G'day")),
)

使用mixins
mixin是多重继承的一种，它将父类的行为和属性结合在一起。比如说，在基于类的通用视图中，有一个mixin叫TemplateResponseMinxin，它原本的目的是定义方法render_to_response()。当与基础类View的行为结合时，结果是一个神奇的TemplateView类：它拥有分析request并作出相应匹配的方法（原本定义在View中的行为），也拥有一个接受一个template_name并返回一个TempalteReponse对象的render_to_response()方法（原本定义在 TemplateResponseMixin中的行为）

mixins是在不同的类之间重用代码的出色方法，但是它也带来了一些代价。也许你已经注意到了，如果你滥用这种方法的话，你将会迷失在mixin中，因为在冗长的继承树中，你很难辨清一个子类到底是用来干嘛的。

注意你只能从一个通用视图中继承，就是说，只能有一个父类是从View类继承来的。如果你在多个View类的子类中继承，比如尝试将ProsessFormView和ListView结合，结果将不会是你期待的那样。

用基于类的视图处理表格
一个基于函数的视图在处理表格时，看起来会像这样：

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import MyForm

def myview(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')
    else:
        form = MyForm(initial={'key': 'value'})

    return render(request, 'form_template.html', {'form': form})
而相似的基于类的视图会想这样：

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View

from .forms import MyForm

class MyFormView(View):
    form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
虽然只是一个简单的例子，但是你可以看到，你可以通过这样的方式来定制视图。比如通过URLconf配置重写类属性（像form_class），或者重写、继承一个或更多的方法。

装饰基于类的视图
class-based view的扩展并不局限于mixins，你也可以使用装饰器。由于基于类的视图不是函数，使用as_view或者创建子类将会以不同的方式了来装饰他们：

from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView

from .views import VoteView

urlpatterns = patterns('',
    (r'^about/', login_required(TemplateView.as_view(template_name="secret.html"))),
    (r'^vote/', permission_required('polls.can_vote')(VoteView.as_view())),
)
这是装饰一个实例的方法。如果你想装饰视图的每一个实例，你需要使用另一种方法。

装饰类
为了装饰基于类的视图的每一个实例，你需要装饰这个类本身。你可以将这个装饰器应用于类的dispatch()方法来达到这一目的。
类的方法和独立的方法并不完全一样，所以你不能直接将函数装饰器应用于类方法——你需要先将它转化成一个方法装饰器。method_decorator装饰器将一个函数装饰器转化成一个方法装饰器，这样一来，他就可以应用于实例的方法。例如：
1
2
3
4
5
6
7
8
9
10
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

class ProtectedView(TemplateView):
    template_name = 'secret.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedView, self).dispatch(*args, **kwargs)
"""