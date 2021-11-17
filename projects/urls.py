#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/10/22 10:43 
# email： liang1.li@ximalaya.com
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from . import views
#自动生成路由
router = DefaultRouter()
# router.register(r"projects", views.ProjectViewSet)

# 1.创建SimpleRouter()对象
# router=routers.SimpleRouter()
# 2.注册路由
#参数prefix：为路由前缀，一般添加为子应用名，不需要🏠as_view()
# viewset：对应的视图集类
router.register(r"projects",views.ProjectViewSet,)

from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    # 这里注意路由不要直接写""，里面有个空格或者/都可以，不然可能出不来django rest framework这个接口文档页面
    # path('index', views.ProjectList.as_view()),
    # path('<int:pk>', views.ProjectDetail.as_view()),
    # 仅仅只用继承GenericViewSet，或者ViewSet之后，才具有  方法名：动作一一对应的功能
    # path('index', views.ProjectViewSet.as_view({
    #     'get': 'list',
    #     'post': 'create'
    # })),
    # path('<int:pk>', views.ProjectViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'destroy',
    #     'patch': 'partial_update'
    # })),
    # path('index/names', views.ProjectViewSet.as_view({
    #     # 获取所有的项目名称
    #     'get': 'names',
    #     # 'post':'names'
    #
    # })),
    # path('<int:pk>/interfaces', views.ProjectViewSet.as_view({
    #     'get': 'interfaces',
    # })),
    #将自动生成的路由添加到这个列表
    # path('',include(router.urls))
    #在子应用中添加jwt认证的login接口
    path('login/', obtain_jwt_token)
]

urlpatterns += router.urls
