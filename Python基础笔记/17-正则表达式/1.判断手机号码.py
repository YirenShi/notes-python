"""
给你一串字符串，判断是否是手机号码

"""
import re

def checkPhone(str):
    if len(str) != 11:
        return False
    elif str[0] != "1":
        return False
    elif str[1:3] != "39"  and str[1:3] != "31" :
        return False
    for i in range(3,11):
        if str[i] >  "9" or str[i] < "0" :
            return False
    return True


def checkPhone2(str):
    #13917031446
    part = r"^1(([3578]\d)|(47))\d{8}$"
    res = re.findall(part,str)
    print(res)
def checkPhone3(str):
    #13917031446
    part = r"(1(([3578]\d)|(47))\d{8})"
    res = re.findall(part,str)
    print(res)
"""
print(checkPhone("13917031446"))
print(checkPhone("183170314465"))
print(checkPhone("1831703144"))
print(checkPhone("28317031446"))
print(checkPhone("18317031446"))
print("--------")
print(checkPhone2("13917031446"))
print(checkPhone2("183170314465"))
print(checkPhone2("1831703144"))
print(checkPhone2("28317031446"))
print(checkPhone2("18317031446"))
"""
checkPhone3("asdasd18317031446safrsdf18317031446")
