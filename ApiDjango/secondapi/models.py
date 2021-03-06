from django.db import models
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ApiDjango.settings")
from rest_framework import serializers

# import django
# if django.VERSION >= (1,7):
#     django.setup()


# Create your models here.

class userinfo(models.Model):
    id = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=80)

    def __str__(self):
        return self.test_name

class UserSerializer(serializers.HyperlinkedModelSerializer):
    ser_id = models.AutoField(primary_key=True)
    ser_test = models.CharField(max_length=80)

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    group_id = models.AutoField(primary_key=True)
    group_test = models.CharField(max_length=80)

class Author(models.Model):
    name = models.CharField(max_length=50)
    qq = models.CharField(max_length=10)
    addr =  models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author)
    content = models.TextField()
    score = models.IntegerField()
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Person(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


    def my_property(self):
        return self.first_name + " " + self.last_name
    my_property.short_description = "姓名"  #给my_property增加一个short_description属性

    full_name = property(my_property)   # @property 可以将python定义的函数“当做”属性访问，从而提供更加友好访问方式

