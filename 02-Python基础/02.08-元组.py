"""
基本操作
与列表相似，元组Tuple也是个有序序列，但是元组是不可变的，用()生成。

In [1]:
t = (10, 11, 12, 13, 14)
t
Out[1]:
(10, 11, 12, 13, 14)
可以索引，切片：

In [2]:
t[0]
Out[2]:
10
In [3]:
t[1:3]
Out[3]:
(11, 12)
但是元组是不可变的：

In [4]:
# 会报错
t[0] = 1
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-da6c1cabf0b0> in <module>()
      1 # 会报错
----> 2 t[0] = 1

TypeError: 'tuple' object does not support item assignment
单个元素的元组生成
由于()在表达式中被应用，只含有单个元素的元组容易和表达式混淆，所以采用下列方式定义只有一个元素的元组：

In [5]:
a = (10,)
print a
print type(a)
(10,)
<type 'tuple'>
In [6]:
a = (10)
print type(a)
<type 'int'>
将列表转换为元组：

In [7]:
a = [10, 11, 12, 13, 14]
tuple(a)
Out[7]:
(10, 11, 12, 13, 14)
元组方法
由于元组是不可变的，所以只能有一些不可变的方法，例如计算元素个数 count 和元素位置 index ，用法与列表一样。

In [8]:
a.count(10)
Out[8]:
1
In [9]:
a.index(12)
Out[9]:
2
为什么需要元组
旧式字符串格式化中参数要用元组；

在字典中当作键值；

数据库的返回值……
"""