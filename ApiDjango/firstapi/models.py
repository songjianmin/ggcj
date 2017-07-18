from django.db import models
# from rest_framework import serializers
import os
import sys
# import django
from django.core.handlers.wsgi import WSGIHandler


# import sys
# # print (sys.path)
# sys.path.append('E:\\Python-project\\Selenium\\ggcj\\ApiDjango')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ApiDjango.settings'
# django.setup()
application = WSGIHandler()

# Create your models here.
class userinfo(models.Model):
    pk_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=80)

    def __str__(self):
        return self.user_name

# if __name__=="__main__":
#     userinfo.objects.create(user_id=103,user_name="www")
