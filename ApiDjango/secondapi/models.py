from django.db import models
import os
from rest_framework import serializers

os.environ.update({"DJANGO_SETTINGS_MODULE": "ApiDjango.settings"})

# Create your models here.

class userinfo(models.Model):
    id = models.AutoField(primary_key=True)
    test_id = models.IntegerField()
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