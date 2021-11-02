#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/10/19 15:47 
# email： liang1.li@ximalaya.com
from django.urls import path

from . import views

urlpatterns = [
   # path('', views.index, name='index'),
   path('<int:pk>', views.InterfaceDetail.as_view()),
]