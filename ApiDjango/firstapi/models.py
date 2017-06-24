from django.db import models

# Create your models here.
class userinfo(models.Model):
    pk_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=80)