"""
先看一个例子：

In [1]:
x = [1, 2, 3]
y = x
x[1] = 100
print y
[1, 100, 3]
改变变量x的值，变量y的值也随着改变，这与Python内部的赋值机制有关。

简单类型
先来看这一段代码在Python中的执行过程。

x = 500
y = x
y = 'foo'
x = 500
Python分配了一个 PyInt 大小的内存 pos1 用来储存对象 500 ，然后，Python在命名空间中让变量 x 指向了这一块内存，注意，整数是不可变类型，所以这块内存的内容是不可变的。

内存	命名空间
pos1 : PyInt(500) (不可变)	x : pos1
y = x
Python并没有使用新的内存来储存变量 y 的值，而是在命名空间中，让变量 y 与变量 x 指向了同一块内存空间。

内存	命名空间
pos1 : PyInt(500) (不可变)	x : pos1
y : pos1
y = 'foo'
Python此时分配一个 PyStr 大小的内存 pos2 来储存对象 foo ，然后改变变量 y 所指的对象。

内存	命名空间
pos1 : PyInt(500) (不可变)
pos2 : PyStr('foo') (不可变)	x : pos1
y : pos2
对这一过程进行验证，可以使用 id 函数。

id(x)

返回变量 x 的内存地址。

In [2]:
x = 500
id(x)
Out[2]:
48220272L
In [3]:
y = x
id(y)
Out[3]:
48220272L
也可以使用 is 来判断是不是指向同一个事物：

In [4]:
x is y
Out[4]:
True
现在 y 指向另一块内存：

In [5]:
y = 'foo'
id(y)
Out[5]:
39148320L
In [6]:
x is y
Out[6]:
False
Python会为每个出现的对象进行赋值，哪怕它们的值是一样的，例如：

In [7]:
x = 500
id(x)
Out[7]:
48220296L
In [8]:
y = 500
id(y)
Out[8]:
48220224L
In [9]:
x is y
Out[9]:
False
不过，为了提高内存利用效率，对于一些简单的对象，如一些数值较小的int对象，Python采用了重用对象内存的办法：

In [10]:
x = 2
id(x)
Out[10]:
6579504L
In [11]:
y = 2
id(y)
Out[11]:
6579504L
In [12]:
x is y
Out[12]:
True
容器类型
现在来看另一段代码：

x = [500, 501, 502]
y = x
y[1] = 600
y = [700, 800]
x = [500, 501, 502]
Python为3个PyInt分配内存 pos1 ， pos2 ， pos3 （不可变），然后为列表分配一段内存 pos4 ，它包含3个位置，分别指向这3个内存，最后再让变量 x 指向这个列表。

内存	命名空间
pos1 : PyInt(500) (不可变)
pos2 : PyInt(501) (不可变)
pos3 : PyInt(502) (不可变)
pos4 : PyList(pos1, pos2, pos3) (可变)	x : pos4
y = x
并没有创建新的对象，只需要将 y 指向 pos4 即可。

内存	命名空间
pos1 : PyInt(500) (不可变)
pos2 : PyInt(501) (不可变)
pos3 : PyInt(502) (不可变)
pos4 : PyList(pos1, pos2, pos3) (可变)	x : pos4
y : pos4
y[1] = 600
原来 y[1] 这个位置指向的是 pos2 ，由于不能修改 pos2 的值，所以首先为 600 分配新内存 pos5 。

再把 y[1] 指向的位置修改为 pos5 。此时，由于 pos2 位置的对象已经没有用了，Python会自动调用垃圾处理机制将它回收。

内存	命名空间
pos1 : PyInt(500) (不可变)
pos2 : 垃圾回收
pos3 : PyInt(502) (不可变)
pos4 : PyList(pos1, pos5, pos3) (可变)
pos5 : PyInt(600) (不可变)	x : pos4
y : pos4
y = [700, 800]
首先创建这个列表，然后将变量 y 指向它。

内存	命名空间
pos1 : PyInt(500) (不可变)
pos3 : PyInt(502) (不可变)
pos4 : PyList(pos1, pos5, pos3) (可变)
pos5 : PyInt(600) (不可变)
pos6 : PyInt(700) (不可变)
pos7 : PyInt(800) (不可变)
pos8 : PyList(pos6, pos7) (可变)	x : pos4
y : pos8
对这一过程进行验证：

In [13]:
x = [500, 501, 502]
print id(x[0])
print id(x[1])
print id(x[2])
print id(x)
48220224
48220248
48220200
54993032
赋值，id(y) 与 id(x) 相同。

In [14]:
y = x
print id(y)
54993032
In [15]:
x is y
Out[15]:
True
修改 y[1] ，id(y) 并不改变。

In [16]:
y[1] = 600
print id(y)
54993032
id(x[1]) 和 id(y[1]) 的值改变了。

In [17]:
print id(x[1])
print id(y[1])
48220272
48220272
更改 y 的值，id(y) 的值改变

In [18]:
y = [700, 800]
print id(y)
print id(x)
54995272
54993032
"""