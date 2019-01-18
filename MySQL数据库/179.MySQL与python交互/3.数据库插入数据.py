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

sql = 'insert into bandcard values(0,500),(0,600),(0,700),(0,800)'
try:
    cursor.execute(sql)
    db.commit()
except:
    #如果提交失败，回滚到上一次的数据
    db.rollback()
#断开
cursor.close()
db.close()

