#!usr/bin/env python
# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
import os

class Send_email():
    def __init__(self,send_user="songjianmin@17guagua.com",pwd="qscBnXcQb3p7CF48",
                 rec_user=["songjianmin@17guagua.com"],
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

        msg = MIMEMultipart()
        msg['Subject'] = self.subject

        # email_content = self.content
        content1 = MIMEText(self.content,"plain",'utf-8')
        msg.attach(content1)

        s = smtplib.SMTP(self.smtp_server)
        s.login(self.user,self.pwd)
        # for i in range(10):
        s.sendmail(self.user,self.rec_user,msg.as_string())
        print ("send ok!")
        s.close()

if __name__ == "__main__":
    send_email = Send_email()
    send_email.send()
