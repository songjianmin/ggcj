#!usr/bin/env python
# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
import os

class Send_email():
    def __init__(self,send_user="songjianmin@17guagua.com",pwd="qscBnXcQb3p7CF48",
                 rec_user=["songjianmin@17guagua.com","31780344@qq.com"],
                 title_mail="test",
                 content_mail="test content1",
                 smtp_server = 'smtp.17guagua.com'):
        self.user = send_user
        self.pwd = pwd
        self.rec_user = rec_user
        self.subject = title_mail
        self.content = content_mail
        self.smtp_server = smtp_server

    def send(self):

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

if __name__ == "__main__":
    send_email = Send_email()
    send_email.send()
