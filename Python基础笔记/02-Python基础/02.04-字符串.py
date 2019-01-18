"""
s = "hello, world"
print s
hello, world
In [2]:
s = 'hello world'
print s
hello world
简单操作
加法：

In [3]:
s = 'hello ' + 'world'
s
Out[3]:
'hello world'
字符串与数字相乘：

In [4]:
"echo" * 3
Out[4]:
'echoechoecho'
字符串长度：

In [5]:
len(s)
Out[5]:
11
字符串方法
Python是一种面向对象的语言，面向对象的语言中一个必不可少的元素就是方法，而字符串是对象的一种，所以有很多可用的方法。

跟很多语言一样，Python使用以下形式来调用方法：

对象.方法(参数)
分割
s.split()将s按照空格（包括多个空格，制表符\t，换行符\n等）分割，并返回所有分割得到的字符串。

In [6]:
line = "1 2 3 4  5"
numbers = line.split()
print numbers
['1', '2', '3', '4', '5']
s.split(sep)以给定的sep为分隔符对s进行分割。

In [7]:
line = "1,2,3,4,5"
numbers = line.split(',')
print numbers
['1', '2', '3', '4', '5']
连接
与分割相反，s.join(str_sequence)的作用是以s为连接符将字符串序列str_sequence中的元素连接起来，并返回连接后得到的新字符串：

In [8]:
s = ' '
s.join(numbers)
Out[8]:
'1 2 3 4 5'
In [9]:
s = ','
s.join(numbers)
Out[9]:
'1,2,3,4,5'
替换
s.replace(part1, part2)将字符串s中指定的部分part1替换成想要的部分part2，并返回新的字符串。

In [10]:
s = "hello world"
s.replace('world', 'python')
Out[10]:
'hello python'
此时，s的值并没有变化，替换方法只是生成了一个新的字符串。

In [11]:
s
Out[11]:
'hello world'
大小写转换
s.upper()方法返回一个将s中的字母全部大写的新字符串。

s.lower()方法返回一个将s中的字母全部小写的新字符串。

In [12]:
"hello world".upper()
Out[12]:
'HELLO WORLD'
这两种方法也不会改变原来s的值：

In [13]:
s = "HELLO WORLD"
print s.lower()
print s
hello world
HELLO WORLD
去除多余空格
s.strip()返回一个将s两端的多余空格除去的新字符串。

s.lstrip()返回一个将s开头的多余空格除去的新字符串。

s.rstrip()返回一个将s结尾的多余空格除去的新字符串。

In [14]:
s = "  hello world   "
s.strip()
Out[14]:
'hello world'
s的值依然不会变化：

In [15]:
s
Out[15]:
'  hello world   '
In [16]:
s.lstrip()
Out[16]:
'hello world   '
In [17]:
s.rstrip()
Out[17]:
'  hello world'
更多方法
可以使用dir函数查看所有可以使用的方法：

In [18]:
dir(s)
Out[18]:
['__add__',
 '__class__',
 '__contains__',
 '__delattr__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__getnewargs__',
 '__getslice__',
 '__gt__',
 '__hash__',
 '__init__',
 '__le__',
 '__len__',
 '__lt__',
 '__mod__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rmod__',
 '__rmul__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '_formatter_field_name_split',
 '_formatter_parser',
 'capitalize',
 'center',
 'count',
 'decode',
 'encode',
 'endswith',
 'expandtabs',
 'find',
 'format',
 'index',
 'isalnum',
 'isalpha',
 'isdigit',
 'islower',
 'isspace',
 'istitle',
 'isupper',
 'join',
 'ljust',
 'lower',
 'lstrip',
 'partition',
 'replace',
 'rfind',
 'rindex',
 'rjust',
 'rpartition',
 'rsplit',
 'rstrip',
 'split',
 'splitlines',
 'startswith',
 'strip',
 'swapcase',
 'title',
 'translate',
 'upper',
 'zfill']
多行字符串
Python 用一对 """ 或者 ''' 来生成多行字符串：

In [19]:
a = """hello world.
it is a nice day."""
print a
hello world.
it is a nice day.
在储存时，我们在两行字符间加上一个换行符 '\n'

In [20]:
a
Out[20]:
'hello world.\nit is a nice day.'
使用 () 或者 \ 来换行
当代码太长或者为了美观起见时，我们可以使用两种方法来将一行代码转为多行代码：

()
\
In [21]:
a = ("hello, world. "
    "it's a nice day. "
    "my name is xxx")
a
Out[21]:
"hello, world. it's a nice day. my name is xxx"
In [22]:
a = "hello, world. " \
    "it's a nice day. " \
    "my name is xxx"
a
Out[22]:
"hello, world. it's a nice day. my name is xxx"
强制转换为字符串
str(ob)强制将ob转化成字符串。
repr(ob)也是强制将ob转化成字符串。
不同点如下：

In [23]:
str(1.1 + 2.2)
Out[23]:
'3.3'
In [24]:
repr(1.1 + 2.2)
Out[24]:
'3.3000000000000003'
整数与不同进制的字符串的转化
可以将整数按照不同进制转化为不同类型的字符串。

十六进制：

In [25]:
hex(255)
Out[25]:
'0xff'
八进制：

In [26]:
oct(255)
Out[26]:
'0377'
二进制：

In [27]:
bin(255)
Out[27]:
'0b11111111'
可以使用 int 将字符串转为整数：

In [28]:
int('23')
Out[28]:
23
还可以指定按照多少进制来进行转换，最后返回十进制表达的整数：

In [29]:
int('FF', 16)
Out[29]:
255
In [30]:
int('377', 8)
Out[30]:
255
In [31]:
int('11111111', 2)
Out[31]:
255
float 可以将字符串转换为浮点数：

In [32]:
float('3.5')
Out[32]:
3.5
格式化字符串
Python用字符串的format()方法来格式化字符串。

具体用法如下，字符串中花括号 {} 的部分会被format传入的参数替代，传入的值可以是字符串，也可以是数字或者别的对象。

In [33]:
'{} {} {}'.format('a', 'b', 'c')
Out[33]:
'a b c'
可以用数字指定传入参数的相对位置：

In [34]:
'{2} {1} {0}'.format('a', 'b', 'c')
Out[34]:
'c b a'
还可以指定传入参数的名称：

In [35]:
'{color} {n} {x}'.format(n=10, x=1.5, color='blue')
Out[35]:
'blue 10 1.5'
可以在一起混用：

In [36]:
'{color} {0} {x} {1}'.format(10, 'foo', x = 1.5, color='blue')
Out[36]:
'blue 10 1.5 foo'
可以用{<field name>:<format>}指定格式：

In [37]:
from math import pi

'{0:10} {1:10d} {2:10.2f}'.format('foo', 5, 2 * pi)
Out[37]:
'foo                 5       6.28'
具体规则与C中相同。

也可以使用旧式的 % 方法进行格式化：

In [38]:
s = "some numbers:"
x = 1.34
y = 2
# 用百分号隔开，括号括起来
t = "%s %f, %d" % (s, x, y)
In [39]:
t
Out[39]:
'some numbers: 1.340000, 2'
"""





""""
什么是字符串
字符串是以单引号括起来的任意文本、
"abc"
"def"
z字符串不可变
"""

#创建字符串
str1 = "sunck is a good man!"
str3 = "sunck is a nice man!"
str5 = "sunck is a handsome man!"
"""
#字符串运算

"""
#字符串连接
str6 ="sunck is a"
str7 ="good man"
str8 = str6 + str7

print("str6=", str6)
print("str7=", str7)
print("str8=", str8)
#输出重复字符串
str9 ="good"
str10 = str9 * 3
print("str10=", str10)
# 符文字符串中的某一个字符
#通过索引下标查找字符，索引从0开始
str11 = "sunck is a nice man!"
print(str11[1])
#str11[1]="a"
#字符串不可变---34
#print("str11=",str11)

#截取字符串中的一部分，
str13 = "sunck is a nice man!"
#从给定下标开始截取到给定下标之前
str15 = str13[6:14]
#从头截取到给定下标之前
str16 = str13[0:5]
print("str15= ", str15)
print("str16= ", str16)
#从给定下标处开始截取到结尾
str17 = str13[16:]
print("str17= ", str17)

str18 = "sunck is s good man"
#good in str18  ,true ,not --false    not in不在
print("good" in str18)
print("good1" not in str18)


#格式化输出
print("sunck is a good man")
num = 10
str19 = "sunck is s nice man"
f = 10.1234
print("num = ", num)
# %d   %a   %f   占位符
#                                  3-精确到小数点后3位，会四舍五入
print("num = % d,str19 =  %a,f = %.3f"% (num,str19,f))
#转义字符    \
#将一些字符转换成有特殊含义的字符
#\n
print("num = % d\nstr19 =  %a\nf = %.3f"% (num,str19,f))
print("sunck \\n is a good man ")
'''
\\
'''
print('sunck  is a \'good\' man ')
print("sunck  is a \"good\" man ")
#如果字符串内有很多换行，用\n写在一行不好阅读
print("sunck \n is a \ngood\n man ")

print("""
good
nice
handsome
""")

"""
\t  制表符 默认4个空格
"""
print("sunck\t good")
#如果字符串中有好多字符度需要转义，需加入好多\，
# 为了简化，python允许用r表示内部字符串默认不转义
#        \\\t\\
print("\\\t \\")
print(r"\\\t \\")

#eval(str)
#功能：将字符串str当成有效的表达式来求值并返回计算结果
num20 = eval("123")
print(eval("12+3"))


#len(str)
#返回字符串的长度（字符个数）

print(len("sunck is a good man客家话"))

#lower（str）
#转换字符串中的大写字符为小写字符
str21 = "Sunck Is"
print(str21.lower())
#print("str21 = %s" %（str21))  字符串未改变，相当于重新生成一个字符串str22

#upper（） 转换字符串中的小写字符为大写字符
print("Sunck Is".upper())
str22 = "Sunck Is"

#swapcase() 转换字符串中的小写字符为大写字符,大写字符为小写字符
str23 = "Sunck Is"
print(str23.swapcase())


#capitalize 首字母大写，其他小写
str24 =  "SUNCk IS"
print(str24.capitalize())

#title（） 每个单词的首字母大写
str25 = "SUNCk IS"
print(str24.title())

#center(width, fillchar)#character
#返回一个指定宽度的居中的字符串，fillchar为填充的字符串，默认为空格填充
str26 = "SUNCk IS a good man"
print(str26.center(40,"*"))


#ljust(width[,fillchar])
#返回一个指定宽度的左对齐字符串，fillchar为填充字符，默认为空格填充
str27 = "SUNCk IS a good man27"
print(str27.ljust(40),"*")

#rjust(width[,fillchar])
#返回一个指定宽度的右对齐字符串，fillchar为填充字符，默认为空格填充
print(str27.rjust(40),"*")

#zfill(width)
#返回一个长度为width的字符串，原字符串右对齐，前面补零
str28 = "kaige is a nice man"
print(str28.zfill(40))

#count(str[,start][,end])
#返回字符串中str出现的次数，可以指定一个范围，默认从头到尾
str29 = "kaige is a very very nice man"
print(str29.count("very",15,len(str29)))

#fing(str[start][,end])
#从左至右检查str字符串是否包含在字符串中，可以指定范围，默认从头到尾
#得到的是第一次出现的开始下标，没有返回-1
str30 =  "kaige is a very very nice man"
print(str30.find("very"))
print(str30.find("good"))
print(str30.find("very",15,len(str30)))

#rfing(str[start][,end])
#从右至左检查str字符串是否包含在字符串中，可以指定范围，默认从头到尾
#得到的是第一次出现的开始下标，没有返回-1
print(str30.rfind("very"))
print(str30.rfind("good"))
print(str30.rfind("very",0,len(str30)))

#index(str,start = 0,end = len(str))
#与find()一样，只不过如果str不存在的时候，会报一个异常（find报错为-1）
str31 =  "kaige is a very very nice man"
print(str31.index("very"))

#rindex(str,start = 0,end = len(str))
#与rfind()一样，只不过如果str不存在的时候，会报一个异常（rfind报错为-1）
print(str31.rindex("very"))

#lstrip()截取字符中左侧指定的字符，默认为空格
str33 = "*******kaige is a  nice man"
print(str33.lstrip("*"))

#rstrip()截取字符中右侧指定的字符，默认为空格
str33 ="*******kaige is a  nice man******"
print(str33.rstrip("*"))

#strip()截取字符中左右侧指定的字符，默认为空格
str35 = "*******kaige is a  nice man******"
print(str35.strip("*"))
#ASII码表
str36 = "a"
print(ord(str36))#ord（）   字符串转ASSII 码表
str37 = chr(65)#chr（）  ASII码表转字符串
print(str37)


print("a" == "a")

#split(str="",num)--num
#以str为分隔符截取字符串,指定num，仅截取num个字符串
str38 = "sunck*****is**a******good*man"
list39 = str38.split("*")
c = 0
for s in list39:
    if len(s) > 0 :
        c += 1
print(c)

#splitlines([keepends])  安装（‘\r’， ‘\r\n’， ‘\n）分隔--按行切割
#keepends ==true 会保留换行符

str40 = '''sunck is a good man
sunck is a nice man
sunck is a gsomehand man
'''
print(str40.splitlines())


#jion(seq) 以指定的字符串分隔符，将seq中所有元素组合成一个字符串
list41 = ['sunck is a good man', 'sunck is a nice man', 'sunck is a gsomehand man']
str42 = "$%#$".join(list41)
print(str42)


#max()  min()

str43 = "sunck is a good man! z"
print(max(str43))
print(min(str43))


#replace(oldstr, newstr, count)
#yong newstr替换oldstr,默认是全部替换，如果指定了count，那么只替换前count数
str44 = "sunck is a good  good good man!"

str45 = str44.replace("good", "nice",1)
print(str44)
print(str45)

#创建一个字符串映射表
t46 = str.maketrans("ac","65")
#a---6   c---5
str47 = "sunck is a good man"
str48 = str47.translate(t46)
print(str48)

#startswith(str,start=0,end=len(str))
str49 = "sunck is a good man"
print(str49.startswith("sun",5,16))
#endswith(str,start=0,end=len(str))
#在给定的范围内判断是否是以给定的字符串结尾，如果没有指定范围，默认整个字符串
str50 =  "sunck is a good man"
print(str50.endswith("sun"))
#编码
#encode(encoding = "utf-8",errors = "strict")
str51 = "suncck is a good man凯"
print(str51.encode())
data52 = str51.encode("utf-8")
print(data52)


#解码  注意：要与编码时的编码格式一致
#"ignore"  忽略错误
str53 = data52.decode("utf-8","ignore")
print(str53)

#isalpha()
#如果字符串中至少有一个字符且所有字符都是字母返回true，否则返回false
str54 = "sunckisagoodman"
print(str54.isalpha())

#isalnum（）
#如果字符中至少有一个字符且所有的字符都市字母活数字返回true，否则返回false
str55 = "123a "
print(str55.isalnum())

#isupper
#如果字符串中至少有一个英文字符且所有英文字符都是大写的英文字母，返回true，否则false
print("ABC".isupper())
print("ABC1".isupper())

#islower()
#如果字符串中至少有一个英文字符且所有英文字符都是小写的英文字母，返回true，否则false
print("abc".islower())
print("ABC1".islower())

#istitle()
#如果字符串是标题化(单词首字母大写，其余小写)的返回true，否则返回false
print("sunck is a good man".istitle)

#isdigit()
#如果字符中只包含数字字符返回true，否则返回false
print("123".isdigit())
print("123a".isdigit())

#isnumeric（） 同上
print("123".isnumeric())
print("123a".isnumeric())
#字符串只包含十进制字符
print("123".isdecimal())
print("123a".isdecimal())

#如果字符串中只包含空格则返回true，否则返回false
print("".isspace())
print("   ".isspace())
print("\t".isspace())
print("\n".isspace())
print("\r".isspace())