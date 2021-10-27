#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/10/22 10:43 
# email： liang1.li@ximalaya.com
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# router = DefaultRouter()
# router.register(r"projects", views.ProjectViewSet)

urlpatterns = [
    #这里注意路由不要直接写""，里面有个空格或者/都可以，不然可能出不来django rest framework这个接口文档页面
    path('index', views.ProjectList.as_view()),
    path('<int:pk>', views.ProjectDetail.as_view()),

]

# urlpatterns += router.urls
