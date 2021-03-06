from django.shortcuts import render,redirect
from django.core.mail import send_mail  #发送邮件
from celery_tasks.tasks import send_register_active_email
from django.contrib.auth import authenticate, login, logout  #django 认证系统
from django.core.urlresolvers import reverse #反向解析
from utils.mixin import LoginRequiredMixin  #Mixin
from django.views.generic import View
from user.models import User, Address
from goods.models import GoodsSKU
from django.http import HttpResponse
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer# pip install itsdangerous
from itsdangerous import SignatureExpired  #过期报错异常
from  django.conf import settings
import re
from user.models import User
import time
# Create your views here.
# /user/register
def register(request):
    '''注册'''
    #通过判断GET  POST 将url减少为一个
    if request.method == 'GET':
        # 显示注册页面
        return render(request, 'register.html')
    else:
        # 进行注册处理
        # 接收数据
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')

        # 进行数据校验
        if not all([username, password, email]):
            # 数据不完整
            return render(request, 'register.html', {'errmsg': '数据不完整'})

        # 校验邮箱
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})

        if allow != 'on':
            return render(request, 'register.html', {'errmsg': '请同意协议'})

        # 校验用户名是否重复
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # 用户名不存在
            user = None

        if user:
            # 用户名已存在
            return render(request, 'register.html', {'errmsg': '用户名已存在'})

        # 进行业务处理: 进行用户注册
        user = User.objects.create_user(username, email, password)
        user.is_active = 0
        user.save()

        # 返回应答, 跳转到首页
        return redirect(reverse('goods:index'))

def register_handle(request):
    '''进行注册处理'''
    # 接收数据
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')
    allow = request.POST.get('allow')

    # 进行数据校验
    if not all([username, password, email]):
        # 数据不完整
        return render(request, 'register.html', {'errmsg':'数据不完整'})

    # 校验邮箱
    if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        return render(request, 'register.html', {'errmsg':'邮箱格式不正确'})

    if allow != 'on':
        return render(request, 'register.html', {'errmsg':'请同意协议'})

    # 校验用户名是否重复
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        # 用户名不存在
        user = None

    if user:
        # 用户名已存在
        return render(request, 'register.html', {'errmsg':'用户名已存在'})

    # 进行业务处理: 进行用户注册
    user = User.objects.create_user(username, email, password)
    user.is_active = 0
    user.save()
    #发送激活邮件，包含激活链接：http://127.0.0.1:8000/user/active/id
    #激活连接中需要包含用户的身份信，并且要把身份信息进行加密

    # 返回应答, 跳转到首页
    return redirect(reverse('goods:index'))


from django.views.generic import View
from  django.conf import settings
class RegisterView(View):
    """注册"""
    def get(self,request):
        """显示注册页面"""
        return render(request,'register.html')
    def post(self,request):
        """进行注册处理"""
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')

        # 进行数据校验
        if not all([username, password, email]):
            # 数据不完整
            return render(request, 'register.html', {'errmsg': '数据不完整'})

        # 校验邮箱
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})

        if allow != 'on':
            return render(request, 'register.html', {'errmsg': '请同意协议'})

        # 校验用户名是否重复
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # 用户名不存在
            user = None

        if user:
            # 用户名已存在
            return render(request, 'register.html', {'errmsg': '用户名已存在'})

        # 进行业务处理: 进行用户注册
        user = User.objects.create_user(username, email, password)
        user.is_active = 0
        user.save()

        # 发送激活邮件，包含激活链接：http://127.0.0.1:8000/user/active/id
        # 激活连接中需要包含用户的身份信，并且要把身份信息进行加密

        #加密用户的身份信息，生成激活token
        serializer = Serializer(settings.SECRET_KEY,3600)
        info = {'confirm':user.id}
        token = serializer.dumps(info)   #  加密  bytes数据
        #token.decode('utf-8')#解码  默认utf-8 可不写
        #token = serializer.loads(info)  解密  正常解码，此处非这种解码方式
        token = token.decode() #解码后变为字符串

        #redis 无法确认版本号
        """
        # 发邮件               @app.task 装饰后有delay函数，可放入任务队列
        send_register_active_email.delay(email, username, token)

        # 返回应答, 跳转到首页
        return redirect(reverse('goods:index'))

        """
        #发邮件
        subject = '天天生鲜欢迎信息'  #标题
        message = ''  #正文，如正文html文件，不写
        sender = settings.EMAIL_FROM
        receiver = [email]   #recipient_list=收件人列表
        html_message = '正文'  #html正文
        #                           recipient_list=收件人列表
        send_mail(subject,message,sender,receiver,html_message =html_message)#阻塞信息，无法返回页面，需异步处理
        time.sleep(5)
        # 返回应答, 跳转到首页
        return redirect(reverse('goods:index'))


class ActiveView(View):
    """用户激活"""
    def get(self,request,token):
        """进行用户激活"""
        #进行解密，获取要激活的用户信息
        serializer = Serializer(settings.SECRET_KEY, 3600)
        try:
            serializer.loads(token)  #解密
            #获取待机或用的的id
            user_id = info['confirm']

            #根据id获取用户信息
            user = User.objects.get(id = user_id)
            user.is_active = 1
            user.save()

            #跳转到登录页面
            return redirect(reverse('user:login'))#反向解析

        except SignatureExpired as e:
            #激活链接已过期
            return HttpResponse('激活链接已过期')

# /user/login
class LoginView(View):
    '''登录'''
    def get(self, request):
        '''显示登录页面'''
        # 判断是否记住了用户名
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
            checked = 'checked'
        else:
            username = ''
            checked = ''

        # 使用模板
        return render(request, 'login.html', {'username':username, 'checked':checked})

    def post(self, request):
        '''登录校验'''
        # 接收数据
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        # 校验数据
        if not all([username, password]):
            return render(request, 'login.html', {'errmsg':'数据不完整'})

        # 业务处理:登录校验
        user = authenticate(username=username, password=password)
        if user is not None:
            # 用户名密码正确
            if user.is_active:
                # 用户已激活
                # 记录用户的登录状态
                login(request, user)

                # 获取登录后所要跳转到的地址
                # 默认跳转到首页
                next_url = request.GET.get('next', reverse('goods:index'))

                # 跳转到next_url
                response = redirect(next_url) # HttpResponseRedirect

                # 判断是否需要记住用户名
                remember = request.POST.get('remember')

                if remember == 'on':
                    # 记住用户名
                    response.set_cookie('username', username, max_age=7*24*3600)
                else:
                    response.delete_cookie('username')

                # 返回response
                return response
            else:
                # 用户未激活
                return render(request, 'login.html', {'errmsg':'账户未激活'})
        else:
            # 用户名或密码错误
            return render(request, 'login.html', {'errmsg':'用户名或密码错误'})


# /user/logout
class LogoutView(View):
    '''退出登录'''
    def get(self, request):
        '''退出登录'''
        # 清除用户的session信息
        logout(request)

        # 跳转到首页
        return redirect(reverse('goods:index'))


# /user
class UserInfoView(LoginRequiredMixin, View):
    '''用户中心-信息页'''
    def get(self, request):
        '''显示'''
        # Django会给request对象添加一个属性request.user
        # 如果用户未登录->user是AnonymousUser类的一个实例对象 ,返回false
        # 如果用户登录->user是User类的一个实例对象，返回True
        # request.user.is_authenticated()



        # 除了你给模板文件传递的模板变量之外，django框架会把request.user也传给模板文件
        return render(request, 'user_center_info.html', {'page':'user'})


# /user/order
class UserOrderView(LoginRequiredMixin, View):
    '''用户中心-订单页'''
    def get(self, request):
        '''显示'''
        # 获取用户的订单信息

        return render(request, 'user_center_order.html', {'page':'order'})


# /user/address
class AddressView(LoginRequiredMixin, View):
    '''用户中心-地址页'''
    def get(self, request):
        '''显示'''

        # 使用模板
        return render(request, 'user_center_site.html', {'page':'address', 'address':address})

    def post(self, request):
        '''地址的添加'''
        # 接收数据
        receiver = request.POST.get('receiver')
        addr = request.POST.get('addr')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')

        # 校验数据
        if not all([receiver, addr, phone]):
            return render(request, 'user_center_site.html', {'errmsg':'数据不完整'})

        # 校验手机号
        if not re.match(r'^1[3|4|5|7|8][0-9]{9}$', phone):
            return render(request, 'user_center_site.html', {'errmsg':'手机格式不正确'})

        # 业务处理：地址添加
        # 如果用户已存在默认收货地址，添加的地址不作为默认收货地址，否则作为默认收货地址
        # 获取登录用户对应User对象
        user = request.user

        # try:
        #     address = Address.objects.get(user=user, is_default=True)
        # except Address.DoesNotExist:
        #     # 不存在默认收货地址
        #     address = None

        address = Address.objects.get_default_address(user)

        if address:
            is_default = False
        else:
            is_default = True

        # 添加地址
        Address.objects.create(user=user,
                               receiver=receiver,
                               addr=addr,
                               zip_code=zip_code,
                               phone=phone,
                               is_default=is_default)

        # 返回应答,刷新地址页面
        return redirect(reverse('user:address')) # get请求方式
