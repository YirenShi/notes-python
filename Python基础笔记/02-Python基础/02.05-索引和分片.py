"""
索引
对于一个有序序列，可以通过索引的方法来访问对应位置的值。字符串便是一个有序序列的例子，Python使用 [] 来对有序序列进行索引。

In [1]:
s = "hello world"
s[0]
Out[1]:
'h'
Python中索引是从 0 开始的，所以索引 0 对应与序列的第 1 个元素。为了得到第 5 个元素，需要使用索引值 4 。

In [2]:
s[4]
Out[2]:
'o'
除了正向索引，Python还引入了负索引值的用法，即从后向前开始计数，例如，索引 -2 表示倒数第 2 个元素：

In [3]:
s[-2]
Out[3]:
'l'
单个索引大于等于字符串的长度时，会报错：

In [4]:
s[11]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-4-79ffc22473a3> in <module>()
----> 1 s[11]

IndexError: string index out of range
分片
分片用来从序列中提取出想要的子序列，其用法为：

var[lower:upper:step]

其范围包括 lower ，但不包括 upper ，即 [lower, upper)， step 表示取值间隔大小，如果没有默认为1。

In [5]:
s
Out[5]:
'hello world'
In [6]:
s[1:3]
Out[6]:
'el'
分片中包含的元素的个数为 3-1=2 。

也可以使用负索引来指定分片的范围：

In [7]:
s[1:-2]
Out[7]:
'ello wor'
包括索引 1 但是不包括索引 -2 。

lower和upper可以省略，省略lower意味着从开头开始分片，省略upper意味着一直分片到结尾。

In [8]:
s[:3]
Out[8]:
'hel'
In [9]:
s[-3:]
Out[9]:
'rld'
In [10]:
s[:]
Out[10]:
'hello world'
每隔两个取一个值：

In [11]:
s[::2]
Out[11]:
'hlowrd'
当step的值为负时，省略lower意味着从结尾开始分片，省略upper意味着一直分片到开头。

In [12]:
s[::-1]
Out[12]:
'dlrow olleh'
当给定的upper超出字符串的长度（注意：因为不包含upper，所以可以等于）时，Python并不会报错，不过只会计算到结尾。

In [13]:
s[:100]
Out[13]:
'hello world'
使用“0”作为索引开头的原因
使用[low, up)形式的原因
假设需要表示字符串 hello 中的内部子串 el ：

方式	[low, up)	(low, up]	(lower, upper)	[lower, upper]
表示	[1,3)	(0,2]	(0,3)	[1,2]
序列长度	up - low	up - low	up - low - 1	up - low + 1
对长度来说，前两种方式比较好，因为不需要烦人的加一减一。

现在只考虑前两种方法，假设要表示字符串hello中的从头开始的子串hel：

方式	[low, up)	(low, up]
表示	[0,3)	(-1,2]
序列长度	up - low	up - low
第二种表示方法从-1开始，不是很好，所以选择使用第一种[low, up)的形式。

使用0-base的形式
Just too beautiful to ignore.
----Guido van Rossum
两种简单的情况：

从头开始的n个元素；

使用0-base：[0, n)
使用1-base：[1, n+1)
第i+1个元素到第i+n个元素。

使用0-base：[i, n+i)
使用1-base：[i+1, n+i+1)
1-base有个+1部分，所以不推荐。

综合这两种原因，Python使用0-base的方法来进行索引。
"""