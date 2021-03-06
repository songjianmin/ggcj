from django.contrib import admin

# Register your models here.
from .models import Author,Article,Tag,userinfo,Person

class authorlist(admin.ModelAdmin):
    list_display = ['name','qq','addr','email']
    search_fields = ['name','qq','addr']
    list_filter = ['name','qq',]

class articlelist(admin.ModelAdmin):
    list_display = ['title','author','content','score',Tag]

class taglist(admin.ModelAdmin):
    list_display = ['name',]

class personlist(admin.ModelAdmin):
    list_display = ['my_property',]


# class PersonAdmin(admin.ModelAdmin):
#     list_filter = ('my_property',)

admin.site.register(Author,authorlist)
admin.site.register(Article,articlelist)
admin.site.register(Tag,taglist)
admin.site.register(userinfo)
admin.site.register(Person,personlist)
