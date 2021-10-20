from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views import View
from .models import Project


def index(request):
    if request.method=="GET":
        return HttpResponse("Hello, GET1")
    elif request.method=="POST":
        return HttpResponse("Hello, POST")
    else:
        return HttpResponse("Hello, 其他方法")

class indexView(View):
    """
    主页类试图"""
    # def get(self,request):
    #     # return HttpResponse("Hello, GET")
    #     #从数据库查询数据
    #     data=[
    #         {
    #             "project_name":"1" ,
    #             "appname":"python"
    #         },
    #         {
    #             "project_name": "2",
    #             "appname": "python1"
    #         },
    #         {
    #             "project_name": "3",
    #             "appname": "python2"
    #         },
    #     ]
    #     return render(request,'index.html',locals())

    # def get(self,request,pk):
    #     return HttpResponse("Hello, GET")

    def get(self,request):
        #创建数据
        # #方法一
        # #创建模型类对象
        # ob=Project(name="使用类创建的项目",tester="test",developer="test",leader="test"
        #         ,publish_app="test")
        # #调用save（）保存
        # ob.save()

        #方法二
        Project.objects.create(name="使用objects()创建的项目",tester="test",developer="test",leader="test"
                ,publish_app="test")

        return HttpResponse("Hello, GET")

    def post(self,request):

        return HttpResponse("Hello, POST")
    def delete(self,request):
        return HttpResponse("Hello, delete")
    def put(self,request):
        return HttpResponse("Hello, put")