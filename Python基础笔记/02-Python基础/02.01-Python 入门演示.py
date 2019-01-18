"""
简单的数学运算
整数相加，得到整数：

In [1]:
2 + 2
Out[1]:
4
浮点数相加，得到浮点数：

In [2]:
2.0 + 2.5
Out[2]:
4.5
整数和浮点数相加，得到浮点数：

In [3]:
2 + 2.5
Out[3]:
4.5
变量赋值
Python使用<变量名>=<表达式>的方式对变量进行赋值

In [4]:
a = 0.2
字符串 String
字符串的生成，单引号与双引号是等价的：

In [5]:
s = "hello world"
s
Out[5]:
'hello world'
In [6]:
s = 'hello world'
s
Out[6]:
'hello world'
三引号用来输入包含多行文字的字符串：

In [7]:
s = """hello
world"""
print s
hello
world
In [8]:
s = '''hello
world'''
print s
hello
world
字符串的加法：

In [9]:
s = "hello" + " world"
s
Out[9]:
'hello world'
字符串索引：

In [10]:
s[0]
Out[10]:
'h'
In [11]:
s[-1]
Out[11]:
'd'
In [12]:
s[0:5]
Out[12]:
'hello'
字符串的分割：

In [13]:
s = "hello world"
s.split()
Out[13]:
['hello', 'world']
查看字符串的长度：

In [14]:
len(s)
Out[14]:
11
列表 List
Python用[]来生成列表

In [15]:
a = [1, 2.0, 'hello', 5 + 1.0]
a
Out[15]:
[1, 2.0, 'hello', 6.0]
列表加法：

In [16]:
a + a
Out[16]:
[1, 2.0, 'hello', 6.0, 1, 2.0, 'hello', 6.0]
列表索引：

In [17]:
a[1]
Out[17]:
2.0
列表长度：

In [18]:
len(a)
Out[18]:
4
向列表中添加元素：

In [19]:
a.append("world")
a
Out[19]:
[1, 2.0, 'hello', 6.0, 'world']
集合 Set
Python用{}来生成集合，集合中不含有相同元素。

In [20]:
s = {2, 3, 4, 2}
s
Out[20]:
{2, 3, 4}
集合的长度：

In [21]:
len(s)
Out[21]:
3
向集合中添加元素：

In [22]:
s.add(1)
s
Out[22]:
{1, 2, 3, 4}
集合的交：

In [23]:
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
a & b
Out[23]:
{2, 3, 4}
并：

In [24]:
a | b
Out[24]:
{1, 2, 3, 4, 5}
差：

In [25]:
a - b
Out[25]:
{1}
对称差：

In [26]:
a ^ b
Out[26]:
{1, 5}
字典 Dictionary
Python用{key:value}来生成Dictionary。

In [27]:
d = {'dogs':5, 'cats':4}
d
Out[27]:
{'cats': 4, 'dogs': 5}
字典的大小

In [28]:
len(d)
Out[28]:
2
查看字典某个键对应的值：

In [29]:
d["dogs"]
Out[29]:
5
修改键值：

In [30]:
d["dogs"] = 2
d
Out[30]:
{'cats': 4, 'dogs': 2}
插入键值：

In [31]:
d["pigs"] = 7
d
Out[31]:
{'cats': 4, 'dogs': 2, 'pigs': 7}
所有的键：

In [32]:
d.keys()
Out[32]:
['cats', 'dogs', 'pigs']
所有的值：

In [33]:
d.values()
Out[33]:
[4, 2, 7]
所有的键值对：

In [34]:
d.items()
Out[34]:
[('cats', 4), ('dogs', 2), ('pigs', 7)]
数组 Numpy Arrays
需要先导入需要的包，Numpy数组可以进行很多列表不能进行的运算。

In [35]:
from numpy import array
a = array([1, 2, 3, 4])
a
Out[35]:
array([1, 2, 3, 4])
加法：

In [36]:
a + 2
Out[36]:
array([3, 4, 5, 6])
In [37]:
a + a
Out[37]:
array([2, 4, 6, 8])
画图 Plot
Python提供了一个很像MATLAB的绘图接口。

In [38]:
%matplotlib inline
from matplotlib.pyplot import plot
plot(a, a**2)
Out[38]:
[<matplotlib.lines.Line2D at 0x9fb6fd0>]

循环 Loop
In [39]:
line = '1 2 3 4 5'
fields = line.split()
fields
Out[39]:
['1', '2', '3', '4', '5']
In [40]:
total = 0
for field in fields:
    total += int(field)
total
Out[40]:
15
Python中有一种叫做列表推导式(List comprehension)的用法：

In [41]:
numbers = [int(field) for field in fields]
numbers
Out[41]:
[1, 2, 3, 4, 5]
In [42]:
sum(numbers)
Out[42]:
15
写在一行：

In [43]:
sum([int(field) for field in line.split()])
Out[43]:
15
文件操作 File IO
In [44]:
cd ~
d:\Users\lijin
写文件：

In [45]:
f = open('data.txt', 'w')
f.write('1 2 3 4\n')
f.write('2 3 4 5\n')
f.close()
读文件：

In [46]:
f = open('data.txt')
data = []
for line in f:
    data.append([int(field) for field in line.split()])
f.close()
data
Out[46]:
[[1, 2, 3, 4], [2, 3, 4, 5]]
In [47]:
for row in data:
    print row
[1, 2, 3, 4]
[2, 3, 4, 5]
删除文件：

In [48]:
import os
os.remove('data.txt')
函数 Function
Python用关键词def来定义函数。

In [49]:
def poly(x, a, b, c):
    y = a * x ** 2 + b * x + c
    return y

x = 1
poly(x, 1, 2, 3)
Out[49]:
6
用Numpy数组做参数x：

In [50]:
x = array([1, 2, 3])
poly(x, 1, 2, 3)
Out[50]:
array([ 6, 11, 18])
可以在定义时指定参数的默认值：

In [51]:
from numpy import arange

def poly(x, a = 1, b = 2, c = 3):
    y = a*x**2 + b*x + c
    return y

x = arange(10)
x
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
Out[51]:
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
In [52]:
poly(x)
Out[52]:
array([  3,   6,  11,  18,  27,  38,  51,  66,  83, 102])
In [53]:
poly(x, b = 1)
Out[53]:
array([ 3,  5,  9, 15, 23, 33, 45, 59, 75, 93])
模块 Module
Python中使用import关键词来导入模块。

In [54]:
import os
当前进程号：

In [55]:
os.getpid()
Out[55]:
4400
系统分隔符：

In [56]:
os.sep
Out[56]:
'\\'
- 类 Class
用class来定义一个类。 Person(object)表示继承自object类； __init__函数用来初始化对象； self表示对象自身，类似于C Java里面this。

In [57]:
class Person(object):
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    def full_name(self):
        return self.first + ' ' + self.last
构建新对象：

In [58]:
person = Person('Mertle', 'Sedgewick', 52)
调用对象的属性：

In [59]:
person.first
Out[59]:
'Mertle'
调用对象的方法：

In [60]:
person.full_name()
Out[60]:
'Mertle Sedgewick'
修改对象的属性：

In [61]:
person.last = 'Smith'
添加新属性，d是之前定义的字典：

In [62]:
person.critters = d
person.critters
Out[62]:
{'cats': 4, 'dogs': 2, 'pigs': 7}
网络数据 Data from Web
In [63]:
url = 'http://ichart.finance.yahoo.com/table.csv?s=GE&d=10&e=5&f=2013&g=d&a=0&b=2&c=1962&ignore=.csv'
处理后就相当于一个可读文件：

In [64]:
import urllib2
ge_csv = urllib2.urlopen(url)
data = []
for line in ge_csv:
    data.append(line.split(','))
data[:4]
Out[64]:
[['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close\n'],
 ['2013-11-05', '26.32', '26.52', '26.26', '26.42', '24897500', '24.872115\n'],
 ['2013-11-04',
  '26.59',
  '26.59',
  '26.309999',
  '26.43',
  '28166100',
  '24.88153\n'],
 ['2013-11-01',
  '26.049999',
  '26.639999',
  '26.030001',
  '26.540001',
  '55634500',
  '24.985086\n']]
使用pandas处理数据：

In [65]:
ge_csv = urllib2.urlopen(url)
import pandas
ge = pandas.read_csv(ge_csv, index_col=0, parse_dates=True)
ge.plot(y='Adj Close')
Out[65]:
<matplotlib.axes._subplots.AxesSubplot at 0xc2e3198>

"""