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

# 创建序列化器
# 1.继承Serializer或者其的子类
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from polls.models import Project
from interfaces.serializer import InterfacesModelSerializer


# 创建自定义序列化器中的校验器
# 第一个参数为字段的值
def is_unqiue_project_name(name):
    if "项目" not in name:
        raise serializers.ValidationError("项目名称中必须包含项目关键字")


class ProjectSerializer(serializers.Serializer):
    """创建序列化器类"""
    # label：别名相当于verbose_name，help_text：帮助信息
    # 需要输出那些字段，就在序列化器中定义那些字段
    # read_only=True,指定该字段只能进行序列化输出
    # 定义的序列化字段，默认既可以进行序列化输出，也可以进行反序列化输入
    id = serializers.IntegerField(label='ID', read_only=True)
    # write_only=True,指定该字段只能进行反序列化输入，而不能进行反序列化输出
    name = serializers.CharField(label="项目名称", max_length=30,
                                 help_text="项目名称", write_only=True,
                                 validators=[UniqueValidator(queryset=Project.objects.all(), message="名称不能重复"),
                                             is_unqiue_project_name],error_messages={'max_length':"长度不能超过30,不写就是默认的错误信息",})

    leader = serializers.CharField(label="负责人", max_length=50,
                                   help_text="负责人",error_messages={'max_length':"长度不能超过50,不写就是默认的错误信息",})
    tester = serializers.CharField(label="测试人员", max_length=30,
                                   help_text="测试人员")
    developer = serializers.CharField(label="开发人员", max_length=50,
                                      help_text="开发人员")
    publish_app = serializers.CharField(label="发布应用", max_length=100,
                                        help_text="发布应用")
    # allow_null=True,allow_blank=True对应数据库模型类里面的null和blank
    desc = serializers.CharField(label="描述",
                                 help_text="紧要描述", allow_null=True,
                                 allow_blank=True, default="")
    #校验器写在序列化之外，看起来不太好，所以序列化器的校验器在序列化器里面也有两种方式
    # 1.单字段校验
    # 必须validate开头_后面是要校验字段的名称，value是前端传进来的值
    def validate_name(self, value):
        # 要求name必须以项目2个字结尾
        if not value.endswith("项目"):
            raise serializers.ValidationError("项目名称中必须以项目关键字结尾")
        # 这里注意一定要返回这个value，不然，序列化后的值这个字段的值为空
        return value

    # 2.多字段校验，名称只能是validate。attrs是一个列表
    def validate(self, attrs):
        """如果test不同时是项目负责人和测试负责人，抛出错误"""
        if 'test' in attrs['tester'] and 'test' in attrs['leader']:
            raise serializers.ValidationError("test必须不同时是项目负责人和测试负责人")
        return attrs

    def create(self, validated_data):
        """把对应的视图函数中create进行数据库操作的逻辑放到这里就可以"""
        # 这里注意使用这种解包的操作，如果在视图函数的save（）方法中传参数，要将这个参数移除后再解包，不然
        # 多了数据库里面没有的字段，会报错误。或者，可以使用validated_data["key"]=value来写
        obj = Project.objects.create(**validated_data)
        # 一定记得把创建成功的数据库模型类对象返回
        return obj

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.leader = validated_data['leader']
        instance.tester = validated_data['tester']
        instance.developer = validated_data['developer']
        instance.desc = validated_data['desc']
        instance.publish_app = validated_data['publish_app']
        instance.save()
        return instance

#自定义的模型序列化器
class ProjectModelSerializer(serializers.ModelSerializer):

    #如果还有定制化的序列化器属性，比如自定义的序列化器校验器，直接都用对应同名的字段来覆盖
    name = serializers.CharField(label="项目名称", max_length=30,
                                 help_text="项目名称", write_only=True,
                                 validators=[UniqueValidator(queryset=Project.objects.all(), message="名称不能重复"),
                                             is_unqiue_project_name])
    #在父表序列化器中定义从表的关联字段（一对多）
    #ModelSerializer直接指定父表，那么模型序列化器从表的字段不会自动被生成校验
    # 如果从表外健指定了related_name="interfaces"，使用interfaces，没有的话字段名称使用全小写的从表名_set,固定写法
    # many=True,一对多一定要写many=True，此时PrimaryKeyRelatedField类型返回值是id列表
    # interfaces=serializers.PrimaryKeyRelatedField(read_only=True,many=True)
    interfaces_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    #如果要不要展示接口的的id列表，而是名称.并且只要输出结果有多个，一定要加many=True
    # interfaces_set = serializers.StringRelatedField(many=True)

    #如果该字段要指定从表某个字段，使用SlugRelatedField
    # interfaces_set = serializers.SlugRelatedField(slug_field="tester",many=True,read_only=True)

    #我们还可以拿到从表的序列化器类，作为一个父表的一个字段，因为继承关系,都是继承自filed
    # interfaces_set=InterfacesModelSerializer(label="所属接口的信息",many=True)

    class Meta:
        # 1.指定参考哪一个模型类来创建
        model=Project
        #指定为模型类的那些字段，来生成序列化器
        # fields="__all__"
        #指定特定的字段，可以放在元组里面
        # fields =('id','name','leader','developer','tester' ,'interfaces')
        # fields = ('id', 'name', 'leader', 'developer', 'tester', 'interfaces_set')
        fields = ('id', 'name', 'leader', 'developer', 'tester', 'interfaces_set')
        #指定不需要序列化的字段,这个和上面指定特定字段 fields =('id','name','leader','developer','tester')等价
        # exclude=('desc','publish_app')

        # read_only_filelds=('leader','tester')
        #ProjectModelSerializer的其他字段的额外属性
        extra_kwargs={
            'leader':{
                'write_only':True,
                'error_messages':{
                    'max_length':"长度不能超过50,不写就是默认的错误信息"
                }
            }
        }
    # 单字段校验
    # 必须validate开头_后面是要校验字段的名称，value是前端传进来的值
    def validate_name(self, value):
        # 要求name必须以项目2个字结尾
        if not value.endswith("项目"):
            raise serializers.ValidationError("项目名称中必须以项目关键字结尾")
        # 这里注意一定要返回这个value，不然，序列化后的值这个字段的值为空
        return value

    # 多字段校验，名称只能是validate。attrs是一个列表
    def validate(self, attrs):
        """如果test不同时是项目负责人和测试负责人，抛出错误"""
        if 'test' in attrs['tester'] and 'test' in attrs['leader']:
            raise serializers.ValidationError("test必须不同时是项目负责人和测试负责人")
        return attrs

    #自动创建create和update，但是可以覆盖写