from django.contrib import admin

# Register your models here.
from .models import Author,Article,Tag,userinfo

class authorlist(admin.ModelAdmin):
    list_display = ['name','qq','addr','email']

class articlelist(admin.ModelAdmin):
    list_display = ['title','author','content','score',Tag]

class taglist(admin.ModelAdmin):
    list_display = ['name',]

admin.site.register(Author,authorlist)
admin.site.register(Article,articlelist)
admin.site.register(Tag,taglist)
admin.site.register(userinfo)