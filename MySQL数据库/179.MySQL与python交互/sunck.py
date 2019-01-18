import pymysql

class sunckSql():
    def __init__(self,host,user,password,dbName):
        self.host = host
        self.user = user
        self.password = password
        self.dbName = dbName

    def connect(self):
        self.db = pymysql.connect(self.host,self.user,self.password,self.dbName)
        self.cursor = self.db.cursor()

    def close(self):
        self.curse.close()
        self.db.close()

    def get_one(self,sql):
        res = None
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.close()
        except:
            print("查询失败")
        return res

    def get_all(self,sql):
        res = ()
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except:
            print("查询失败")
        return res

    def insert(self,sql):
        return self._edit(sql)

    def update(self,sql):
        return self._edit(sql)
    def delete(self,sql):
        return self._edit(sql)

    def _edit(self,sql):
        count = 0
        try:
            self.connect()
            count = self.cursor.excute(sql)
            self.db.commit()
            self.close()
        except:
            print("事物提交失败")
            self.db.rollback()