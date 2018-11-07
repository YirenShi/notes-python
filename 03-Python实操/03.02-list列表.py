#存储5个人的年龄，求他们的平均年龄
age1 = 18
age2 = 20
age3 = 34
age4 = 21
age5 = 33
print((age1 +age2 + age3 + age4 + age5)/5)

#思考：使用列表
#本质：一种有序的集合

#创建列表
#格式：列表名 = [列表选项1，列表选项2， 列表选项3，......，列表选项n]
"""

"""
#创建了一个空列表
list1 = []
print(list1)
#创建带有元素的列表
list = [18, 19, 20, 21, 22]
index = 0
sum = 0
#嵌套最好不要超过3层
while index <5:
    sum += list[index]
    index += 1
    if index ==5:
        print("平均年临：%d"%(sum/5))
#注意：列表中的元素数据可以是不同类型的
list3 = [1, 2, "sunck", "good", True]
print(list3)

#列表元素的访问
#取值：格式：列表名[下标]
list4 = [18, 19, 20, 21, 22]
print(list4[2])
#替换：
list4 [2] = 300
print(list4)

#列表操作：
#列表组合
list5 = [1, 2, 3]
list6 = [4, 5, 6]
list7 = list5 + list6
print(list7)

#列表的重复
list8 = [1, 2, 3]
print(list8 * 3)

#判断元素是否在列表中
list9 = [1, 2, 3, 4,5]
print(3 in list9)

#列表截取
list10 = [1, 2, 3, 4, 5, 6, 7, 8,9]
print(list10[2:5])
print(list10[3:])
print(list10[:5])

#二维列表
list11 = [[1, 2, 3, 4, 5, 6, 7, 8,9], [2, 5]]
print(list11[1][1])

#列表方法
#append   在列表中，末尾添加新的元素
list12 = [1, 2, 3, 4, 5, 6,]
list12.append(6)
list12.append([7, 8, 9])
print(list12)


#extend:在末尾一次性追加另一个列表中的多个值
list13 = [1, 2, 3, 4, 5, 6,]
#list13.extend(6)---列表，字符不可用
list13.extend([7, 8, 9])
print(list13)

#z在下标出添加一个元素，不覆盖元数据，元数据向后顺延
list14 = [1, 2, 3, 4, 5, 6,]
list14.insert(1, 100)
list14.insert(2, [200,300])
print(list14)

#pop (x = list[-1])
#移除列表中指定下标出的元素（默认移除最后一个元素）,并返回删除的数据
list15 = [1, 2, 3, 4, 5, 6,]
list15.pop()
list15.pop(2)
#list15.pop(2, [200,300])
print(list15.pop(1))
print(list15)

#remove 移除列表中的每个元素,第一个匹配的结果
list16 = [1, 2, 3, 4, 5, 6,4, 5, 4]
list16.remove(4)
print(list16)

#清除列表中的所有数据
list17 = [1, 2, 3, 4, 5, 6,4, 5, 4]
list17.clear()
print(list17)

#从列表中找出某个值第一个匹配的索引值
list18 = [1, 2, 3, 4, 5,3,4, 5, 6]
index18 = list18.index(3)
print(index18)
#圈定范围.
index19 = list18.index(3, 3, 7)
print(index18, index19)

#列表元素个数
list20 = [1, 2, 3, 4, 5]
print(len(list20))

#获取列表中的最大值
list21 = [1, 2, 3, 4, 5]
print(max(list21))


#获取列表中的最小值
list22 = [1, 2, 3, 4, 5]
print(min(list22))

#查看元素在列表中出现的次数
list23 = [1, 2, 3, 4, 5,3,4, 5, 6]
print(list23.count(3))


num24 = 0
all = list23.count(3)
while num24 < all:
    list23.remove(3)
    num24 += 1
print(list23)

#reserve 倒序
list25 = [1 , 2,3 ,4 ,5]
list25.reverse()
print(list25)

# sort 排序  升序
list26 = [2 , 1,5 ,4 ,3]
list26.sort()
print(list26)

#拷贝
#浅拷贝   引用拷贝
list27 = [1, 2,3 ,4 ,5]
list28 = list27
list28[1] = 200
print(list28)
print(list27)
print(id(list28))
print(id(list27))
#深拷贝
list29= [1, 2,3 ,4 ,5]
list30 = list29.copy()
list30[1] = 200
print(list30)
print(list29)
print(id(list30))
print(id(list29))

#将元组转成列表
"""
list31 = list((3,4,5))
print(list31)
"""