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

class ProjectList(GenericAPIView):
    # GenericAPIView是APIView的子类，具有APIView的所有功能
    #使用GenericAPIView必须要指定queryset和serializer_class两个类属性
    #queryset是当前类视图函数所需要的查询集
    #serializer_class是对应的序列化器
    queryset=Project.objects.all()
    serializer_class=serializer.ProjectModelSerializer

    def get(self, request):
        # 1.从数据库中获取所有的项目信息
        # obj_list = Project.objects.all()
        # obj_list = self.queryset
        #GenericAPIView不要直接使用queryset属性来获取查询集
        #需要使用self.get_queryset()来获取查询集，因为更加灵活，后面可以重写父类的get_queryset()
        obj_list = self.get_queryset()

        # # 将数据库模型实例转化为字典类型（嵌套字典的列表）
        # project_list = []
        # for i in obj_list:
        #     one_project = {
        #         "name": i.name,
        #         "leader": i.leader,
        #         "tester": i.tester,
        #         "developer": i.developer,
        #         "publish_app": i.publish_app,
        #     }
        #     project_list.append(one_project)
        # return JsonResponse(project_list, safe=False)
        # ser=serializer.ProjectModelSerializer(instance=obj_list,many=True)

        #同样的GenericAPIView中不要直接通过类属性serializer_class来获取序列化器
        #使用self.get_serializer来获取序列化器
        # ser=self.serializer_class(instance=obj_list,many=True)
        ser=self.get_serializer(instance=obj_list,many=True)


        # return JsonResponse(ser.data,safe=False)
        # return HttpResponse("Hello, GET")
        return Response(ser.data,status=status.HTTP_200_OK)

    def post(self, request):
        """新增项目"""
        # 1. 从前端获取json格式的数据，转换为python中的类型
        # 为了严谨性，这里需要做各种复杂的校验
        # 比如：是否是json，传递的项目数据是否符合要求，有些必传参数是否携带
        # json_data = request.body.decode('utf-8')
        # python_data = json.loads(json_data)
        # ser=serializer.ProjectModelSerializer(data=python_data)
        # ser = serializer.ProjectModelSerializer(data=request.data)
        # ser = self.serializer_class(data=request.data)
        ser = self.get_serializer(data=request.data)
        #校验前端输入的数据
        # try:
        #     ser.is_valid(raise_exception=True)
        # except Exception:
        #     # 只有在调用is_valid(raise_exception=True)
        #     # 方法之后，才可以调用errors属性，获取校验的错误提示
        #     return JsonResponse(ser.errors)
        ser.is_valid(raise_exception=True)

        # 2.向数据库中新增项目
        # obj=Project.objects.create(name=python_data['name'],
        #                        leader=python_data["leader"],
        #                        tester=python_data['tester'],
        #                        developer=python_data['developer'],
        #                        desc=python_data['desc'],
        #                        publish_app=python_data['publish_app'],
        #                        desc=python_data['desc'])
        #  **字典，可以将字典key-value键值对拆为关键字参数key=value


        # obj = Project.objects.create(**python_data)
        # 校验成功后的数据使用ser.validated_data
        # obj = Project.objects.create(**ser.validated_data)

        #1。在序列化器中调用了create（）方法，要在试图函数中使用序列化器对象调用save（）方法
        #2。如果在创建序列化器对象的时候，只给data传参，那么调用save（）方法，实际是调用的序列化器的create（）方法
        #3。如果给save（）传递关键字参数，实际上是放到了validated_data里面，key值相同就是覆盖，不同的就是添加
        # ser.save(user="李亮")
        ser.save()
        # 3.将模型类对象转化为字典，然后返回(一般restful风格的接口都要求有返回）

        # one_project = {
        #     "name": obj.name,
        #     "leader": obj.leader,
        #     "tester": obj.tester,
        #     "developer": obj.developer,
        #     "publish_app": obj.publish_app,
        #     "desc": obj.desc
        # }
        # return JsonResponse(one_project,status=201)
        ##### 这里写错了，只需要一个序列化器对象，之前是分开写序列化输出，和序列化输入的
        ##### ser=serializer.ProjectSerializer(obj)
        # return JsonResponse(ser.data)
        #在drf框架中，一定要用Response来进行返回
        #response是httpresponse的子类，具有httpresponse的所有功能
        #可以自动根据请求头中的accept参数，来返回相应数据格式到前端

        #第一个参数为python中的常用数据类型（字典，嵌套字典列表），尽量使序列化器类.data
        #status指定相应状态码，content_type指定响应体数据类型
        return Response(ser.data,status=status.HTTP_200_OK)


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


class ProjectDetail(GenericAPIView):
    queryset = Project.objects.all()
    serializer_class = serializer.ProjectModelSerializer
    def get(self, request, pk):
        """获取数据详情"""
        # 1.校验前端传递的pk（项目id）值，类型是否正确，在数据库中是否存在

        # 2.获取到数据库中该id查询的结果对象
        # obj1 = self.get_object(pk)
        #使用GenericAPIView中的self.get_object()来获取单个模型对象，就不要我们使用自己自定义的get_object()
        obj1=self.get_object()
        # 3.将获取到的模型类对象转化为字典，返回
        # one_project = {
        #     "name": obj1.name,
        #     "leader": obj1.leader,
        #     "tester": obj1.tester,
        #     "developer": obj1.developer,
        #     "publish_app": obj1.publish_app,
        #     "desc": obj1.desc
        # }
        #1.通过模型类对象（或者查询集），传给instance参数，可以进行序列化操作
        #2.通过序列化器ProjectSerializer对象的data属性，就可以获得转化之后的字典
        # ser=self.serializer_class(instance=obj1)
        ser=self.get_serializer(instance=obj1)

        #加入json_dumps_params={"ensure_ascii":False}可以调用接口在浏览器上，展示中文
        # return JsonResponse(ser.data,json_dumps_params={"ensure_ascii":False})
        return Response(ser.data,status=status.HTTP_200_OK)

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
