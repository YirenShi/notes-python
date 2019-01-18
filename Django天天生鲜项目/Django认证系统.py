"""
使用Django认证系统

这篇文档解释默认配置下Django认证系统的使用。这些配置已经逐步可以满足大部分常见项目的需要，可以处理范围非常广泛的任务，且具有一套细致的密码和权限实现。对于需要与默认配置不同需求的项目，Django支持扩展和自定义认证。

Django的认证同时提供认证和授权，并通常统一称为认证系统，因为这些功能某些地方是耦合的。

User对象

User对象是认证系统的核心。它们通常表示与你的站点进行交互的用户，并用于启用限制访问、注册用户信息和给创建者关联内容等。在Django的认证框架中只存在一种类型的用户，因此诸如‘superusers‘或管理员‘staff‘用户只是具有特殊属性集的user对象，而不是不同类型的user对象。

默认user的基本属性有：

用户名
密码
电子邮件
名字
姓
完整的参考请参阅完整的API文档，以下的内容更偏重特定的任务。

创建user

创建users最直接的方法是使用create_user()辅助函数：

>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user(‘john‘, ‘lennon@thebeatles.com‘, ‘johnpassword‘)

# At this point, user is a User object that has already been saved
# to the database. You can continue to change its attributes
# if you want to change other fields.
>>> user.last_name = ‘Lennon‘
>>> user.save()
如果你已经安装了Django admin，你也可以交互式地创建users.

创建superusers

使用createsuperuser命令创建superusers：

$ python manage.py createsuperuser --username=joe --email=joe@example.com
将会提示你输入一个密码。在你输入一个密码后，该user将会立即创建。如果不带--username和--email选项，将会提示你输入这些值。

修改密码

Django不会在user模型上存储原始的（明文）密码，而只是一个哈希（完整的细节参见文档：密码是如何管理的）。因为这个原因，不要尝试直接操作user的password属性。这也是为什么创建一个user时要使用辅助函数。

若要修改一个用户的密码，你有几种选择：

manage.py changepassword *username*提供一种从命令行修改User密码的方法。它提示你修改一个给定user的密码，你必须输入两次。如果它们匹配，新的密码将会立即修改。如果你没有提供user，命令行将尝试修改与当前系统用户匹配的用户名的密码。

你也可以通过程序修改密码，使用set_password()：

>>> from django.contrib.auth.models import User
>>> u = User.objects.get(username=‘john‘)
>>> u.set_password(‘new password‘)
>>> u.save()
如果你安装了Django admin，你还可以在认证系统的admin页面修改user的密码。

Django还提供views和forms用于允许user修改他们自己密码。

New in Django 1.7.
如果启用了SessionAuthenticationMiddleware，修改user的密码将会登出他们所有的会话。 详细信息请参阅密码修改后会话失效。

认证Users

authenticate(**credentials)[source]?
请使用authenticate()，认证一组给定的用户名和密码。它接收关键字参数形式的凭证，使用默认配置时参数是username和password，如果密码能够匹配给定的用户名，它将返回一个User对象。如果密码无效，authenticate()返回None。例子：

from django.contrib.auth import authenticate
user = authenticate(username=‘john‘, password=‘secret‘)
if user is not None:
    # the password verified for the user
    if user.is_active:
        print("User is valid, active and authenticated")
    else:
        print("The password is valid, but the account has been disabled!")
else:
    # the authentication system was unable to verify the username and password
    print("The username and password were incorrect.")
注意:

这是认证一系列凭证的低级的方法；例如，它被RemoteUserMiddleware使用。除非你正在编写你自己的认证系统，否则你可能不会使用到它。当然如果你在寻找一种登录user的方法，请参见login_required()装饰器。

权限和授权

Django本身提供了一个简单的权限系统。它提供一种分配权限给特定的用户和用户组的方法。

它被Django的admin站点使用，但欢迎你在你自己的代码中使用。

Django admin 站点使用如下的权限：

拥有该类型对象"add"权限的用户才可以访问"add"表单以及添加一个该类型对象。
查看修改列表、查看“change”表单以及修改一个对象的权利只限于具有该类型对象的“change”权限的用户拥有。
用户必须在一个对象上具有“delete”权限，才能删除这个对象。
权限不但可以根据每个对象的类型，而且可以根据特定的对象实例设置。通过使用ModelAdmin类提供的has_add_permission()、has_change_permission()和has_delete_permission()方法，可以针对相同类型的不同对象实例自定义权限。

User对象具有两个多对多的字段：groups和user_permissions。User对象可以用和其它Django 模型一样的方式访问它们相关的对象：

myuser.groups = [group_list]
myuser.groups.add(group, group, ...)
myuser.groups.remove(group, group, ...)
myuser.groups.clear()
myuser.user_permissions = [permission_list]
myuser.user_permissions.add(permission, permission, ...)
myuser.user_permissions.remove(permission, permission, ...)
myuser.user_permissions.clear()
默认的权限?

当django.contrib.auth在你的INSTALLED_APPS设置中列出时，它将确保为你安装的应用中的每个Django模型创建3个默认的权限 – add、change和delete。

这些权限将在你运行manage.py migrate时创建；在添加django.contrib.auth到INSTALLED_APPS中之后，当你第一次运行migrate时，将会为之前安装的模型创建默认的权限，包括与此同时正在安装的新的模型。之后，每当你运行manage.py migrate时，它都将为新的模型创建默认的权限。

假设你有个app_label叫做foo的应用，这个应用有一个名为Bar的模型，要测试基本的权限，你应该使用：

add: user.has_perm(‘foo.add_bar‘)
change: user.has_perm(‘foo.change_bar‘)
delete: user.has_perm(‘foo.delete_bar‘)
很少直接访问Permission模型。

组

django.contrib.auth.models.Group模型是用户分类的一种通用的方式，通过这种方式你可以应用权限或其它标签到这些用户。一个用户可以属于任意多个组。

组中某个用户自动具有赋给那个组的权限。例如，如果组Site editors具有权限 can_edit_home_page，那么该组中的任何用户都具有该权限。

除权限之外，组还是给用户分类的一种方便的方法以给他们某些标签或扩展的功能。例如，你可以创建一个组‘Special users‘，然后你可以这样写代码，给他们访问你的站点仅限会员的部分，或者给他们发仅限于会员的邮件。

用程序创建权限

虽然自定义的权限可以定义在模型的Meta类中，你还可以直接创建权限。例如，你可以为myapp中的BlogPost 创建can_publish权限：

from myapp.models import BlogPost
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

content_type = ContentType.objects.get_for_model(BlogPost)
permission = Permission.objects.create(codename=‘can_publish‘,
                                       name=‘Can Publish Posts‘,
                                       content_type=content_type)
然后该权限可以通过user_permissions属性分配给一个User，或者通过permissions属性分配给Group。

权限的缓存

ModelBackend在第一次需要访问User对象来检查权限时会缓存它们的权限。这对于请求-响应循环还是比较好的，因为在权限添加进来之后并不会立即检查（例如在admin中）。如果你正在添加权限并需要立即检查它们，例如在一个测试或视图中，最简单的解决办法是从数据库中重新获取User。 例如：

from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404

def user_gains_perms(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # any permission check will cache the current set of permissions
    user.has_perm(‘myapp.change_bar‘)

    permission = Permission.objects.get(codename=‘change_bar‘)
    user.user_permissions.add(permission)

    # Checking the cached permission set
    user.has_perm(‘myapp.change_bar‘)  # False

    # Request new instance of User
    user = get_object_or_404(User, pk=user_id)

    # Permission cache is repopulated from the database
    user.has_perm(‘myapp.change_bar‘)  # True

    ...
Web请求中的认证

Django使用会话和中间件来拦截request 对象到认证系统中。

它们在每个请求上提供一个request.user属性，表示当前的用户。如果当前的用户没有登入，该属性将设置成AnonymousUser的一个实例，否则它将是User的实例。

你可以通过is_authenticated()区分它们，像这样：

if request.user.is_authenticated():
    # Do something for authenticated users.
    ...
else:
    # Do something for anonymous users.
    ...
如何登入一个用户

如果你有一个认证了的用户，你想把它附带到当前的会话中 - 这可以通过login()函数完成。

login()[source]?
从视图中登入一个用户，请使用login()。它接受一个HttpRequest对象和一个User对象。login()使用Django的session框架来将用户的ID保存在session中。

注意任何在匿名会话中设置的数据都会在用户登入后的会话中都会记住。

下面的示例向你演示如何使用authenticate() 和login()：

from django.contrib.auth import authenticate, login

def my_view(request):
    username = request.POST[‘username‘]
    password = request.POST[‘password‘]
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            # Return a ‘disabled account‘ error message
            ...
    else:
        # Return an ‘invalid login‘ error message.
        ...
先调用authenticate()：

当你是手工登入一个用户时，你必须在调用login()之前通过authenticate()成功地认证该用户。authenticate()在用户上设置一个属性，注意哪个认证后端成功验证了该用户（有关详细信息，请参阅后端文档），以及此信息以后在登录过程中需要。如果你试图登入一个直接从数据库中取出的用户，将会抛出一个错误。

如何登出一个用户

logout()[source]?
若要登出一个已经通过django.contrib.auth.login()登入的用户，可以在你的视图中使用django.contrib.auth.logout()。 它接收一个HttpRequest对象且没有返回值。例如：

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirect to a success page.
注意，即使用户没有登入，logout()也不会抛出任何错误。

当你调用logout()时，当前请求的会话数据将被完全清除。所有存在的数据都将清除。这是为了防止另外一个人使用相同的Web浏览器登入并访问前一个用户的会话数据。如果你想在用户登出之后>可以立即访问放入会话中的数据，请在调用django.contrib.auth.logout()之后放入。

只允许登录的用户访问

原始的方法

限制页面访问的简单、原始的方法是检查request.user.is_authenticated()并重定向到一个登陆页面：

from django.conf import settings
from django.shortcuts import redirect

def my_view(request):
    if not request.user.is_authenticated():
        return redirect(‘%s?next=%s‘ % (settings.LOGIN_URL, request.path))
    # ...
...或者显示一个错误信息：

from django.shortcuts import render

def my_view(request):
    if not request.user.is_authenticated():
        return render(request, ‘myapp/login_error.html‘)
    # ...
login_required 装饰器

login_required([redirect_field_name=REDIRECT_FIELD_NAME, login_url=None])[source]?
作为一个快捷方式，你可以使用便捷的login_required()装饰器：

from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    ...
login_required()完成下面的事情：

如果用户没有登入，则重定向到settings.LOGIN_URL，并将当前访问的绝对路径传递到查询字符串中。例如：/accounts/login/?next=/polls/3/。
如果用户已经登入，则正常执行视图。视图的代码可以安全地假设用户已经登入。
默认情况下，在成功认证后用户应该被重定向的路径存储在查询字符串的一个叫做"next"的参数中。如果对该参数你倾向使用一个不同的名字，login_required()带有一个可选的redirect_field_name参数：

from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name=‘my_redirect_field‘)
def my_view(request):
    ...
注意，如果你提供一个值给redirect_field_name，你非常可能同时需要自定义你的登录模板，因为存储重定向路径的模板上下文变量将使用redirect_field_name值作为它的键，而不是默认的"next"。

login_required()还带有一个可选的login_url参数。例如：

from django.contrib.auth.decorators import login_required

@login_required(login_url=‘/accounts/login/‘)
def my_view(request):
    ...
注意，如果你没有指定login_url参数，你需要确保settings.LOGIN_URL与你的登录视图正确关联。例如，使用默认值，可以添加下面几行到你的URLconf中：

from django.contrib.auth import views as auth_views

url(r‘^accounts/login/$‘, auth_views.login),
settings.LOGIN_URL同时还接收视图函数名和命名的URL模式。这允许你自由地重新映射你的URLconf中的登录视图而不用更新设置。

注

login_required装饰器不检查user的is_active标志位。

给已验证登录的用户添加访问限制

基于特定的权限和其他方式来限制访问，你最好按照前面描述的那样操作。

简单的方法就是在视图中直接运行你对request.user的测试。例如，视图检查用户的邮件属于特定的地址（例如@example.com），若不是，则重定向到登录页面。

from django.shortcuts import redirect

def my_view(request):
    if not request.user.email.endswith(‘@example.com‘):
        return redirect(‘/login/?next=%s‘ % request.path)
    # ...
user_passes_test(func[, login_url=None, redirect_field_name=REDIRECT_FIELD_NAME])[source]?
你可以用方便的 user_passes_test 装饰器，当回调函数返回 False 时会执行一个重定向操作：

from django.contrib.auth.decorators import user_passes_test

def email_check(user):
    return user.email.endswith(‘@example.com‘)

@user_passes_test(email_check)
def my_view(request):
    ...
user_passes_test() 要求一个以User 对象为参数的回调函数，若用户允许访问此视图，返回 True。注意，user_passes_test() 不会自动检查 User 是否为匿名对象。

user_passes_test()接收两个额外的参数：

login_url
让你指定那些没有通过检查的用户要重定向至哪里。若不指定其值，它可能是默认的 settings.LOGIN_URL。
redirect_field_name
与login_required()的参数相同。把它设置为 None 来把它从 URL 中移除，当你想把通不过检查的用户重定向到没有next page 的非登录页面时。
例如：

@user_passes_test(email_check, login_url=‘/login/‘)
def my_view(request):
    ...
permission_required 装饰器

permission_required(perm[, login_url=None, raise_exception=False])[source]?
检查一个用户是否有指定的权限是相对常见的需求。因此，Django 提供了一个快捷方式： permission_required() 装饰器：

from django.contrib.auth.decorators import permission_required

@permission_required(‘polls.can_vote‘)
def my_view(request):
    ...
has_perm() 方法, 权限名称采用如下方法 "<app label>.<permission codename>" (例如 polls.can_vote 表示在 polls 应用下一个模块的权限。

要注意permission_required() 也接受一个可选的login_url参数。例如：

from django.contrib.auth.decorators import permission_required

@permission_required(‘polls.can_vote‘, login_url=‘/loginpage/‘)
def my_view(request):
    ...
在 login_required() 装饰器中， login_url默认为settings.LOGIN_URL。

如果提供了 raise_exception 参数，装饰器抛出PermissionDenied异常，使用 the 403 (HTTP Forbidden) 视图而不是重定向到登录页面。

Changed in Django 1.7:
permission_required()装饰器既可以接收一个权限序列也可以接收一个单个的权限。

对普通的视图使用权限?

若要对一个基于类的普通视图使用权限，可以在该类上装饰View.dispatch方法。详细细节参见Decorating the class。 另外一个方法是编写一个封装as_view()的mixin。

密码更改后的会话失效

New in Django 1.7.
警告

这种保护只在MIDDLEWARE_CLASSES中SessionAuthenticationMiddleware开启的情况下应用。如果settings.py由Django ≥ 1.7. 的startproject生成，它会被包含进来。

会话验证在Django 2.0中将变成强制性的， 无论是否开启SessionAuthenticationMiddleware 。 如果你拥有一个1.7之前的项目，或者使用不包含SessionAuthenticationMiddleware的模板生成的项目，考虑在阅读下面的升级说明之后开启它。

如果你的AUTH_USER_MODEL继承自AbstractBaseUser，或者实现了它自己的get_session_auth_hash()方法，验证后的会话会包含这个函数返回的哈希值。在AbstractBaseUser的情况中，这是密码字段的HMAC。如果开启了SessionAuthenticationMiddleware ，Django会验证每个请求带有的哈希值是否匹配服务端计算出来的哈希值。这允许用户通过修改密码来登出所有的会话。

Django中包含的默认的密码修改视图，以及django.contrib.auth中的 django.contrib.auth.views.password_change()和user_change_password视图 ，会使用新的密码哈希值升级会话，以便用户在修改密码时不会登出。如果你拥有自定义的密码修改视图，并且希望具有相似的行为，使用这个函数：

update_session_auth_hash(request, user)
这个函数接受当前请求，并且会在会话哈希值得到的地方升级用户对象，也会适当地升级会话哈希值。使用示例：

from django.contrib.auth import update_session_auth_hash

def password_change(request):
    if request.method == ‘POST‘:
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        ...
如果你在升级一个现存的站点，并且希望开启这一中间件，而不希望你的所有用户之后重新登录，你可以首先升级到DJango1.7并且运行它一段时间，以便所有会话在用户登录时自然被创建，它们包含上面描述的会话哈希。一旦你使用SessionAuthenticationMiddleware开始运行你的站点，任何没有登录并且会话使用验证哈希值升级过的用户的现有会话都会失效，并且需要重新登录。

注意

虽然get_session_auth_hash()基于SECRET_KEY，使用新的私钥升级你的站点会使所有现有会话失效。

认证的视图

Django 提供一些视图，你可以用来处理登录、登出和密码管理。它们使用内建的认证表单，但你也可以传递你自己的表单。

Django 没有为认证视图提供默认的模板。你应该为你想要使用的视图创建自己的模板。模板的上下文定义在每个视图中，参见所有的认证视图.

使用视图

有几种不同的方法在你的项目中使用这些视图。最简单的方法是包含django.contrib.auth.urls 中提供的URLconf到你自己的URLconf中，例如

urlpatterns = [
    url(‘^‘, include(‘django.contrib.auth.urls‘))
]
这将包含进下面的URL模式：

^login/$ [name=‘login‘]
^logout/$ [name=‘logout‘]
^password_change/$ [name=‘password_change‘]
^password_change/done/$ [name=‘password_change_done‘]
^password_reset/$ [name=‘password_reset‘]
^password_reset/done/$ [name=‘password_reset_done‘]
^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name=‘password_reset_confirm‘]
^reset/done/$ [name=‘password_reset_complete‘]
这些视图提供了一个简单易记的URL名称。使用命名URL模式的细节请参见URL文档。

如果你想更多地控制你的URL，你可以在你的URLconf中引用一个特定的视图：

urlpatterns = [
    url(‘^change-password/‘, ‘django.contrib.auth.views.password_change‘)
]
这些视图具有可选的参数，你可以用来改变视图的行为。例如，如果你想修改一个视图使用的模板名称，你可以提供template_name 参数。一种方法是在URLconf 中提供关键字参数，它们将被传递到视图中。例如：

urlpatterns = [
    url(
        ‘^change-password/‘,
        ‘django.contrib.auth.views.password_change‘,
        {‘template_name‘: ‘change-password.html‘}
    )
]
所有的视图都返回一个TemplateResponse 实例，这让你在渲染前自定义响应很容易。一种方法是在你自己的视图中封装一个视图：

from django.contrib.auth import views

def change_password(request):
    template_response = views.password_change(request)
    # Do something with `template_response`
    return template_response
更多的细节，参见TemplateResponse文档。

所有的认证视图

下面列出了django.contrib.auth提供的所有视图。实现细节参见使用视图。

login(request[, template_name, redirect_field_name, authentication_form, current_app, extra_context])[source]?
URL 名称： login

关于使用命名URL模式的细节参见URL 文档。

可选的参数：

template_name: 用于用户登录视图的模板名。默认为registration/login.html。
redirect_field_name: GET字段的名称，包含登陆后重定向URL。默认为next。
authentication_form: 用于认证的可调用对象（通常只是一个表单类）。默认为AuthenticationForm。
current_app: 指示包含当前视图的是哪个应用。更多信息参见命名URL的解析策略。
extra_context: 一个上下文数据的字典，将被添加到传递给模板的默认上下文数据中。
下面是django.contrib.auth.views.login所做的事情：

如果通过 GET调用，它显示一个POST给相同URL的登录表单。后面有更多这方面的信息。
如果通过POST调用并带有用户提交的凭证，它会尝试登入该用户。如果登入成功，该视图重定向到next中指定的URL。如果next没有提供，它重定向到settings.LOGIN_REDIRECT_URL（默认为/accounts/profile/）。如果登入不成功，则重新显示登录表单。
你需要提供html模板给login，默认调用registration/login.html。模板会得到4个模板上下文变量：

form: 一个表示AuthenticationForm的Form对象。
next: 登入成功之后重定向的URL。它还可能包含一个查询字符串。
site: 如果你没有安装site框架，这将被设置成RequestSite的一个实例，它从当前的HttpRequest获得site名称和域名。
site_name: site.name的别名。如果你没有安装site框架，这将被设置成request.META[‘SERVER_NAME‘]的值。关于site 的更多信息，参见“sites” 框架。
如果你不喜欢调用registration/login.html，你可以通过额外的参数传递template_name参数给你URLconf中的视图。例如，下面URLconf中的行将使用myapp/login.html：

url(r‘^accounts/login/$‘, auth_views.login, {‘template_name‘: ‘myapp/login.html‘}),
通过传递redirect_field_name给视图，你还可以指定GET字段的值，它包含登入成功后的重定向的URL。默认情况下，该字段叫做next。

下面是一个registration/login.html模板的示例，你可以用它来作为起点。它假设你有一个定义了content块的base.html模板：

{% extends "base.html" %}

{% block content %}

{% if form.errors %}
<p>Your username and password didn‘t match. Please try again.</p>
{% endif %}

<form method="post" action="{% url ‘django.contrib.auth.views.login‘ %}">
{% csrf_token %}
<table>
<tr>
    <td>{{ form.username.label_tag }}</td>
    <td>{{ form.username }}</td>
</tr>
<tr>
    <td>{{ form.password.label_tag }}</td>
    <td>{{ form.password }}</td>
</tr>
</table>

<input type="submit" value="login" />
<input type="hidden" name="next" value="{{ next }}" />
</form>

{% endblock %}
如果你自定义认证（参见Customizing Authentication），你可以通过authentication_form参数传递一个自定义的认证表单给登录视图。该表单必须在它的__init__方法中接收一个request关键字参数，并提供一个get_user方法，此方法返回认证过的用户对象（这个方法永远只在表单验证成功后调用）。

logout(request[, next_page, template_name, redirect_field_name, current_app, extra_context])[source]?
登出一个用户。

URL名称： logout

可选的参数：

next_page: 登出之后要重定向的URL。
template_name: 用户登出之后，要展示的模板的完整名称。如果不提供任何参数，默认为registration/logged_out.html。
redirect_field_name: 包含登出之后所重定向的URL的GET字段的名称。默认为 next。如果提供了GET参数，会覆盖next_page URL。
current_app: 一个提示，表明哪个应用含有了当前视图。 详见 命名空间下的URL解析策略 。
extra_context: 一个上下文数据的字典，会被添加到向模板传递的默认的上下文数据中。
模板上下文：

title: 本地化的字符串“登出”。
site: 根据SITE_ID 设置的当前站点。如果你并没有安装站点框架，会设置为 RequestSite的示例，它从当前HttpRequest来获取站点名称和域名。
site_name: site.name的别名。如果没有安装站点框架，会设置为request.META[‘SERVER_NAME‘]。站点的更多信息请见“站点”框架。
current_app: 一个提示，表明哪个应用含有了当前视图。 详见 命名空间下的URL解析策略 。
extra_context: 一个上下文数据的字典，会被添加到向模板传递的默认的上下文数据中。
logout_then_login(request[, login_url, current_app, extra_context])[source]?
登出一个用户，然后重定向到登录页面。

URL 名称： 没有提供默认的URL

可选的参数：

login_url: 登录页面要重定向的URL。如果没有提供，默认为settings.LOGIN_URL。
current_app: 一个提示，表明哪个应用含有了当前视图。详见 命名空间下的URL解析策略 。
extra_context: 一个上下文数据的字典，会被添加到向模板传递的默认的上下文数据中。
password_change(request[, template_name, post_change_redirect, password_change_form, current_app, extra_context])[source]?
允许一个用户修改他的密码。

URL 名称： password_change

可选的参数：

template_name: 用来显示修改密码表单的template的全名。如果没有提供，默认为registration/password_change_form.html 。
post_change_redirect: 密码修改成功后重定向的URL。
password_change_form: 一个自定义的“修改密码”表单，必须接受user 关键词参数。表单用于实际修改用户密码。默认为 PasswordChangeForm。
current_app: 一个提示，暗示哪个应用包含当前的视图。详见 命名空间下的URL解析策略 。
extra_context: 上下文数据的字典，会添加到传递给模板的默认的上下文数据中。
模板上下文：

form: 密码修改表单（请见上面的password_change_form）。
password_change_done(request[, template_name, current_app, extra_context])[source]?
这个页面在用户修改密码之后显示。

URL 名称： password_change_done

可选参数：

template_name: 所使用模板的完整名称。如果没有提供，默认为registration/password_change_done.html。
current_app: 一个提示，暗示哪个应用包含当前的视图。 详见 命名空间下的URL解析策略 。
extra_context: 上下文数据的字典，会添加到传递给模板的默认的上下文数据中。
password_reset(request[, is_admin_site, template_name, email_template_name, password_reset_form, token_generator, post_reset_redirect, from_email, current_app, extra_context, html_email_template_name])[source]?
允许用户通过生成一次性的连接并发送到用户注册的邮箱地址中来重置密码。

如果提供的邮箱地址不在系统中存在，这个视图不会发送任何邮件，但是用户也不会收到任何错误信息。这会阻止数据泄露给潜在的攻击者。如果你打算在这种情况提供错误信息，你可以继承PasswordResetForm，并使用password_reset_form 参数。

用无效密码标记的用户（参见set_unusable_password()）不允许请求重置密码，为了防止使用类似于LDAP的外部验证资源时的滥用。注意它们不会收到任何错误信息，因为这会暴露它们的账户，也不会发送任何邮件。

URL 名称： password_reset

可选参数：

template_name: 用于显示密码重置表单的模板的完整名称。如果不提供，则默认为registration/password_reset_form.html。
email_template_name: 生成带有重置密码链接的电子邮件的模板的完整名称。如果不提供，则默认为registration/password_reset_email.html。
subject_template_name: 带有重置密码链接的电子邮件的标题模板的完整名称。如果不提供，则默认为registration/password_reset_subject.txt。
password_reset_form: 将用于获取要重置密码的用户的电子邮件的表单。默认为PasswordResetForm。
token_generator: 用于检查一次性链接的类的实例。默认为default_token_generator，它是 django.contrib.auth.tokens.PasswordResetTokenGenerator 的一个实例。
post_reset_redirect: 密码重置请求成功后，将重定向到的URL。
from_email: 一个有效的电子邮件地址。默认情况下Django 使用DEFAULT_FROM_EMAIL。
current_app: 指示哪个应用程序包含当前视图的提示。有关详细信息，请参阅namespaced URL resolution strategy。
extra_context: 将添加到传递给模板的默认上下文数据的上下文数据字典。
html_email_template_name: 用于使用密码重置链接生成text/html多部分电子邮件的模板的全名。默认情况下，不发送HTML电子邮件。
New in Django 1.7:
添加了html_email_template_name。

自1.8版起已弃用：is_admin_site参数已被废弃，将在Django2.0中被移除。

模板上下文：

form: 用于重置用户密码的表单（请参阅上面的password_reset_form）。
Email模板上下文：

email: user.email的别名
user: 根据email表单字段显示当前User。只有有效用户才能重置其密码（User.is_active 是 True）。
site_name: site.name的别名。如果您没有安装网站框架，则会将其设置为request.META[‘SERVER_NAME‘]的值。有关网站的详情，请参阅The “sites” framework。
domain: site.domain的别名。如果您没有安装网站框架，则会将其设置为request.get_host()的值。
protocol: http或https
uid: 用户的主键编码在base 64中。
token: 令牌检查重置链接是否有效。
registration/password_reset_email.html样例（邮件正文模板）：

Someone asked for password reset for email {{ email }}. Follow the link below:
{{ protocol}}://{{ domain }}{% url ‘password_reset_confirm‘ uidb64=uid token=token %}
主题模板使用了同样的模板上下文。主题必须是单行的纯文本字符串。

password_reset_done(request[, template_name, current_app, extra_context])[source]?
这个页面在向用户发送重置密码的邮件后展示。如果password_reset()视图没有显式设置 post_reset_redirectURL，默认会调用这个视图。

URL名称： password_reset_done

注意

如果提供的email地址在系统中不存在，用户未激活，或者密码不可用，用户仍然会重定向到这个视图，但是不会发送邮件。

可选参数：

template_name: 所使用模板的全名如果未提供，默认为registration/password_reset_done.html。
current_app: 指示哪个应用程序包含当前视图的提示。有关详细信息，请参阅命名空间网址解析策略。
extra_context: 将添加到传递给模板的默认上下文数据的上下文数据字典。
password_reset_confirm(request[, uidb64, token, template_name, token_generator, set_password_form, post_reset_redirect, current_app, extra_context])[source]?
为输入新密码展示表单。

URL名称： password_reset_confirm

可选参数：

uidb64: 用户的id以base 64编码。默认值为 None.
token: 令牌检查密码是否有效。默认为None。
template_name: 显示确认密码视图的模板的全名。默认值为registration/password_reset_confirm.html。
token_generator: 实例的类检查密码。这将默认为default_token_generator，它是django.contrib.auth.tokens.PasswordResetTokenGenerator的一个实例。
set_password_form: 将用于设置密码的表单。默认为SetPasswordForm
post_reset_redirect: 重置密码后重定向的网址。默认为None。
current_app: 指示哪个应用程序包含当前视图的提示。有关详细信息，请参阅命名空间网址解析策略。
extra_context: 将添加到传递给模板的默认上下文数据的上下文数据字典。
模板上下文：

form: 用于设置新用户密码的格式（参见上面的set_password_form）。
validlink: Boolean，如果链接（uidb64和token的组合）有效或未使用，则为True。
password_reset_complete(request[, template_name, current_app, extra_context])[source]?
展示一个视图，它通知用户密码修改成功。

URL名称： password_reset_complete

可选参数：

template_name: 显示视图的模板的全名。默认为registration/password_reset_complete.html。
current_app: 指示哪个应用程序包含当前视图的提示。有关详细信息，请参阅命名空间网址解析策略。
extra_context: 将添加到传递给模板的默认上下文数据的上下文数据字典。
辅助函数

redirect_to_login(next[, login_url, redirect_field_name])[source]?
重定向到登录页面，然后在登入成功后回到另一个URL。

必需的参数：

next: 登陆成功后重定向的URL
可选的参数：

login_url: 要重定向到的登录页面的URL。如果未提供，默认为settings.LOGIN_URL。
redirect_field_name: 包含要在注销后重定向的URL的GET字段的名称。如果传递给定的GET参数，则覆盖next。
内建的表单

如果你不想用内建的视图，但是又不想编写针对该功能的表单，认证系统提供了几个内建的表单，位于django.contrib.auth.forms：

注

内建的验证表单对它们处理的用户模型做了特定假设。如果你使用了自定义的用户模型，可能需要为验证系统定义你自己的表单。更多信息请见内建验证表单与自定义用户模型的使用的文档。

class AdminPasswordChangeForm[source]?
Admin 站点中使用的表单，用于修改用户密码。

接受user作为第一个参数。

class AuthenticationForm[source]?
用于用户登录的表单。

接受request 作为第一个参数，它将保存在表单实例中以在子类中使用。

confirm_login_allowed(user)[source]?
New in Django 1.7.
默认情况下，AuthenticationForm 将拒绝is_active 标志为False 的用户。你可以自定义这个行为来决定哪些用户可以登录。方法是使用一个自定义的表单，它子类化AuthenticationForm 并覆盖confirm_login_allowed 方法。如果给出的用户不能登录，这个方法应该引发一个ValidationError。

例如，若要允许所有用户登录而不管“is_active”状态如何：

from django.contrib.auth.forms import AuthenticationForm

class AuthenticationFormWithInactiveUsersOkay(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass
或者只允许某些激活的用户登录：

class PickyAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                _("This account is inactive."),
                code=‘inactive‘,
            )
        if user.username.startswith(‘b‘):
            raise forms.ValidationError(
                _("Sorry, accounts starting with ‘b‘ aren‘t welcome here."),
                code=‘no_b_users‘,
            )
class PasswordChangeForm[source]
用于用户修改密码的表单。

class PasswordResetForm[source]
用于生成并邮件发送重置密码的一个一次性链接的表单。

send_email(subject_template_name, email_template_name, context, from_email, to_email[, html_email_template_name=None])?
New in Django 1.8.
使用这些参数来发送EmailMultiAlternatives。可以覆盖这个方法，来自定义邮件如何发送给用户。

参数：
subject_template_name —— 邮件标题的模板。
email_template_name —— 邮件正文的模板。
context —— 传递给subject_template、email_template 和html_email_template 的上下文（如果它不为None）。
from_email —— 发信人的地址。
to_email —— 收件人的地址。
html_email_template_name —— HTML 格式的邮件正文的模板；默认为None，这种情况下将发送纯文本文件。
默认情况下，save() 方法向context 中添加的变量与password_reset() 向它的邮件上下文传递的变量相同。

class SetPasswordForm[source]
允许用户不输入旧密码修改密码的表单。

class UserChangeForm[source]
Admin 站点中使用的表单，用于修改用户信息和权限。

class UserCreationForm[source]
用于创建新用户的表单。

模板中的认证数据

当你使用RequestContext时，当前登入的用户和它们的权限在模板上下文中可以访问。

技术细节

技术上讲，这些变量只有在你使用RequestContext并启用了‘django.contrib.auth.context_processors.auth‘上下文处理器时才可以在模板上下文中访问到。它是默认产生的配置文件。更多信息，参见RequestContext 文档。

用户

当渲染RequestContext模板时，当前登录的用户，可能是User实例或者AnonymousUser实例，会存储在模板变量{{ user }}中：

{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}. Thanks for logging in.</p>
{% else %}
    <p>Welcome, new user. Please log in.</p>
{% endif %}
如果使用的不是RequestContext，则不可以访问该模板变量：

权限

当前登录的用户的权限存储在模板变量{{ perms }}中。这是个 django.contrib.auth.context_processors实例的封装，他是一个对于模板友好的权限代理。

在{{ perms }} 对象中，单一属性的查找是 User.has_module_perms的代理。如果已登录的用户在foo 应用中拥有任何许可，这个例子会显示 True：

{{ perms.foo }}
二级属性的查找是User.has_perm的代理。如果已登录的用户拥有foo.can_vote的许可，这个示例会显示True：

{{ perms.foo.can_vote }}
所以，你可以用模板的{% if %}语句检查权限：

{% if perms.foo %}
    <p>You have permission to do something in the foo app.</p>
    {% if perms.foo.can_vote %}
        <p>You can vote!</p>
    {% endif %}
    {% if perms.foo.can_drive %}
        <p>You can drive!</p>
    {% endif %}
{% else %}
    <p>You don‘t have permission to do anything in the foo app.</p>
{% endif %}
还可以通过{% if in %}语句查询权限。例如：

{% if ‘foo‘ in perms %}
    {% if ‘foo.can_vote‘ in perms %}
        <p>In lookup works, too.</p>
    {% endif %}
{% endif %}
在admin中管理用户

如果django.contrib.admin和django.contrib.auth这两个你都安装了，将可以通过admin方便地查看和管理用户、组和权限。可以像其它任何Django模型一样创建和删除用户。可以创建组，并分配权限给用户和组。admin中还会保存和显示对用户模型编辑的日志。

创建用户

在admin的主页，你应该可以在“Auth”部分看到“Users”链接。“Add user” 页面与标准admin页面不同点在于它要求你在编辑用户的其它字段之前先选择一个用户名和密码。

另请注意：如果你想使得一个用户能够使用Django的admin站点创建其它用户， 你需要给他添加用户和修改用户的权限（例如，"Add user” 和“Change user” 权限）。如果一个账号具有添加用户的权限但是没有权限修改他们，该账号将不能添加用户。为什么呢？因为如果你具有添加用户的权限，你将可以添加超级用户，这些超级用户将可以修改其他用户。所以Django同时要求添加权限和修改权限作为一种轻量的安全措施。

仔细考虑一下你是如何允许用户管理权限的。如果你赋予了一个非超级用户编辑用户的能力，这和给他们超级用户的权限在最终效果上是一样的，因为他们将能够提升他们自己下面的用户的权限。

修改密码

用户密码不会显示在admin上（也不会存储在数据库中），但是会显示密码存储的细节。 这个信息的显示中包含一条指向修改密码表单的链接，允许管理员修改用户的密码。

django 认证系统

标签：web   eating   try   print   一个人   中间件   adl   可调用对象   get


"""