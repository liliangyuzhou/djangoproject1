"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from polls import views
from rest_framework.documentation import include_docs_urls

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(title="接口测试文档",  # 必传
                 default_version='v1',  # 必传
                 description="测试平台接口文档",
                 terms_of_service="https://www.google.com/policies/terms/",
                 contact=openapi.Contact(email="1287641566@qq.com"),
                 license=openapi.License(name="BSD License"),
                 ),
    public=True,
    # permission_classes=(permissions.AllowAny,), #权限类

)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index,name='index'),
    path('polls/', include('polls.urls')),
    path('interfaces/', include('interfaces.urls')),
    path('projects/', include('projects.urls')),

    # path('api/', include('rest_framework.urls')),
    path('docs/', include_docs_urls(title="测试平台接口文档", description="这是一个接口文档")),

    # drf-yasg,在drf1.1版本会使用url()
    # url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    #jwt添加认证
    path('api/',include('rest_framework.urls'))
]
