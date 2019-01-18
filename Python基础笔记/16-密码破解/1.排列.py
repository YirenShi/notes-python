import itertools
#将可迭代的对象转为迭代器

myList = list(itertools.permutations([1,2,3,4],3))
print(myList)
print(len(myList))

"""
排列的可能性次数：n！/（n-m）！
"""










