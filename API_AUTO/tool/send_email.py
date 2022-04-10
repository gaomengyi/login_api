"""
发送邮件到指定账户
"""
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# 邮件发送的用户名和密码 密码需要获取第三方授权码
_user = "1186966522@qq.com"
_password = "zzvpudaeplrgiigh"
now = time.strftime("%Y-%m-%d %H:%M:%S")  # 获取时间戳


class SendEmail:
    def send_email(self, email_to, filepath):
        """
        email_to 收件方
        failpath 你要发送附件的地址
        如名字所示MIMEMultipart 是分多个部分
        """
        msg = MIMEMultipart()  # 创建MIMEMultipart类的实例
        msg['Subject'] = now + "高萌萌的测试报告"  # 邮件的标题：时间+高萌萌的测试报告
        msg['From'] = _user  # 发送人
        msg['To'] = email_to  # 接收人

        # ---这是文字部分---
        part = MIMEText("这次自动化的测试结果，请查收！")  # 邮件的文本
        msg.attach(part)

        # ---这是附件部分---
        part = MIMEApplication(open(filepath, "rb").read())
        part.add_header("Content-Disposition", "attachment", filename=filepath)
        msg.attach(part)
        s = smtplib.SMTP_SSL("smtp.qq.com", timeout=30)  # 连接服务器
        s.login(_user, _password)  # 登录服务器
        s.sendmail(_user, email_to, msg.as_string())  # 发送邮件
        s.close()


if __name__ == '__main__':
    SendEmail().send_email("2964781277@qq.com", r"E:\pycharm\code\ningmeng\API_AUTO\test_result\html_report\test.html")
