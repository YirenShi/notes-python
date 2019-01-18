import itertools
import time

#myList = list(itertools.product([1,2,3,4,5,6,7,8,9,0],repeat = 3))
#print(myList)
password = ("".join(x) for x in itertools.product("1234567890",repeat = 3))
#print(len(myList))

while True:
    try:
        str = next(password)
        print(str)
    except StopIteration as e:
        break





