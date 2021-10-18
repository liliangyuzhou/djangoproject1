#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/10/14 15:26 
# email： liang1.li@ximalaya.com
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index1', views.indexView.as_view()),
    path('<int:pk>/x', views.indexView.as_view()),
]