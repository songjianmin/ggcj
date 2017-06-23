#!usr/bin/env python
# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
import os
import time

class Send_Email():
    def __init__(self,send_user="songjianmin@17guagua.com",pwd="qscBnXcQb3p7CF48",
                 rec_user=["songjianmin@17guagua.com"],
                 title_mail="test",
                 content_mail="test content1",
                 smtp_server = 'smtp.17guagua.com',
                 attch_addr = "E:\\Python-project\\Selenium\\ggcj\\huodong\\report"
                 ):
        self.user = send_user
        self.pwd = pwd
        self.rec_user = rec_user
        self.subject = title_mail
        self.content = content_mail
        self.smtp_server = smtp_server
        self.attch_addr = attch_addr

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

    def send_attch(self):

        lists = os.listdir(self.attch_addr)
        lists.sort(key=lambda fn:os.path.getmtime(self.attch_addr+"\\"+fn)
                   if not os.path.isdir(self.attch_addr+"\\"+fn) else 0)
        # for each in lists:
        #     print (each)
        # print (lists)
        print (u'最新的文件：'+lists[-1])
        # print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.path.getmtime(self.attch_addr+"\\"+lists[-1]))))

        file_new = os.path.join(self.attch_addr,lists[-1])
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


    def send_html(self):

        content_html = 'test<br><br><table border="1">' \
                       '<tr><th>Month</th><th>Savings</th></tr>' \
                       '<tr><td>January</td><td>$100</td></tr></table>'
        msg=MIMEMultipart()
        msg["Subject"]=self.subject
        msg["From"]=self.user
        toaddrlist = ""
        for each in self.rec_user:
            toaddrlist = each + "," + toaddrlist
        msg["to"] = toaddrlist

        content = MIMEText(content_html,'html','gb2312')
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