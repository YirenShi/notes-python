"""
对应于元组（tuple）与列表（list）的关系，对于集合（set），Python提供了一种叫做不可变集合（frozen set）的数据结构。

使用 frozenset 来进行创建：

In [1]:
s = frozenset([1, 2, 3, 'a', 1])
s
Out[1]:
frozenset({1, 2, 3, 'a'})
与集合不同的是，不可变集合一旦创建就不可以改变。

不可变集合的一个主要应用是用来作为字典的键，例如用一个字典来记录两个城市之间的距离：

In [2]:
flight_distance = {}
city_pair = frozenset(['Los Angeles', 'New York'])
flight_distance[city_pair] = 2498
flight_distance[frozenset(['Austin', 'Los Angeles'])] = 1233
flight_distance[frozenset(['Austin', 'New York'])] = 1515
flight_distance
Out[2]:
{frozenset({'Austin', 'New York'}): 1515,
 frozenset({'Austin', 'Los Angeles'}): 1233,
 frozenset({'Los Angeles', 'New York'}): 2498}
由于集合不分顺序，所以不同顺序不会影响查阅结果：

In [3]:
flight_distance[frozenset(['New York','Austin'])]
Out[3]:
1515
In [4]:
flight_distance[frozenset(['Austin','New York'])]
Out[4]:
1515
"""