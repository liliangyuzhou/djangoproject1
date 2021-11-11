from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404
from rest_framework.views import APIView
#继承APIView，给查询列表提供排序，过滤，分页
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

from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination

from utils import mixins

class ProjectList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  GenericAPIView):
    # GenericAPIView是APIView的子类，具有APIView的所有功能
    #使用GenericAPIView必须要指定queryset和serializer_class两个类属性
    #queryset是当前类视图函数所需要的查询集
    #serializer_class是对应的序列化器
    queryset=Project.objects.all()
    serializer_class=serializer.ProjectModelSerializer
    #指定模型序列化器类那些字段需要过滤，可以在字段前面添加前缀，^（必须以什么开头），=，@，$ ，在源码中可以看到
    #该字段的列表里面的值必须和模型序列化器类的属性名称保持一致，那些参数需要进行过滤，列表中就写那些参数
    search_fields=['name','tester','id']

    #a.可以在全局配置文件中，指定对应的搜索引擎（对所有获取数据列表的功能都会支持过滤功能）
    #b.也可以在特定的类视图中指定filter_backends过滤
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields=['name','tester','id']

    #为了不全局配置搜索引擎，只对某个类视图生效，可以通过pagination_class指定搜索引擎
    pagination_class =PageNumberPagination

    def get(self, request,*args,**kwargs):
        return self.list(*args,**kwargs)

    def post(self, request,*args,**kwargs):
        return self.create(request,*args,**kwargs)



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


class ProjectDetail(mixins.RetriveModelMixin,
                    GenericAPIView):
    queryset = Project.objects.all()
    serializer_class = serializer.ProjectModelSerializer
    def get(self, request,*args,**kwargs):
        return self.retrive(*args,**kwargs)

    # def get_object(self, pk):
    #     try:
    #         # obj1 = Project.objects.get(id=pk)
    #         obj1 = self.queryset.get(id=pk)
    #     except Project.DoesNotExist:
    #         # 不存在，可以抛出一个404的异常，这个异常是django自带的
    #         raise Http404
    #     return obj1

    def put(self, request, pk):
        """更新某个项目"""
        # 1.校验前端传递的pk（项目id）值，类型是否正确，在数据库中是否存在
        # 2.获取到数据库中该id查询的结果对象
        # obj2 = self.get_object(pk=pk)
        obj2 = self.get_object()

        # print(obj2.name,type(obj2.name))
        # 3.从前端获取json格式的数据
        # json_data = request.body.decode('utf-8')
        # python_data = json.loads(json_data)
        # print(python_data)
        # print(python_data['name'])
        # print(obj2.name)
        # ser=serializer.ProjectModelSerializer(instance=obj2,data=python_data)
        # ser = serializer.ProjectModelSerializer(instance=obj2, data=request.data)
        # ser = self.serializer_class(instance=obj2, data=request.data)
        ser = self.get_serializer(instance=obj2, data=request.data)

        #使用的apiview后不需要我们主动捕获异常，会自动处理
        ser.is_valid(raise_exception=True)

        # 校验前端输入的数据
        # try:
        #     ser.is_valid(raise_exception=True)
        # except Exception as e:
        #     # 只有在调用is_valid(raise_exception=True)
        #     # 方法之后，才可以调用errors属性，获取校验的错误提示
        #     return JsonResponse(ser.errors)

        # 更新项目
        #序列化器对象ser直接调用save()方法，调用的是序列化器的create方法，并且列化器只需要传递data属性
        #要使用save方法调用update方法，要给序列化器同时传递instance属性和data属性
        ser.save()
        # obj2.name = ser.validated_data['name']
        # obj2.leader = ser.validated_data['leader']
        # obj2.tester = ser.validated_data['tester']
        # obj2.developer = ser.validated_data['developer']
        # obj2.desc = ser.validated_data['desc']
        # obj2.publish_app = ser.validated_data['publish_app']
        # obj2.save()
        # print(type(obj2.name))

        # 将更新后的项目转化为字典
        # one_project = {
        #     "name": obj2.name,
        #     "leader": obj2.leader,
        #     "tester": obj2.tester,
        #     "developer": obj2.developer,
        #     "publish_app": obj2.publish_app,
        #     "desc": obj2.desc
        # }

        # print(one_project)
        # return JsonResponse(one_project,status=201)
        # ser=serializer.ProjectSerializer(instance=obj2)
        # return JsonResponse(ser.data,status=201)
        return Response(ser.data,status=status.HTTP_201_CREATED)


    def delete(self,request,pk):
        # 1.校验前端传递的pk（项目id）值，类型是否正确，在数据库中是否存在
        # 2.获取到数据库中该id查询的结果对象
        # obj2 =self.get_object(pk)
        obj2=self.get_object()
        obj2.delete()

        # return JsonResponse(None,safe=False,status=204)
        return Response(None,status=status.HTTP_200_OK)
