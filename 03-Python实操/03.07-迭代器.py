""""
可迭代对象：可以至今作用与for循环的对象统称为可迭代对象
（Iterable），可以用isinstance（）去判断一个对象是否是Iterable对象
可以直接作用与for的数据类型一般分两种
1.集合数据类型：如list，tuple，dict，setstring
2.是generator，包括生成器和带yeild的generator function
"""
from collections import Iterable
print(isinstance([],Iterable))
print(isinstance((),Iterable))
print(isinstance({},Iterable))
print(isinstance("",Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(1,Iterable))


"""
迭代器：不但可以作用与for循环，还可以被next（）函数不断的调用并返回下一个值，
直到最后抛出一个错误（stopIteration）表示无法继续返回下一个值

可迭代对象：可以被next（）函数笤俑并不断返回下一个值的对象称为迭代器（Iterator对象）
可以使用isinstance（）函数判断一个对象是否Iterator对象
"""
from collections import Iterator
print(isinstance([],Iterator))
print(isinstance((),Iterator))
print(isinstance({},Iterator))
print(isinstance("",Iterator))
print(isinstance((x for x in range(10)),Iterator))

l = (x for x in [23,4,5,6,7,8,9])
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))

#转成Iterator
ll = iter([1,2,3,4,5,6])
print(next(ll))
print(next(ll))

print(isinstance(iter([])),Iterator)
print(isinstance(iter(())),Iterator)
print(isinstance(iter({})),Iterator)
print(isinstance(iter("")),Iterator)