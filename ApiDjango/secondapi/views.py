from django.shortcuts import render
from django.http import HttpResponse

from secondapi.models import userinfo
# Create your views here.

def Create_Userinfo(request):

    # userinfo.objects.create(id=int(request.GET['id']),test_id=int(request.GET['test_id']),test_name=request.GET['test_name'])   #insert sql
    # return HttpResponse("新增OK")

    # res=userinfo.objects.filter(id=1)  #select sql
    # return HttpResponse(res)

    res = userinfo.objects.all()
    string_id=""
    for each in res:
        string_id = string_id+str(each.test_id)+","
    return HttpResponse(string_id)

def home(request):
    string=u" 模板进阶，传参到html中"
    forlist = ["1.传递string到html",
               "2.for 循环 list",
               "3.显示字典内容",
               "4.条件判断",
               "5.模板上得到视图对应的网站",
               "6.模板中的逻辑操作",
               "7.模板中 获取当前网址，当前用户等"]
    info_dict = {'site':u"模板进阶",'content':u'传参到html'}

    iflist = map(str,range(100))
    # return render(request,'secondapi/home.html',{'string':string})
    # return render(request, 'secondapi/home.html', {'list': forlist})
    # return render(request, 'secondapi/home.html', {'dict': info_dict})
    return render(request, 'secondapi/home.html', {'iflist': iflist})

def index(request):

    return render(request,'secondapi/index.html')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    return HttpResponse(str(int(a)+int(b)))
