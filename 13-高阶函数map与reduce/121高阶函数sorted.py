#排序：冒泡排序，选择排序，      快速排序，插入法，计数器排序


#普通排序
list1 = [4,7,2,6,3]
list2 = sorted(list1)#默认升序排序
print(list1)
print(list2)

#按绝对值大小排序
list3 = [4,-7,2,-6,3]
#key接受函数来实现自定义排序规则
list4 = sorted(list3,key = abs)
print(list3)
print(list4)

#按降序
list5 = [4,7,2,6,3]
list6 = sorted(list5,reverse= True)
print(list5)
print(list6)

#按长短--函数可以自己写
def myLine(str):
    return len(str)
list7 = ["a111","b222","c33","d7854"]
list8 = sorted(list7,key = myLine)
print(list7)
print(list8)







