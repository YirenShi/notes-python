#定义了一个无参数无返回值的函数
def myprint():
    print("sunck is a good man")
    print("sunck is a nice man")
    print("sunck is a handsome man")

myprint()

#需求：编写一个函数，给函数一个字符串和一个年龄，在函数内部打印出来
#形参（形式参数）：定义函数小括号中的变量，本质是变量
#参数的传递必须按顺序传递，个数目前来看要对应
#def myprint(str , age , hoby):
#   print(str , age)
#实参（实际参数），调用函数时给函数传递的数据，本质是值
def myprint(str , age):
   print(str , age)
a = 18
myprint("sunck is a good man" , a)


"""
值传递：传递的是不可变类型
string。tuple。number是不可变的
"""
def func1(num):
    print(id(num))
    num = 10
    print(id(num))
temp = 20
print(id(temp))
func1(temp)  #num = temp
print(id(temp))
print(temp)
"""
引用传递：传递的是可变类型
list。dict。set是可变的
"""
def fun2(list):
    list[0] = 100
li = [1,2,3,4,5,6,7]
fun2(li)
print(li)

a = 10
b = 10
b = 40
print(id(a),id(b))

c = 20
d = 30
print(id(c),id(d))

d = c
print(id(c),id(d))
print(d)











