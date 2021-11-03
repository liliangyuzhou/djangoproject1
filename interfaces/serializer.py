#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/10/25 16:15 
# email： liang1.li@ximalaya.com

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from interfaces.models import Interfaces
from polls.models import Project



#自定义的模型序列化器
class InterfacesModelSerializer(serializers.ModelSerializer):

    #1.从表的模型序列化器默认自动创建了project这个父表字段校验，类型为PrimaryKeyRelatedField()，默认输出的父表
    # 的外健id值
    #如果只要输出的话，就写read_only=True
    # project=serializers.PrimaryKeyRelatedField(read_only=True)

    # #注：创建时候报错需要project_id替换project
    # project_id=serializers.PrimaryKeyRelatedField(read_only=True)

    #2.如果不想输出项目id，而是项目名称，要使用另外一种类型StringRelatedField（）,该类型源码可以看到只能进行序列化输出
    # 会自动调用Project的__str__方法，可以打断点查看
    # project=serializers.StringRelatedField(label="所属项目名称")

    #3.关联字段如果想要输出父表的其他字段，比如leader，tester等，要使用另外一种类型
    #slug_field这个参数必写，因为制定该父类字段project输出的值，尽量使用唯一约束的字段
    #只需要输出就写read_only=True
    # project=serializers.SlugRelatedField(slug_field="tester",read_only=True)
    #即需要序列化输出，也需要反序列化输入，那么就要写queryset参数
    # project=serializers.SlugRelatedField(slug_field="tester",queryset=Project.objects.all())


    class Meta:
        # 1.指定参考哪一个模型类来创建
        model=Interfaces
        fields="__all__"
