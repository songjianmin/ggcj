#!usr/bin/env python
# -*- coding:utf-8 -*-

import random
from secondapi.models import Author,Article,Tag

author_name_list = ["weizhongxiang","yaoming","libingbing","liuruoying","songjianmin"]
article_title_list = ["Django 教程","Python 课程","美女","帅哥"]

def create_author():
    for author_name in author_name_list:
        author,created = Author.objects.get_or_create(name=author_name)
        author.qq =