#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/10/22 10:43 
# email： liang1.li@ximalaya.com
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProjectList.as_view()),
    path('<int:pk>', views.ProjectDetail.as_view()),
]