#!usr/bin/env python
# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
import os

user = "songjianmin@17guagua.com"
pwd = "*()2015Song"
to = ["songjinamin@17guagua.com","317804344@qq.com"]
msg = MIMEMultipart()
msg['Subject'] = "test"
content1 = MIMEText("正文test","plain",'utf-8')
msg.attach(content1)

s = smtplib.SMTP('smtp.163.com')
s.login(user,pwd)
s.sendmail(user,to,msg.as_string())
print ("send ok!")
s.close()