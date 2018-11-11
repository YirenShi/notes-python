"""
uUTC(S世界协调时间）：格林尼治天文时间，世界标准世界，在中来说是UTC+8
DST(夏令时）：是一种节约能源而人为规定时间制度，在夏季调快一个小时

时间的表示形式：
1.时间戳：以整型或浮点型表示时间的一个以秒为单位的时间间隔，这个时间间隔的基础值是从1970年1月1日零点开始算起
2.元组：一种python的数据结构表示，这个元组有9个整型内容
year  \month \ day \hours \minutes \seconds  \weekday \ julia day  \ flag(1 或者 -1 或 0）
strftime(format[, tuple]) -> string
将指定的struct_time(默认为当前时间)，根据指定的格式化字符串输出
python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）

%f 毫秒（000000-999999）


%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身

字符串格式化：

<span style="font-family:FangSong_GB2312;font-size:18px;">

格式符

%[(name)][floags][width].[precision]typecode

(name) 可选，用于选择指定的key

flags  可选，可提供的值有：

  +    右对齐，整数前加正号，负数前加负号

  -    左对齐，正数钱无符号，负数前加负号；

 空格 右对齐；正数前加空格，负数前加负号

 0    右对齐，正数前无符号，负数前加负号；用0填充

width   可选，占有宽度

typecode  必选

%s 字符串（str()的显示）

%r 字符串采用repr()显示

%c 单个字符

%b 二进制整数 bin

%i 十进制整数 int

%o  八进制整数 oct

%x 十六进制整数 hex

%f  浮点数

%e 指数

%% 字符% （前提是里面要有格式符的话需要这么写）

案例：

a = "i am %s" % "alex"

a = "i am %s age %d " % ("alex",18)

a = "i am %(name)s age %(age)d" % {"name":"alex","age":18}

a = "percent %.2f" % 99.98234

a = "i am %(pp).2f" % {"pp":123.3245}

a = "i am %.2f %%" % {"pp":123.3223455}

format 格式化

type         【可选】格式化类型 •传入” 字符串类型 “的参数 •s，格式化字符串类型数据

•空白，未指定类型，则默认是None，同s

•传入“ 整数类型 ”的参数

 •b，将10进制整数自动转换成2进制表示然后格式化

•c，将10进制整数自动转换为其对应的unicode字符

 •d，十进制整数

  •o，将10进制整数自动转换成8进制表示然后格式化；

 •x，将10进制整数自动转换成16进制表示然后格式化（小写x）

 •X，将10进制整数自动转换成16进制表示然后格式化（大写X）

•传入“ 浮点型或小数类型 ”的参数 •e， 转换为科学计数法（小写e）表示，然后格式化；

•E， 转换为科学计数法（大写E）表示，然后格式化;

 •f ， 转换为浮点型（默认小数点后保留6位）表示，然后格式化；

 •F， 转换为浮点型（默认小数点后保留6位）表示，然后格式化；

 •g， 自动在e和f中切换

•G， 自动在E和F中切换

 •%，显示百分比（默认显示小数点后6位）

还是看案例吧

a = "i am {},age {}".format("seven",18,"alex")

b = "i am {},age {}, {}".format(*["seven", 18 ,"alex"])

c = "i am {0}, age {1}, really {0}".format("seven", 18)

d = "i am {0}, age{1}, really {0}".format(*["seven", 18])

e = "i am {name}, age {age}, really {name}".format(name="seven", age = 18)

f = "i am {name}, age {age}, rally {name}".format(**{"name":"seven", "age":18})

g = "i am {0[0]},age{0[1]}, really{0[2]}".format([1,2,3],[11,22,33])

h = "i am {:s}, age {:d}, money {:f}".format("seven", 18, 888.1)

i = "i am {:s}, age {:d}".format(*["seven", 18])

j = "i am {name:s}, age {age:d}".format(name="seven",age=18)

k = "i am {name:s}, age {age:d}".format(**{"name":"seven","age":18})

l = "numers:{:b},{:o},{d},{:x},{:X},{:%}".format(15,15,15,15,15,15.32445,2)

m = "numbers:{0:b},{0:o},{0:d},{0:x},{0:%}".format(15)

tpl = "numbers: {num:b},{num:o},{num:d},{num:x},{num:X}, {num:%}".format(num=15)
3.格式化字符串
"""

import time
#返回当前时间的时间戳，浮点数形式，不需要参数--格林尼治时间*****
c = time.time()
print(c)
#将时间戳作为UTC时间元组
t =  time.gmtime(c)#time.struct_time(tm_year=2018, tm_mon=10, tm_mday=6, tm_hour=13, tm_min=45, tm_sec=9, tm_wday=5, tm_yday=279, tm_isdst=0)
print(t)

#将时间戳转为本地时间元组*****
beijingtime = time.localtime(c)
print(beijingtime)

#将本地时间元组转换为时间戳

m = time.mktime(beijingtime)
print(m)

#将时间元组转换成字符串
s = time.asctime(beijingtime)#1538833416.0
print(s)


#将时间戳转换为字符串Sat Oct  6 21:42:22 2018
#p =time.asctime(time.localtime(time.time()))
p = time.ctime()
print(p)

#将时间元组转换成给定格式的字符串,如果没有参数2，默认转当前时间***
q = time.strftime("%Y-%m-%d %X ")
print(p)

#将时间字符串转为时间元组
w = time.strptime(q,"%Y-%m-%d %X ")
print(w)


#延迟一个时间，整型或者浮点型
#time.sleep(4)

#返回当前程序的cup执行时间
#unix系统始终返回全部的运行时间
#windows从第二次开始，都是以第一次调用此函数的开始时间戳作为基数
y1 = time.clock()
print(y1)
time.sleep(1)
y2 = time.clock()
print(y2)

time.sleep(2)
y3 = time.clock()
print(y3)











