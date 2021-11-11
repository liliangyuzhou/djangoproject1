#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/11/11 17:43 
# email： liang1.li@ximalaya.com
from rest_framework.response import Response
from rest_framework import status
class ListModelMixin:
    def list(self,*args,**kwargs):
        obj_list = self.get_queryset()
        obj_list = self.filter_queryset(obj_list)
        page = self.paginate_queryset(obj_list)
        if page is not None:
            ser = self.get_serializer(instance=page, many=True)
            return self.get_paginated_response(ser.data)
        ser = self.get_serializer(instance=obj_list, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

class CreateModelMixin:
    def create(self,request,*args,**kwargs):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status=status.HTTP_200_OK)

class RetriveModelMixin:
    def retrive(self,*args,**kwargs):
        obj1 = self.get_object()
        ser = self.get_serializer(instance=obj1)
        return Response(ser.data, status=status.HTTP_200_OK)

# class UpdateModelMixin:
#     def update(self,request,*args,**kwargs):
#         obj2 = self.get_object()
#         ser = self.get_serializer(instance=obj2, data=request.data)
#         ser.save()
#         return Response(ser.data, status=status.HTTP_201_CREATED)