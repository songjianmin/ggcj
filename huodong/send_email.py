#!usr/bin/env python
# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
import os
import time


"""
附：傻瓜式发送各种类型附件方法---------------------------------------
飘逸的python - 发送带各种类型附件的邮件
基本思路就是，使用MIMEMultipart来标示这个邮件是多个部分组成的，然后attach各个部分。如果是附件，则add_header加入附件的声明。
在python中，MIME的这些对象的继承关系如下。
MIMEBase
    |-- MIMENonMultipart
        |-- MIMEApplication
        |-- MIMEAudio
        |-- MIMEImage
        |-- MIMEMessage
        |-- MIMEText
    |-- MIMEMultipart
一般来说，不会用到MIMEBase，而是直接使用它的继承类。MIMEMultipart有attach方法，而MIMENonMultipart没有，只能被attach。
MIME有很多种类型，这个略麻烦，如果附件是图片格式，我要用MIMEImage，如果是音频，要用MIMEAudio，如果是word、excel，我都不知道该用哪种MIME类型了，得上google去查。
最懒的方法就是，不管什么类型的附件，都用MIMEApplication，MIMEApplication默认子类型是application/octet-stream。
application/octet-stream表明“这是个二进制的文件，希望你们那边知道怎么处理”，然后客户端，比如qq邮箱，收到这个声明后，会根据文件扩展名来猜测。

下面上代码。

假设当前目录下有foo.xlsx/foo.jpg/foo.pdf/foo.mp3这4个文件。
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
_user = "sigeken@qq.com"
_pwd  = "***"
_to   = "402363522@qq.com"

#如名字所示Multipart就是分多个部分
msg = MIMEMultipart()
msg["Subject"] = "don't panic"
msg["From"]    = _user
msg["To"]      = _to

#---这是文字部分---
part = MIMEText("乔装打扮，不择手段")
msg.attach(part)

#---这是附件部分---
#xlsx类型附件
part = MIMEApplication(open('foo.xlsx','rb').read())
part.add_header('Content-Disposition', 'attachment', filename="foo.xlsx")
msg.attach(part)

#jpg类型附件
part = MIMEApplication(open('foo.jpg','rb').read())
part.add_header('Content-Disposition', 'attachment', filename="foo.jpg")
msg.attach(part)

#pdf类型附件
part = MIMEApplication(open('foo.pdf','rb').read())
part.add_header('Content-Disposition', 'attachment', filename="foo.pdf")
msg.attach(part)

#mp3类型附件
part = MIMEApplication(open('foo.mp3','rb').read())
part.add_header('Content-Disposition', 'attachment', filename="foo.mp3")
msg.attach(part)

s = smtplib.SMTP("smtp.qq.com", timeout=30)#连接smtp邮件服务器,端口默认是25
s.login(_user, _pwd)#登陆服务器
s.sendmail(_user, _to, msg.as_string())#发送邮件
s.close()

"""

class Send_Email():
    def __init__(self,send_user="songjianmin@17guagua.com",pwd="qscBnXcQb3p7CF48",
                 rec_user=["songjianmin@17guagua.com"],
                 title_mail="test",
                 content_mail="test content1",
                 smtp_server = 'smtp.17guagua.com',
                 ):
        self.user = send_user
        self.pwd = pwd
        self.rec_user = rec_user
        self.subject = title_mail
        self.content = content_mail
        self.smtp_server = smtp_server

    def send_text(self):

        toaddrlist = ''
        msg = MIMEMultipart()
        msg['Subject'] = self.subject
        msg['From'] = self.user
        for each in self.rec_user:
            toaddrlist = each+','+toaddrlist
        msg['to'] = toaddrlist

        # email_content = self.content
        content1 = MIMEText(self.content,"plain",'utf-8')
        msg.attach(content1)

        try:
            s = smtplib.SMTP(self.smtp_server,25)
            s.login(self.user,self.pwd)
            # for i in range(10):
            s.sendmail(self.user,self.rec_user,msg.as_string())
            print ("send ok!")
            s.close()
        except Exception as e:
            print (e,"----")
            print ("Error:无法发送邮件")

    def send_attch(self,attch_addr = "E:\\Python-project\\Selenium\\ggcj\\huodong\\report"):

        lists = os.listdir(attch_addr)
        lists.sort(key=lambda fn:os.path.getmtime(attch_addr+"\\"+fn)
                   if not os.path.isdir(attch_addr+"\\"+fn) else 0)
        # for each in lists:
        #     print (each)
        # print (lists)
        print (u'最新的文件：'+lists[-1])
        # print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.path.getmtime(attch_addr+"\\"+lists[-1]))))

        file_new = os.path.join(attch_addr,lists[-1])
        # print (file_new)
        msg = MIMEMultipart()
        msg['Subject'] = self.subject
        msg['From'] = self.user
        toaddrlist = ''
        for each in self.rec_user:
            toaddrlist = each + ',' + toaddrlist
        msg['to'] = toaddrlist

        # email_content = self.content
        content2 = MIMEText(open(file_new,'rb').read(), "base64", 'gb2312')
        content2["Content-Type"]='application/octet-stream'
        content2["Content-Disposition"] = 'attachment;filename=%s'%lists[-1]
        msg.attach(content2)

        content1 = MIMEText(self.content,"plain",'utf-8')
        msg.attach(content1)

        try:
            s = smtplib.SMTP(self.smtp_server, 25)
            s.login(self.user, self.pwd)
            # for i in range(10):
            s.sendmail(self.user, self.rec_user, msg.as_string())
            print("send ok!")
            s.close()
        except Exception as e:
            print(e, "----")
            print("Error:无法发送邮件")


    def send_html(self,content_html= 'test<br><br><table border="1">' \
                       '<tr><th>Month</th><th>Savings</th></tr>' \
                       '<tr><td>January</td><td>$100</td></tr></table>'):

        # content_html = 'test<br><br><table border="1">' \
        #                '<tr><th>Month</th><th>Savings</th></tr>' \
        #                '<tr><td>January</td><td>$100</td></tr></table>'
        msg=MIMEMultipart()
        msg["Subject"]=self.subject
        msg["From"]=self.user
        toaddrlist = ""
        for each in self.rec_user:
            toaddrlist = each + "," + toaddrlist
        msg["to"] = toaddrlist

        # content = MIMEText(content_html,'html','gb2312')
        content = MIMEText(content_html, 'html', 'gb2312')
        msg.attach(content)

        try:
            s = smtplib.SMTP(self.smtp_server,25)
            s.login(self.user,self.pwd)
            s.sendmail(self.user,self.rec_user,msg.as_string())
            s.close()
            print ("send ok")
        except Exception as e:
            print (e)
            print ("send fail !")



if __name__ == "__main__":
    send_email = Send_Email()
    # send_email.send_text()
    # send_email.send_attch()
    send_email.send_html()