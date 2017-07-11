from django.shortcuts import render
from django.http import HttpResponse

from secondapi.models import userinfo
# Create your views here.

def Create_Userinfo(request):

    userinfo.objects.create(id=int(request.GET['id']),test_id=int(request.GET['test_id']),test_name=request.GET['test_name'])


