#!usr/bin/env python
# -*- coding:utf-8 -*-

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ApiDjango.settings")

'''
Django 版本大于等于1.7的时候，需要加上下面两句
import django
django.setup()
否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''

import django
if django.VERSION >= (1,7):
    django.setup()

def main():
    from secondapi.models import Author
    f = open('oldauthor.txt','r',encoding='utf-8')  #此处制定编码方式，否则文件内容有汉子时会报错
    for line in f:
        print (line)
        name,qq,addr,email = line.split("****")
        print (name,qq,addr,email)
        Author.objects.get_or_create(name=name,qq=qq,addr=addr,email=email)
    f.close()

if __name__ == "__main__":
    main()
    print ("Done !")