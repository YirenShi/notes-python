"""
break 语句
作用：跳出for和while循环
注意：只能跳出距离他最近的那一层循环
"""
for i in range(10):
    print(i)
    if i == 5:
        break
num = 1
while num <= 10:
    print(num)
    num += 1
    if num ==3:
        break
#循环语句可以有else语句，break导柱循环截止，不会执行else下面的语句
else:
    print("sunck is a good man")
