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
from rest_framework.validators import UniqueValidator
from polls.models import Project


#创建自定义序列化器中的校验器
#第一个参数为字段的值
def is_unqiue_project_name(name):
    if "项目" not in name:
        raise serializers.ValidationError("项目名称中必须包含项目关键字")


class ProjectSerializer(serializers.Serializer):
    """创建序列化器类"""
    #label：别名相当于verbose_name，help_text：帮助信息
    #需要输出那些字段，就在序列化器中定义那些字段
    # read_only=True,指定该字段只能进行序列化输出
    # 定义的序列化字段，默认既可以进行序列化输出，也可以进行反序列化输入
    id=serializers.IntegerField(label='ID',read_only=True)
    #write_only=True,指定该字段只能进行反序列化输入，而不能进行反序列化输出
    name = serializers.CharField(label="项目名称", max_length=30,
                                 help_text="项目名称", write_only=True,
                                 validators=[UniqueValidator(queryset=Project.objects.all(), message="名称不能重复"),is_unqiue_project_name])

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
                                 help_text="紧要描述",allow_null=True,
                                 allow_blank=True,default="")

    # 单字段校验
    #必须validate开头_后面是要校验字段的名称，value是前端传进来的值
    def validate_name(self,value):
        #要求name必须以项目2个字结尾
        if not value.endswith("项目"):
            raise serializers.ValidationError("项目名称中必须以项目关键字结尾")
        # 这里注意一定要返回这个value，不然，序列化后的值这个字段的值为空
        return value

    #多字段校验，名称只能是validate。attrs是一个列表
    def validate(self,attrs):
        """如果test不同时是项目负责人和测试负责人，抛出错误"""
        if 'test'  in attrs['tester'] and 'test'  in attrs['leader']:
            raise serializers.ValidationError("test必须不同时是项目负责人和测试负责人")
        return attrs





