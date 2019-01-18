"""
fetchone()
功能：获取下一个查询结果集，结果集是一个对象
fetchall()
功能：接受全部的返回的行

rowcount：是一个只读属性，返回execute（）方法影响的行数
"""

import pymysql

#连接数据库
#参数1：mysql服务所在主机的IP
#参数2：用户名
#参数3.密码
#参数4：要连接的数据库名
db = pymysql.connect("localhost","root","123","kaige")
#db = pymysql.connect("192.1.168.100","root","123","kaige")
#创建一个cursor对象
cursor = db.cursor()

sql = 'select * from bandcard where money>400'
try:
    cursor.execute(sql)
    #db.commit()  查询不用写
    reslist = cursor.fetchall()
    for row in reslist:
        print("%d-%d"%(row[0],row[1]))
except:
    #如果提交失败，回滚到上一次的数据
    db.rollback()
#断开
cursor.close()
db.close()

