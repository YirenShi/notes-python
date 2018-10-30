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
