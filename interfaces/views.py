from django.shortcuts import render
from rest_framework.views import APIView

from .serializer import InterfacesModelSerializer
from django.views import View
from django.http import JsonResponse, Http404
from .models import Interfaces
import json
# Create your views here.

class InterfaceDetail(APIView):

    def get_object(self, pk):
        try:
            obj1 = Interfaces.objects.get(id=pk)
        except Interfaces.DoesNotExist:
            # 不存在，可以抛出一个404的异常，这个异常是django自带的
            raise Http404
        return obj1
    def get(self, request, pk):
        """获取数据详情"""
        obj1 = self.get_object(pk)
        ser=InterfacesModelSerializer(instance=obj1)
        return JsonResponse(ser.data,json_dumps_params={"ensure_ascii":False})


class InterfacesList(APIView):

    def get(self, request):
        # 1.从数据库中获取所有的项目信息
        obj_list = Interfaces.objects.all()

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
        ser=InterfacesModelSerializer(instance=obj_list,many=True)
        return JsonResponse(ser.data,safe=False)
        # return HttpResponse("Hello, GET")

    def post(self, request):
        """新增项目"""
        # 1. 从前端获取json格式的数据，转换为python中的类型
        # 为了严谨性，这里需要做各种复杂的校验
        # 比如：是否是json，传递的项目数据是否符合要求，有些必传参数是否携带
        json_data = request.body.decode('utf-8')
        python_data = json.loads(json_data)
        ser=InterfacesModelSerializer(data=python_data)
        #校验前端输入的数据
        try:
            ser.is_valid(raise_exception=True)
        except Exception:
            # 只有在调用is_valid(raise_exception=True)
            # 方法之后，才可以调用errors属性，获取校验的错误提示
            return JsonResponse(ser.errors)
        ser.save()
        return JsonResponse(ser.data)