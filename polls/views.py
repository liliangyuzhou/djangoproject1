from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views import View


def index(request):
    if request.method=="GET":
        return HttpResponse("Hello, GET")
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

    def get(self,request,pk):
        return HttpResponse("Hello, GET")

    def post(self,request):

        return HttpResponse("Hello, POST")
    def delete(self,request):
        return HttpResponse("Hello, delete")
    def put(self,request):
        return HttpResponse("Hello, put")