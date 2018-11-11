"""
try & except 块
写代码的时候，出现错误必不可免，即使代码没有问题，也可能遇到别的问题。

看下面这段代码：

import math

while True:
    text = raw_input('> ')
    if text[0] == 'q':
        break
    x = float(text)
    y = math.log10(x)
    print "log10({0}) = {1}".format(x, y)
这段代码接收命令行的输入，当输入为数字时，计算它的对数并输出，直到输入值为 q 为止。

乍看没什么问题，然而当我们输入0或者负数时：

In [1]:
import math

while True:
    text = raw_input('> ')
    if text[0] == 'q':
        break
    x = float(text)
    y = math.log10(x)
    print "log10({0}) = {1}".format(x, y)
> -1
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-1-ceb8cf66641b> in <module>()
      6         break
      7     x = float(text)
----> 8     y = math.log10(x)
      9     print "log10({0}) = {1}".format(x, y)

ValueError: math domain error
log10 函数会报错，因为不能接受非正值。

一旦报错，程序就会停止执行，如果不希望程序停止执行，那么我们可以添加一对 try & except：

import math

while True:
    try:
        text = raw_input('> ')
        if text[0] == 'q':
            break
        x = float(text)
        y = math.log10(x)
        print "log10({0}) = {1}".format(x, y)
    except ValueError:
        print "the value must be greater than 0"
一旦 try 块中的内容出现了异常，那么 try 块后面的内容会被忽略，Python会寻找 except 里面有没有对应的内容，如果找到，就执行对应的块，没有则抛出这个异常。

在上面的例子中，try 抛出的是 ValueError，except 中有对应的内容，所以这个异常被 except 捕捉到，程序可以继续执行：

In [2]:
import math

while True:
    try:
        text = raw_input('> ')
        if text[0] == 'q':
            break
        x = float(text)
        y = math.log10(x)
        print "log10({0}) = {1}".format(x, y)
    except ValueError:
        print "the value must be greater than 0"
> -1
the value must be greater than 0
> 0
the value must be greater than 0
> 1
log10(1.0) = 0.0
> q
捕捉不同的错误类型
import math

while True:
    try:
        text = raw_input('> ')
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print "log10({0}) = {1}".format(x, y)
    except ValueError:
        print "the value must be greater than 0"
假设我们将这里的 y 更改为 1 / math.log10(x)，此时输入 1：

In [3]:
import math

while True:
    try:
        text = raw_input('> ')
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print "log10({0}) = {1}".format(x, y)
    except ValueError:
        print "the value must be greater than 0"
> 1
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-3-7607f1ae6af9> in <module>()
      7             break
      8         x = float(text)
----> 9         y = 1 / math.log10(x)
     10         print "log10({0}) = {1}".format(x, y)
     11     except ValueError:

ZeroDivisionError: float division by zero
因为我们的 except 里面并没有 ZeroDivisionError，所以会抛出这个异常，我们可以通过两种方式解决这个问题：

捕捉所有异常
将except 的值改成 Exception 类，来捕获所有的异常。

In [4]:
import math

while True:
    try:
        text = raw_input('> ')
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print "1 / log10({0}) = {1}".format(x, y)
    except Exception:
        print "invalid value"
> 1
invalid value
> 0
invalid value
> -1
invalid value
> 2
1 / log10(2.0) = 3.32192809489
> q
指定特定值
这里，我们把 ZeroDivisionError 加入 except 。

In [5]:
import math

while True:
    try:
        text = raw_input('> ')
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print "1 / log10({0}) = {1}".format(x, y)
    except (ValueError, ZeroDivisionError):
        print "invalid value"
> 1
invalid value
> -1
invalid value
> 0
invalid value
> q
或者另加处理：

In [6]:
import math

while True:
    try:
        text = raw_input('> ')
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print "1 / log10({0}) = {1}".format(x, y)
    except ValueError:
        print "the value must be greater than 0"
    except ZeroDivisionError:
        print "the value must not be 1"
> 1
the value must not be 1
> -1
the value must be greater than 0
> 0
the value must be greater than 0
> 2
1 / log10(2.0) = 3.32192809489
> q
事实上,我们还可以将这两种方式结合起来,用 Exception 来捕捉其他的错误：

In [7]:
import math

while True:
    try:
        text = raw_input('> ')
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print "1 / log10({0}) = {1}".format(x, y)
    except ValueError:
        print "the value must be greater than 0"
    except ZeroDivisionError:
        print "the value must not be 1"
    except Exception:
        print "unexpected error"
> 1
the value must not be 1
> -1
the value must be greater than 0
> 0
the value must be greater than 0
> q
得到异常的具体信息
在上面的例子中，当我们输入不能转换为浮点数的字符串时，它输出的是 the value must be greater than 0，这并没有反映出实际情况。

In [8]:
float('a')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-8-99859da4e72c> in <module>()
----> 1 float('a')

ValueError: could not convert string to float: a
为了得到异常的具体信息，我们将这个 ValueError 具现化：

In [9]:
import math

while True:
    try:
        text = raw_input('> ')
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print "1 / log10({0}) = {1}".format(x, y)
    except ValueError as exc:
        if exc.message == "math domain error":
            print "the value must be greater than 0"
        else:
            print "could not convert '%s' to float" % text
    except ZeroDivisionError:
        print "the value must not be 1"
    except Exception as exc:
        print "unexpected error:", exc.message
> 1
the value must not be 1
> -1
the value must be greater than 0
> aa
could not convert 'aa' to float
> q
同时，我们也将捕获的其他异常的信息显示出来。

这里，exc.message 显示的内容是异常对应的说明，例如

ValueError: could not convert string to float: a

对应的 message 是

could not convert string to float: a

当我们使用 except Exception 时，会捕获所有的 Exception 和它派生出来的子类，但不是所有的异常都是从 Exception 类派生出来的，可能会出现一些不能捕获的情况，因此，更加一般的做法是使用这样的形式：

try:
    pass
except:
    pass
这样不指定异常的类型会捕获所有的异常，但是这样的形式并不推荐。

自定义异常
异常是标准库中的类，这意味着我们可以自定义异常类：

In [10]:
class CommandError(ValueError):
    pass
这里我们定义了一个继承自 ValueError 的异常类，异常类一般接收一个字符串作为输入，并把这个字符串当作异常信息，例如：

In [11]:
valid_commands = {'start', 'stop', 'pause'}

while True:
    command = raw_input('> ')
    if command.lower() not in valid_commands:
        raise CommandError('Invalid commmand: %s' % command)
> bad command
---------------------------------------------------------------------------
CommandError                              Traceback (most recent call last)
<ipython-input-11-0e1f81a1136d> in <module>()
      4     command = raw_input('> ')
      5     if command.lower() not in valid_commands:
----> 6         raise CommandError('Invalid commmand: %s' % command)

CommandError: Invalid commmand: bad command
我们使用 raise 关键词来抛出异常。

我们可以使用 try/except 块来捕捉这个异常：

valid_commands = {'start', 'stop', 'pause'}

while True:
    command = raw_input('> ')
    try:
        if command.lower() not in valid_commands:
            raise CommandError('Invalid commmand: %s' % command)
    except CommandError:
        print 'Bad command string: "%s"' % command
由于 CommandError 继承自 ValueError，我们也可以使用 except ValueError 来捕获这个异常。

finally
try/catch 块还有一个可选的关键词 finally。

不管 try 块有没有异常， finally 块的内容总是会被执行，而且会在抛出异常前执行，因此可以用来作为安全保证，比如确保打开的文件被关闭。。

In [12]:
try:
    print 1
finally:
    print 'finally was called.'
1
finally was called.
在抛出异常前执行：

In [13]:
try:
    print 1 / 0
finally:
    print 'finally was called.'
finally was called.
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-13-87ecdf8b9265> in <module>()
      1 try:
----> 2     print 1 / 0
      3 finally:
      4     print 'finally was called.'

ZeroDivisionError: integer division or modulo by zero
如果异常被捕获了，在最后执行：

In [14]:
try:
    print 1 / 0
except ZeroDivisionError:
    print 'divide by 0.'
finally:
    print 'finally was called.'
divide by 0.
finally was called.
"""
"""


"""



#需求：当程序遇到问题是不让程序结束，而越过错误继续向下执行
"""
try.....excrpt.....else
格式：
try:
    语句t
except 错误代码 as e:
    语句1
except 错误代码 as e:
    语句2
    ......
except 错误代码 as e:
    语句n
else：#注意：else语句可有可无
    语句e
作用：用来检测try语句中的错误，从而让except语句捕获错误信息并处理
逻辑：当程序执行到try-except-else语句时
1.如果try语句t执行出现错误，会匹配第一个错误码，如果匹配上就执行对应的语句
2.如果try语句t执行出现错误，没有匹配的错误码，错误将会被提交到上一次的try语句
或者到程序的最上层
3.如果try语句t执行没有出现错误，执行else下的语句e（须有else）

"""
try:
    print(3 / 0)
except ZeroDivisionError as e:
    print("除数为0")
else:
    print("代码没有问题")

#使用except而不使用任何的错误类型
try:
    print(4/0)
except:
    print("程序出现了异常")


#使用except带着多种异常
try:
    pass
except(ZeroDivisionError , NameError):
    print("c出现了NameError或ZeroDivisionError")
print("***")
#特殊
#1.错误其实是class（类），所有的错误都继承自BaseException.所以在
#捕获的时候，他捕获了该类型的错误，还把子类一网打尽


try:
    print(5/0)
except BaseException as e:
    print("异常1")
except ZeroDivisionError as e :

    print("异常2")

#2.跨越多层调用，mian 调用了func1，func2调用了func1，func1出现错误，这时只要main捕获到了就可以处理
def func1(num):
    print(1/num)
def func2(num):
    func1(num)
def main():
    func2(0)
try:
    main()
except ZeroDivisionError as e:
    print("***")






