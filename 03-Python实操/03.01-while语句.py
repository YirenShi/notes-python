"""
while 语句
while 表达式：
      语句
逻辑：当程序执行到while语句时，首先计算“表达式”的值，如果表达式的值为假，结束整个while语句
如果表达式的值为真，则执行语句，执行完”语句“，执行完语句再去计算表达式的值。
如果表达式的值为假，那么结束整个while语句，如果表达式的值还为真，则执行语句，执行玩语句再去计算表达式的值
如此循环往复，知道表达式的值为假才停止
"""
print(1)
print(2)
print(3)
print(4)
print(5)

num = 1
while num <=5:
    print(num)
    num +=1

#计算1+2+3+....100
sum = 0
num = 1
while num <= 100:
    sum +=num
    num +=1
print("sum = %d"% (sum))
"""
0+1
1+2
3+3
6+4
.......
"""

str = "SUNCk IS a good man27"
index = 0
while index <len(str): #index < 19
    print("str [%d]= %s"% (index, str[index]))#str[]提取字符串
    index +=1