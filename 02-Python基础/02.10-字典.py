"""
字典 dictionary ，在一些编程语言中也称为 hash ， map ，是一种由键值对组成的数据结构。

顾名思义，我们把键想象成字典中的单词，值想象成词对应的定义，那么——

一个词可以对应一个或者多个定义，但是这些定义只能通过这个词来进行查询。

和list比较
1.查找和插入的速度极快，不会随着key-value的增加而变慢
2.需要占用大量的内存，内存浪费多--需存储key值

list
1.查找和插入的速度会随着数据量的增多而减慢
2.占用的空间少，浪费空间少



基本操作
空字典
Python 使用 {} 或者 dict() 来创建一个空的字典：

In [1]:
a = {}
type(a)
Out[1]:
dict
In [2]:
a = dict()
type(a)
Out[2]:
dict
有了dict之后，可以用索引键值的方法向其中添加元素，也可以通过索引来查看元素的值：

插入键值
In [3]:
a["one"] = "this is number 1"
a["two"] = "this is number 2"
a
Out[3]:
{'one': 'this is number 1', 'two': 'this is number 2'}
查看键值
In [4]:
a['one']
Out[4]:
'this is number 1'
更新键值
In [5]:
a["one"] = "this is number 1, too"
a
Out[5]:
{'one': 'this is number 1, too', 'two': 'this is number 2'}
初始化字典
可以看到，Python使用key: value这样的结构来表示字典中的元素结构，事实上，可以直接使用这样的结构来初始化一个字典：

In [6]:
b = {'one': 'this is number 1', 'two': 'this is number 2'}
b['one']
Out[6]:
'this is number 1'
字典没有顺序
当我们 print 一个字典时，Python并不一定按照插入键值的先后顺序进行显示,因为字典中的键本身不一定是有序的。

In [7]:
print a
{'two': 'this is number 2', 'one': 'this is number 1, too'}
In [8]:
print b
{'two': 'this is number 2', 'one': 'this is number 1'}
因此，Python中不能用支持用数字索引按顺序查看字典中的值，而且数字本身也有可能成为键值，这样会引起混淆：

In [9]:
# 会报错
a[0]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-9-cc39af2a359c> in <module>()
      1 # 会报错
----> 2 a[0]

KeyError: 0
键必须是不可变的类型
出于hash的目的，Python中要求这些键值对的键必须是不可变的，而值可以是任意的Python对象。

一个表示近义词的字典：

In [10]:
synonyms = {}
synonyms['mutable'] = ['changeable', 'variable', 'varying', 'fluctuating',
                       'shifting', 'inconsistent', 'unpredictable', 'inconstant',
                       'fickle', 'uneven', 'unstable', 'protean']
synonyms['immutable'] = ['fixed', 'set', 'rigid', 'inflexible',
                         'permanent', 'established', 'carved in stone']
synonyms
Out[10]:
{'immutable': ['fixed',
  'set',
  'rigid',
  'inflexible',
  'permanent',
  'established',
  'carved in stone'],
 'mutable': ['changeable',
  'variable',
  'varying',
  'fluctuating',
  'shifting',
  'inconsistent',
  'unpredictable',
  'inconstant',
  'fickle',
  'uneven',
  'unstable',
  'protean']}
另一个例子：

In [11]:
# 定义四个字典
e1 = {'mag': 0.05, 'width': 20}
e2 = {'mag': 0.04, 'width': 25}
e3 = {'mag': 0.05, 'width': 80}
e4 = {'mag': 0.03, 'width': 30}
# 以字典作为值传入新的字典
events = {500: e1, 760: e2, 3001: e3, 4180: e4}
events
Out[11]:
{500: {'mag': 0.05, 'width': 20},
 760: {'mag': 0.04, 'width': 25},
 3001: {'mag': 0.05, 'width': 80},
 4180: {'mag': 0.03, 'width': 30}}
键（或者值）的数据类型可以不同：

In [13]:
people = [
    {'first': 'Sam', 'last': 'Malone', 'name': 35},
    {'first': 'Woody', 'last': 'Boyd', 'name': 21},
    {'first': 'Norm', 'last': 'Peterson', 'name': 34},
    {'first': 'Diane', 'last': 'Chambers', 'name': 33}
]
people
Out[13]:
[{'first': 'Sam', 'last': 'Malone', 'name': 35},
 {'first': 'Woody', 'last': 'Boyd', 'name': 21},
 {'first': 'Norm', 'last': 'Peterson', 'name': 34},
 {'first': 'Diane', 'last': 'Chambers', 'name': 33}]
使用 dict 初始化字典
除了通常的定义方式，还可以通过 dict() 转化来生成字典：

In [14]:
inventory = dict(
    [('foozelator', 123),
     ('frombicator', 18),
     ('spatzleblock', 34),
     ('snitzelhogen', 23)
    ])
inventory
Out[14]:
{'foozelator': 123, 'frombicator': 18, 'snitzelhogen': 23, 'spatzleblock': 34}
利用索引直接更新键值对：

In [15]:
inventory['frombicator'] += 1
inventory
Out[15]:
{'foozelator': 123, 'frombicator': 19, 'snitzelhogen': 23, 'spatzleblock': 34}
适合做键的类型
在不可变类型中，整数和字符串是字典中最常用的类型；而浮点数通常不推荐用来做键，原因如下：

In [16]:
data = {}
data[1.1 + 2.2] = 6.6
# 会报错
data[3.3]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-16-a48e87d01daa> in <module>()
      2 data[1.1 + 2.2] = 6.6
      3 # 会报错
----> 4 data[3.3]

KeyError: 3.3
事实上，观察data的值就会发现，这个错误是由浮点数的精度问题所引起的：

In [17]:
data
Out[17]:
{3.3000000000000003: 6.6}
有时候，也可以使用元组作为键值，例如，可以用元组做键来表示从第一个城市飞往第二个城市航班数的多少：

In [19]:
connections = {}
connections[('New York', 'Seattle')] = 100
connections[('Austin', 'New York')] = 200
connections[('New York', 'Austin')] = 400
元组是有序的，因此 ('New York', 'Austin') 和 ('Austin', 'New York') 是两个不同的键：

In [20]:
print connections[('Austin', 'New York')]
print connections[('New York', 'Austin')]
200
400
字典方法
get 方法
之前已经见过，用索引可以找到一个键对应的值，但是当字典中没有这个键的时候，Python会报错，这时候可以使用字典的 get 方法来处理这种情况，其用法如下：

`d.get(key, default = None)`

返回字典中键 key 对应的值，如果没有这个键，返回 default 指定的值（默认是 None ）。

In [21]:
a = {}
a["one"] = "this is number 1"
a["two"] = "this is number 2"
索引不存在的键值会报错：

In [22]:
a["three"]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-22-8a5f2913f00e> in <module>()
----> 1 a["three"]

KeyError: 'three'
改用get方法：

In [24]:
print a.get("three")
None
指定默认值参数：

In [25]:
a.get("three", "undefined")
Out[25]:
'undefined'
pop 方法删除元素
pop 方法可以用来弹出字典中某个键对应的值，同时也可以指定默认参数：

`d.pop(key, default = None)`

删除并返回字典中键 key 对应的值，如果没有这个键，返回 default 指定的值（默认是 None ）。

In [26]:
a
Out[26]:
{'one': 'this is number 1', 'two': 'this is number 2'}
弹出并返回值：

In [27]:
a.pop("two")
Out[27]:
'this is number 2'
In [28]:
a
Out[28]:
{'one': 'this is number 1'}
弹出不存在的键值：

In [29]:
a.pop("two", 'not exist')
Out[29]:
'not exist'
与列表一样，del 函数可以用来删除字典中特定的键值对，例如：

In [30]:
del a["one"]
a
Out[30]:
{}
update方法更新字典
之前已经知道，可以通过索引来插入、修改单个键值对，但是如果想对多个键值对进行操作，这种方法就显得比较麻烦，好在有 update 方法：

`d.update(newd)`

将字典newd中的内容更新到d中去。

In [31]:
person = {}
person['first'] = "Jmes"
person['last'] = "Maxwell"
person['born'] = 1831
print person
{'born': 1831, 'last': 'Maxwell', 'first': 'Jmes'}
把'first'改成'James'，同时插入'middle'的值'Clerk'：

In [32]:
person_modifications = {'first': 'James', 'middle': 'Clerk'}
person.update(person_modifications)
print person
{'middle': 'Clerk', 'born': 1831, 'last': 'Maxwell', 'first': 'James'}
in查询字典中是否有该键
In [33]:
barn = {'cows': 1, 'dogs': 5, 'cats': 3}
in 可以用来判断字典中是否有某个特定的键：

In [35]:
'chickens' in barn
Out[35]:
False
In [34]:
'cows' in barn
Out[34]:
True
keys 方法，values 方法和items 方法
`d.keys()`

返回一个由所有键组成的列表；

`d.values()`

返回一个由所有值组成的列表；

`d.items()`

返回一个由所有键值对元组组成的列表；

In [36]:
barn.keys()
Out[36]:
['cows', 'cats', 'dogs']
In [37]:
barn.values()
Out[37]:
[1, 3, 5]
In [38]:
barn.items()
Out[38]:
[('cows', 1), ('cats', 3), ('dogs', 5)]
"""