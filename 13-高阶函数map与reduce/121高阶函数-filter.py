"""
原型：filter（fn,lsd)
#参数1是函数
#参数2是序列
功能：用于过滤序列
白话文：把传如的函数依次作用与序列的每个元素，根据返回的是True还是False决定是否保留该元素
"""

list1 = [1,2,3,4,5]
def func(num):
    #偶数保留，
    if num %2 == 0:
        return True
    #基数剔除
    return False
l = filter(func,list1)
#func[1]
print(list(l))

data = [["姓名","年龄","爱好"],["tom","26","无"],["hanmeimie","28","金钱"]]
def func2(v):
    v = str(v)
    if v == "无":
        return False
    return True
for line in data:
    m = filter(func2,line)
    print(list(m))











