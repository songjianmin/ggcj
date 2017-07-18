from django.contrib import admin

# Register your models here.
from .models import userinfo

class alllist(admin.ModelAdmin):
    list_display = ['pk_id','user_id','user_name']

admin.site.register(userinfo,alllist)
