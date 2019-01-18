"""
整型 Integers
整型运算，加减乘：

In [1]:
2 + 2
Out[1]:
4
In [2]:
3 - 4
Out[2]:
-1
In [3]:
4 * 5
Out[3]:
20
在Python 2.7中，整型的运算结果只能返回整型，除法的结果也不例外。

例如12 / 5返回的结果并不是2.4，而是2：

In [4]:
12 / 5
Out[4]:
2
幂指数：

In [5]:
2 ** 5
Out[5]:
32
取余：

In [6]:
32 % 5
Out[6]:
2
赋值给变量：

In [7]:
a = 1
a
Out[7]:
1
使用type()函数来查看变量类型：

In [8]:
type(a)
Out[8]:
int
整型数字的最大最小值：

在 32 位系统中，一个整型 4 个字节，最小值 -2,147,483,648，最大值 2,147,483,647。

在 64 位系统中，一个整型 8 个字节，最小值 -9,223,372,036,854,775,808，最大值 9,223,372,036,854,775,807。

In [9]:
import sys
sys.maxint
Out[9]:
2147483647
长整型 Long Integers
当整型超出范围时，Python会自动将整型转化为长整型，不过长整型计算速度会比整型慢。

In [10]:
a = sys.maxint + 1
print type(a)
<type 'long'>
长整型的一个标志是后面以字母L结尾：

In [11]:
a
Out[11]:
2147483648L
可以在赋值时强制让类型为长整型：

In [12]:
b = 1234L
type(b)
Out[12]:
long
长整型可以与整型在一起进行计算，返回的类型还是长整型：

In [13]:
a - 4
Out[13]:
2147483644L
浮点数 Floating Point Numbers
In [14]:
a = 1.4
type(a)
Out[14]:
float
在之前的除法例子12 / 5中，假如想要使返回的结果为2.4，可以将它们写成浮点数的形式：

In [15]:
12.0 / 5.0
Out[15]:
2.4
In [16]:
12 / 5.0
Out[16]:
2.4
In [17]:
12.0 / 5
Out[17]:
2.4
上面的例子说明，浮点数与整数进行运算时，返回的仍然是浮点数：

In [18]:
5 + 2.4
Out[18]:
7.4
浮点数也可以进行与整数相似的运算，甚至可以取余：

In [19]:
3.4 - 3.2
Out[19]:
0.19999999999999973
In [20]:
12.3 + 32.4
Out[20]:
44.7
In [21]:
2.5 ** 2
Out[21]:
6.25
In [22]:
3.4 % 2.1
Out[22]:
1.2999999999999998
Python的浮点数标准与C，Java一致，都是IEEE 754 floating point standard。

注意看 3.4 - 3.2 的结果并不是我们预期的0.2，这是因为浮点数本身储存方式引起的，浮点数本身会存在一点误差。

事实上，Python 中储存的值为'0.199999999999999733546474089962430298328399658203125'，因为这是最接近0.2的浮点数。|

In [23]:
'{:.52}'.format(3.4 - 3.2)
Out[23]:
'0.199999999999999733546474089962430298328399658203125'
当我们使用print显示时，Python会自动校正这个结果

In [24]:
print 3.4 - 3.2
0.2
可以用sys.float_info来查看浮点数的信息：

In [25]:
import sys
sys.float_info
Out[25]:
sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
例如浮点数能表示的最大值：

In [26]:
sys.float_info.max
Out[26]:
1.7976931348623157e+308
浮点数能表示的最接近0的值：

In [27]:
sys.float_info.min
Out[27]:
2.2250738585072014e-308
浮点数的精度：

In [28]:
sys.float_info.epsilon
Out[28]:
2.220446049250313e-16
复数 Complex Numbers
Python 使用 j 来表示复数的虚部：

In [29]:
a = 1 + 2j
type(a)
Out[29]:
complex
可以查看它的实部，虚部以及共轭：

In [30]:
a.real
Out[30]:
1.0
In [31]:
a.imag
Out[31]:
2.0
In [32]:
a.conjugate()
Out[32]:
(1-2j)
交互计算
可以将复杂的表达式放在一起计算：

In [33]:
1 + 2 - (3 * 4 / 6) ** 5 + 7 % 5
Out[33]:
-27
在Python中运算是有优先级的，优先级即算术的先后顺序，比如“先乘除后加减”和“先算括号里面的”都是两种优先级的规则，优先级从高到低排列如下：

( ) 括号
** 幂指数运算
* / // % 乘，除，整数除法，取余运算
'+ -' 加减
整数除法，返回的是比结果小的最大整数值：

In [34]:
12.3 // 5.2
Out[34]:
2.0
In [35]:
12.3 // -4
Out[35]:
-4.0
简单的数学函数
绝对值：

In [36]:
abs(-12.4)
Out[36]:
12.4
取整：

In [37]:
round(21.6)
Out[37]:
22.0
最大最小值：

In [38]:
print min(2, 3, 4, 5)
print max(2, 4, 3)
2
4
变量名覆盖
不要用内置的函数来命名变量，否则会出现意想不到的结果：

In [39]:
type(max)
Out[39]:
builtin_function_or_method
不要这样做！！！

In [40]:
max = 1
type(max)
Out[40]:
int
In [41]:
max(4, 5)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-41-c60446be959c> in <module>()
----> 1 max(4, 5)

TypeError: 'int' object is not callable
类型转换
浮点数转整型，只保留整数部分：

In [42]:
print int(12.324)
print int(-3.32)
12
-3
整型转浮点型：

In [43]:
print float(1.2)
1.2
其他表示
除了10进制外，整数还有其他类型的表示方法。

科学计数法：

In [44]:
1e-6
Out[44]:
1e-06
16进制，前面加0x修饰，后面使用数字0-9A-F：

In [45]:
0xFF
Out[45]:
255
8进制，前面加0或者0o修饰，后面使用数字0-7：

In [46]:
067
Out[46]:
55
2进制，前面加0b修饰，后面使用数字0或1：

In [47]:
0b101010
Out[47]:
42
原地计算 In-place
Python可以使用下面的形式进行原地计算：

In [48]:
b = 2.5
b += 2
print b
b *= 2
print b
b -= 3
print b
4.5
9.0
6.0
布尔型 Boolean Data Type
布尔型可以看成特殊的二值变量，其取值为True和False：

In [49]:
q = True
type(q)
Out[49]:
bool
可以用表达式构建布尔型变量：

In [50]:
q = 1 > 2
print q
False
常用的比较符号包括：

<, >, <=, >=, ==, !=

Python支持链式比较：

In [51]:
x = 2
1 < x <= 3
Out[51]:
True
"""
# #导入库
#库：封装一些功能
#math：数学相关的库
#random 随机数的方法
import math
import random
"""
分类：整数，浮点数，复数
"""
"""
z整数：python 可以处理任意大小的整数，当然包括负整数。在程序中的表示和数学的写法一样
"""
num1 = 10
num2 = num1
#连续定义多个变量
num3 = num4 = num5 = 1
print(num3, num4, num5)
#交互式赋值定义变量
num6, num7 = 6, 7
print(num6, num7 )
"""
浮点数：浮点数由整数点与小数点部分组成，浮点数运算可能会有四舍五入的误差
"""
f1= 1.1
f2= 2.2
print(f1 + f2)
"""
复数：实数部分和虚数部分构成  可以用a+bj
"""
"""
s数字类型转换
int 取字符串整数
float 整数转浮点数
"""
print(int(2.1))
print(float(1))
#print(int(abc)) 无用
#print(int(123abc)) 无用
#只有作为正负号才有意思
print(int(+123))
print(int(-123))

#数字功能
#abs 返回数字的绝对值
a1 = -10
a2 = abs(a1)
print(a2)
#比较两个数的大小   -1 为a3小，  1为a4小，  0为相等
a3 = 6
a4 = 9
print((6>9)-(6<9))
print((10>9)-(10<9))
print((9>9)-(9<9))
print((a3>a4)-(a3<a4))

#返回给定参数的最大值
print(max(1,2,3,4,5,6))
#返回给定参数的最小值
print(min(1,2,3,4,5,6))

#求x的y次方  2**5
print(pow(2,5))

#round 四舍五入--浮点数,  1小数点后1位 返回浮点数X的四舍五入的值，如果给出的n值，则代表舍入到小数点后n位
print(round(3.456))
print(round(3.556))
print(round(3.456,2))
print(round(3.546,1))

#向上取整
print(math.ceil(18.1))
print(math.ceil(18.9))

#向下取整
print(math.floor(18.1))

#返回整数部分与小数部分0.3，22.0
print(math.modf(22.3))

#sqrt  开方
print(math.sqrt(16))

#随机数

#1 从序列的元素中挑选一个元素
print(random.choice([1,3,5,7,9,"aa"]))
print(random.choice(range(5)))#range(5)##[0,1,2,3,4]
print(random.choice("sunck"))#"sunck"==["s","u","n",***]

#产生一个1~100之间的随机数
r1 = (random.choice(range(10))+1)
print(r1)


#从指定范围内，按指定的基数递增的集合中选取的一个随机数---，2
#random.randrange([start,] stop[, step])----[  ]指可写可不写
#start-指指定范围的开始值，包含在范围内
#stop--指定范围的结束值，不包含在范围内
#step--指递增基数，默认是1
print(random.randrange(1, 100,2))
#从0~99选取一个随机数
print(random.randrange(100))
#随机生成[0,1)之间的数（浮点数）--- ） 不包含 1--不能输入值
print(random.random())

list = [1,2,3,4,5]
#将序列的所有元素随机排序---random.shuffle
random.shuffle(list)
print(list)

#随机生成一个实数，它在3~9的范围
print(random.uniform(3,9))

#三角函数
