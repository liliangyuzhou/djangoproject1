#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/11/11 14:27 
# email： liang1.li@ximalaya.com
from rest_framework.pagination import PageNumberPagination as _PageNumberPagination

class PageNumberPagination(_PageNumberPagination):
    #每页默认的数据条数，优先级最高，比全局配置还要高'PAGE_SIZE': 3,所以全局配置不需要注销
    page_size =4
    #每页查询字符串的名称，默认是'page'，可以更改
    page_query_param = 'p'
    #每页指定数据条数的查询字符串的名称，默认是None，可以修改
    page_size_query_param = 's'
    #每页限制最多展示的数据条数
    max_page_size = None
    #定义无效页面的页码提示，默认源码是_('Invalid page.')
    invalid_page_message = '页码无效'

