#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/10/25 16:15 
# email： liang1.li@ximalaya.com


from rest_framework.serializers import ModelSerializer
from polls.models import Project

class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model=Project
        fields="__all__"
