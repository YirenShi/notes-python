# -*- coding: utf-8 -*-
#强制使用utf-8 编码
"""
if 语句
if- else 语句
                    else-if缩写：每个elif都是对它上面所有表达式的否定
逻辑：当程序执行到if-elif-else 语句时，首先计算表达式1的值，
如果表达式1的值为真，则执行语句1，执行完语句1，则跳过整个if-elif-else 语句
如果表达式1的值为假，计算表达式2的值
如果表达式2的值为真，则执行语句2，执行完语句3，则跳过整个if-elif-else 语句
如果表达式2的值为假，计算表达式3的值
......
如此下去直到某个表达式的值为真才停止，如果没有一个表达式为真，且有else语句，则执行语句e
if-elif-else 语句
格式：
if 表达式1：
    语句1
elif  表达式2：
     语句2
elif  表达式2：
     语句2
     *****
elif  表达式n：
      语句n
else：     #可有可无
      语句e

"""
"""
age = int(input("请输入您的年龄"))

if age < 0:
    print("娘胎里")
if age >= 0 and age <=3:
    print("婴儿")
if 4 <=age and age <= 6:
    print("儿童")
if 7 <= age and age <= 18:
    print("童年")
if 19 <=age and age <= 30:
    print("青年")
if 31 <=age and age <= 40:
    print("壮年")
if 41 <=age and age <= 50:
    print("中年")
if 51 <=age and age <= 100:
    print("老年")
if 101 <=age and age <= 150:
    print("老寿星")
if 151 <= age:
    print("老妖精")
"""
age = int(input("请输入您的年龄"))

if age < 0:
    print("娘胎里")
elif  age <=3:
    print("婴儿")
elif  age <= 6:
    print("儿童")
elif  age <= 18:
    print("童年")
elif  age <= 30:
    print("青年")
elif  age <= 40:
    print("壮年")
elif  age <= 50:
    print("中年")
elif  age <= 100:
    print("老年")
elif  age <= 150:
    print("老寿星")
elif 151 <= age:
    print("老妖精")