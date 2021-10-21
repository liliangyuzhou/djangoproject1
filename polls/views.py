from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views import View
from .models import Project
from django.db.models import Q
from interfaces.models import Interfaces


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

    # def get(self,request):
    #     #创建数据
    #     # #方法一
    #     # #创建模型类对象
    #     # ob=Project(name="使用类创建的项目",tester="test",developer="test",leader="test"
    #     #         ,publish_app="test")
    #     # #调用save（）保存
    #     # ob.save()
    #
    #     #方法二
    #     Project.objects.create(name="使用objects()创建的项目",tester="test",developer="test",leader="test"
    #             ,publish_app="test")
    #
    #     return HttpResponse("Hello, GET")

    def get(self,request):
        #获取数据
        # #1.获取一个数据表的所有记录
        # #QuerySet查询集就相当于一个列表（存放所有项目对象的列表），
        # res=Project.objects.all()
        # print(res)
        # print(res[0].name)
        # #循环取出所有对象的leader参数
        # for i in res:
        #     print(i.leader)

        # #获取某一个（多个）指定的记录，get(),get里面需要传递参数，相当于where后面的条件.只能获取一条记录
        # #如果返回多条记录，或者查询的记录不存在，会抛出异常
        # #get方法的参数往往为主键或者唯一健
        # #返回一个project对象
        # one_ob=Project.objects.get(id=1)
        # #根据对象获取表中的其他属性字段
        # print(one_ob.developer)



        # # 3获取某一些记录，filter()或者exclude()
        # res=Project.objects.filter(pk=1)
        # print(res)
        # #获取leader="李亮"的所有数据
        # res1 = Project.objects.filter(leader="李亮")
        # print(res1)
        # #使用模糊查询，获取leader包含"李"的所有数据
        # res1 = Project.objects.filter(leader__contains="李")
        # print(res1)
        # res1 = Project.objects.filter(leader__icontains="李")
        # print(res1)
        # #查询指定以"李"开头的所有内容,加i忽略大小写
        # res1 = Project.objects.filter(leader__startswith="李")
        # res1 = Project.objects.filter(leader__istartswith="李")
        # print(res1)
        # # 查询指定以"李"结尾的所有内容,加i忽略大小写
        # res1 = Project.objects.filter(leader__endswith="李")
        # res1 = Project.objects.filter(leader__iendswith="李")
        # print(res1)
        # #查询leader是"李亮"或者"test"的这个范围所有数据
        # res1 = Project.objects.filter(leader__in=["李亮","test"])
        # print(res1)
        # #不满足条件的数据，这里意思是查询除了pk=1的数据
        # res = Project.objects.exclude(pk=1)
        # print(res)
        # 4.关联查询
        #根据字表字段  子表名称__字表字段名来查询，也可以子表名称__字表字段名__参数等
        # res=Project.objects.filter(interfaces__name="接口1")
        # print(res)
        # #5.比较查询
        # #id大于2 的所有项目 __gt 大于  __gte 大于等于  __lt 小于   __lte 小于等于
        # res=Project.objects.filter(id__gt=2)
        # print(res)
        #
        # #6逻辑关系，多个条件查询
        # #与
        # res = Project.objects.filter(name="python",leader="李亮")
        # print(res)
        # #或,使用Q变量，多个条件使用｜
        # res = Project.objects.filter(Q(name="python")|Q(leader="李亮"))
        # print(res)
        # #7.查询集的操作
        # #查询结果集相当于一个列表，支持列表中的大多数操作（通过数字获取索引值；正向切片，不支持负数切片；for等）
        # #查询集是对数据库操作的一种优化
        # #查询集会缓存结果，第一次查库，第二次查缓存
        # #支持惰性查询
        # #查询集还支持链式操作
        # res=Project.objects.filter(name="python")
        # print(res)
        # res.filter(leader="李亮1")
        # print(res)
        # res = Project.objects.filter(leader="李亮")
        # print(res)
        # res = Project.objects.filter(leader="李亮").first()
        # print(res)

        # # 更新操作
        # #首先要获取到要修改的模型类
        # #然后修改
        # #保存
        # res=Project.objects.get(pk=1)
        # res.leader="修改"
        # res.save()

        # #删除操作
        # #首先要获取到要删除的模型类
        # #然后删除
        # res = Project.objects.get(pk=6)
        # res.delete()

        #排序操作
        # 取出id》=3的数据，并且按照接口名称排序
        #默认生序，降序'-name'
        res=Project.objects.filter(id__gte=3).order_by('name')
        print(res)
        res = Project.objects.filter(id__gte=3).order_by('-name','publish_app')
        print(res)
        return HttpResponse("Hello, GET")




    def post(self,request):

        return HttpResponse("Hello, POST")
    def delete(self,request):
        return HttpResponse("Hello, delete")
    def put(self,request):
        return HttpResponse("Hello, put")