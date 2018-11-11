import doctest
#docttest模块可以提取注释中的代码执行
#docttest严格按照Python交互模式的输入提取  前面需加空格
def mySum(x,y):
    """
    求两个数的和

    :param x: first num
    :param y: second num
    :return: sum
    example
    #前面需加空格
    >>> print(mySum(1,2))
    3

    """
    return x + y + 1


print(mySum(1,2))
#进行文档测试
doctest.testmod()









