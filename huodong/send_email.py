#!usr/bin/env python
# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
import os

user = "songjianmin@17guagua.com"
pwd = "qscBnXcQb3p7CF48"
to = ["liujunchen@17guagua.com"]
msg = MIMEMultipart()
msg['Subject'] = "test"

email_content = "test内容"
content1 = MIMEText(email_content,"plain",'utf-8')
msg.attach(content1)

s = smtplib.SMTP('smtp.17guagua.com')
s.login(user,pwd)
for i in range(10):
    s.sendmail(user,to,msg.as_string())
print ("send ok!")
s.close()