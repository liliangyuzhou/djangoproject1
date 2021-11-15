from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404
from rest_framework.views import APIView
# 继承APIView，给查询列表提供排序，过滤，分页
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from polls.models import Project
# Create your views here.
from django.views import View
import json
# from .serializer import ProjectModelSerializer
from projects import serializer
from rest_framework.viewsets import ModelViewSet

from rest_framework import viewsets

from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action

# from utils import mixins
from rest_framework import mixins
from rest_framework import generics


# class ProjectList(generics.ListCreateAPIView):
#     # GenericAPIView是APIView的子类，具有APIView的所有功能
#     # 使用GenericAPIView必须要指定queryset和serializer_class两个类属性
#     # queryset是当前类视图函数所需要的查询集
#     # serializer_class是对应的序列化器
#     queryset = Project.objects.all()
#     serializer_class = serializer.ProjectModelSerializer
#     # 指定模型序列化器类那些字段需要过滤，可以在字段前面添加前缀，^（必须以什么开头），=，@，$ ，在源码中可以看到
#     # 该字段的列表里面的值必须和模型序列化器类的属性名称保持一致，那些参数需要进行过滤，列表中就写那些参数
#     search_fields = ['name', 'tester', 'id']
#
#     # a.可以在全局配置文件中，指定对应的搜索引擎（对所有获取数据列表的功能都会支持过滤功能）
#     # b.也可以在特定的类视图中指定filter_backends过滤
#     filter_backends = [SearchFilter, OrderingFilter]
#     ordering_fields = ['name', 'tester', 'id']
#
#     # 为了不全局配置搜索引擎，只对某个类视图生效，可以通过pagination_class指定搜索引擎
#     pagination_class = PageNumberPagination


# class ProjectDetail(View):
#     def get(self, request, pk):
#         """获取数据详情"""
#         # 1.校验前端传递的pk（项目id）值，类型是否正确，在数据库中是否存在
#
#         # 2.获取到数据库中该id查询的结果对象
#         obj1 = Project.objects.get(id=pk)
#         # 3.将获取到的模型类对象转化为字典，返回
#         one_project = {
#             "name": obj1.name,
#             "leader": obj1.leader,
#             "tester": obj1.tester,
#             "developer": obj1.developer,
#             "publish_app": obj1.publish_app,
#             "desc": obj1.desc
#         }
#         return JsonResponse(one_project)
#
#     def put(self, request, pk):
#         """更新某个项目"""
#         # 1.校验前端传递的pk（项目id）值，类型是否正确，在数据库中是否存在
#         # 2.获取到数据库中该id查询的结果对象
#         obj2 = Project.objects.get(id=pk)
#         print(obj2.name,type(obj2.name))
#         # 3.从前端获取json格式的数据
#         json_data = request.body.decode('utf-8')
#         python_data = json.loads(json_data)
#         print(python_data)
#         print(python_data['name'])
#         # print(obj2.name)
#
#         # 更新项目
#         obj2.name = python_data['name'],
#         obj2.leader = python_data['leader'],
#         obj2.tester = python_data['tester'],
#         obj2.developer = python_data['developer'],
#         obj2.desc = python_data['desc'],
#         obj2.publish_app = python_data['publish_app']
#         obj2.save()
#         print(type(obj2.name))
#         # 将更新后的项目转化为字典
#         one_project = {
#             "name": obj2.name,
#             "leader": obj2.leader,
#             "tester": obj2.tester,
#             "developer": obj2.developer,
#             "publish_app": obj2.publish_app,
#             "desc": obj2.desc
#         }
#         print(one_project)
#         return JsonResponse(one_project,status=201)
#
#
#     def delete(self,request,pk):
#         # 1.校验前端传递的pk（项目id）值，类型是否正确，在数据库中是否存在
#         # 2.获取到数据库中该id查询的结果对象
#         obj2 = Project.objects.get(id=pk)
#         obj2.delete()
#
#         return JsonResponse(None,safe=False,status=204)


# class ProjectViewSet(ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectModelSerializer


# class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Project.objects.all()
#     serializer_class = serializer.ProjectModelSerializer


#如果两个类视图合并，一定要继承ViewSet
# 会出现一些问题？
#两个get方法会有冲突
#如果使用mixin中提供的拓展方法（action），当前drf是无法识别这些action

#1。继承ViewSet，
#ViewSet继承ViewSetMixin, views.APIView
#就支持这些action，并在定义url路由时，可以在as_view({'固定方法名'：'action名称'})
#这里所有的action需要自己定义，并且不具有分页，过滤等功能
# class ProjectViewSet(viewsets.ViewSet):
# 2。继承GenericViewSet
#ViewSetMixin, generics.GenericAPIView
#支持分页，过滤，排序等功能
#仅仅继承viewsets.GenericViewSet但是还是没有这些action，如何拿到action呢，还需要继承其他类
# class ProjectViewSet(viewsets.GenericViewSet):

#可以继续继承各种mixin，同时继承viewsets.GenericViewSet，这个类放到后面
#可以按照需求继承mixin
# class ProjectViewSet(mixins.RetrieveModelMixin,
#                      mixins.CreateModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.ListModelMixin,
#                      mixins.DestroyModelMixin,
#                      viewsets.GenericViewSet):
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = serializer.ProjectModelSerializer
    # 指定模型序列化器类那些字段需要过滤，可以在字段前面添加前缀，^（必须以什么开头），=，@，$ ，在源码中可以看到
    # 该字段的列表里面的值必须和模型序列化器类的属性名称保持一致，那些参数需要进行过滤，列表中就写那些参数
    search_fields = ['name', 'tester', 'id']

    # a.可以在全局配置文件中，指定对应的搜索引擎（对所有获取数据列表的功能都会支持过滤功能）
    # b.也可以在特定的类视图中指定filter_backends过滤
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['name', 'tester', 'id']

    # 为了不全局配置搜索引擎，只对某个类视图生效，可以通过pagination_class指定搜索引擎
    pagination_class = PageNumberPagination

    #可以使用action装饰器，自定义指定的action
    #如果不写methods，默认是get方法
    #如果该方法支持多种请求方法methods=['GET','POST']
    #detail参数指定action是否是详情接口（是否需要传递主键ID值）
    # 如果接口需要传递id值，那么需要将detail参数改为True，否则需要传False
    #  url_path指定url的路径字符串,默认是函数名称
    #  url_name指定url的名称,默认是函数名称
    @action(methods=['GET','POST'],detail=False)
    def names(self,request,*args,**kwargs):
        queryset=self.get_queryset()
        name_list=[]
        for obj in queryset:
            # name_list.append(obj.name)
            name_list.append({'项目名称':obj.name})
        return Response(name_list,status=200)
