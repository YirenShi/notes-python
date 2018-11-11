
#引入模块
#import
#格式：   import  module1[,module2,module3,.....,modulen]]
import time,random,os
#引入了自定义模块，不用加py后缀
import  sunck
#注意：一个模块只会引入一次，不管你执行了多少次import，防止模块被多次引入

#使用模块中的内容
#格式：模块名.函数名/变量名

sunck.saygood()
sunck.saynice()
sunck.sayhandsome()

print(sunck.TT)

#from....import 语句
#作用：从模块中导入一恶搞指定的部分到当前命名空间
#格式 from module import name1[name2,name3,....,namen]

from sunck import saygood

#程序内容的函数可以将模块中的同名函数覆盖
#def saygood():
#    print("***")

saygood()
#handsome()  没有引入handsome函数




















