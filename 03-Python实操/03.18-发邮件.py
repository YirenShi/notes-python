
#导入发邮件的库
import smtplib
#邮件文本
from email.mime.text import MIMEText

#SMTP服务器
SMTPSever ="smtp.163.com"
#发邮件的地址
sender = "a964640116@163.com"

#发送者邮箱的密码
password = "a051555"

#设置发送的内容
message = "sunck is a good man"

#转换成邮件文本
msg = MIMEText(message)

#标题
msg["Subject"] = "来自帅哥的问候"


#发送者
msg["From"] = sender

#创建SMTP服务器
mailSever = smtplib.SMTP(SMTPSever,25)

#登录邮箱
mailSever.login(sender,password)

#发送邮件
mailSever.sendmail(sender,["a964640116@163.com"],msg.as_string())

#退出邮箱
mailSever.quit()