import time
class Admin(object):
    admin = "1"
    password = "1"

    def printAdminView(self):
        print("*************************************")
        print("*                                   *")
        print("*                                   *")
        print("*        欢迎登录凯歌银行           *")
        print("*                                   *")
        print("*                                   *")
        print("*************************************")

    def printsysFunctionView(self):
        print("*************************************")
        print("*     开户（1）   查询（2）   *")
        print("*     取款（3）   存款（4）   *")
        print("*     转账（5）   改密码（6） *")
        print("*     锁定（7）   解锁（8）   *")
        print("*     补卡（9）   销户（0）   *")
        print("*              退出（t）      *")
        print("*******************************")
        return 0

    def adminOption(self):
        inputAdmin = input("请输入管理员帐号：")
        if self.admin != inputAdmin:
            print("帐号输入有误！！")
            return -1
        inputPassword = input("请输入管理员密码：")
        if self.password != inputPassword:
            print("密码输入有误！！")
            return -1

        # 能执行到这里说明帐号密码正确
        print("操作成功！请稍后****")
        time.sleep(2)
        return 0####96\\22min讲解















