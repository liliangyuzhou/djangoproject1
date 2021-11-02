from django.shortcuts import render
from .serializer import InterfacesModelSerializer
from django.views import View
from django.http import JsonResponse, Http404
from .models import Interfaces
# Create your views here.

class InterfaceDetail(View):

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