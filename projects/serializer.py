#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/10/25 16:15 
# email： liang1.li@ximalaya.com


# from rest_framework.serializers import serializerserializer
# from polls.serializers import Project
#
# class Projectserializerserializer(serializerserializer):
#     class Meta:
#         model=Project
#         fields="__all__"

#创建序列化器
#1.继承Serializer或者其的子类
from rest_framework import serializers
class ProjectSerializer(serializers.Serializer):
    """创建序列化器类"""
    #label：别名相当于verbose_name，help_text：帮助信息
    #需要输出那些字段，就在序列化器中定义那些字段
    # read_only=True,指定该字段只能进行序列化输出
    # 定义的序列化字段，默认既可以进行序列化输出，也可以进行反序列化输入
    id=serializers.IntegerField(label='ID',read_only=True)
    #write_only=True,指定该字段只能进行反序列化输入，而不能进行反序列化输出
    name = serializers.CharField(label="项目名称", max_length=30,
                            help_text="项目名称",write_only=True)
    leader = serializers.CharField(label="负责人", max_length=50,
                              help_text="负责人")
    tester = serializers.CharField(label="测试人员", max_length=30,
                              help_text="测试人员")
    developer = serializers.CharField(label="开发人员", max_length=50,
                                 help_text="开发人员")
    publish_app = serializers.CharField(label="发布应用", max_length=100,
                                   help_text="发布应用")
    #allow_null=True,allow_blank=True对应数据库模型类里面的null和blank
    desc = serializers.CharField(label="描述",
                                 help_text="紧要描述",allow_null=True,allow_blank=True,default="")


