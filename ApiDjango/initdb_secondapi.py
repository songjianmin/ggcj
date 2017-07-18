#!usr/bin/env python
# -*- coding:utf-8 -*-

import random
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

from secondapi.models import Author,Article,Tag
author_name_list = ["weizhongxiang","yaoming","libingbing","liuruoying","songjianmin"]
article_title_list = ["Django 教程","Python 课程","美女","帅哥"]

def create_author():
    for author_name in author_name_list:
        author,created = Author.objects.get_or_create(name=author_name)
        author.qq = "".join(str(random.choice(range(10))) for _ in range(9))
        author.addr = 'addr_%s'%(random.randrange(1,10))
        author.email = '%s@17guagua.com'% (author.addr)
        author.save()

def create_articles_and_tags():

    for article_title in article_title_list:
        tag_name = article_title.split(" ",1)[0]
        tag,created = Tag.objects.get_or_create(name=tag_name)
        random_author = random.choice(Author.objects.all())
        for i in range(1,21):
            title = '%s_%s'%(article_title,i)
            article,created = Article.objects.get_or_create(title=title,defaults={
                'author':random_author,
                'content':'%s 正文'%title,
                'score':random.randrange(70,101),
            })
            article.tags.add(tag)

def main():
    create_author()
    create_articles_and_tags()

if __name__ == "__main__":
    main()
    print ("Done")