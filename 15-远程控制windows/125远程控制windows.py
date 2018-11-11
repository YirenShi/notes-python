import telnetlib

def telnetDoSomeThing(IP,user,password,command):
    try:
        # 链接服务器
        telnet = telnetlib.Telnet(IP)
        # 设置调试级别
        telnet.set_debuglevel(2)
        # 读取输入用户名信息      匹配信息需根据版本及系统进行实际修改
        rt = telnet.read_until("Login username:".encode("utf-8"))
        # 写入用户名          回车键
        telnet.write((user + "\r\n").encode("utf-8"))

        # 读取输入用户密码信息
        rt = telnet.read_until("Login password:".encode("utf-8"))
        # 写入用户名          回车键
        telnet.write((password + "\r\n").encode("utf-8"))

        # 读取验证IP
        rt = telnet.read_until("Domain name:".encode("utf-8"))
        # 写入密码          回车键
        telnet.write((password + "\r\n").encode("utf-8"))

        # 登录成功，写指令
        rt = telnet.read_until(">".encode("utf-8"))
        # 写入指令          回车键
        telnet.write((command + "\r\n").encode("utf-8"))

        # 命令执行成功，会继续读到 >
        # 失败一般不会是>
        rt = telnet.read_until(">".encode("utf-8"))
        # 断开连接
        telnet.close()
        return True
    except:
        return False

if __name__ =="__main__":
    IP = "10.0.142.197"
    user = "xumingbin"
    password = "******"
    command = "tasklist"
    print(telnetDoSomeThing(IP, user, password, command))
