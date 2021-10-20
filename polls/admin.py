from django.contrib import admin

# Register your models here.
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    """定制后台管理站点，这个类的名称自己起"""
    #指定在修改（新增）中需要显示的字段,必填字段必须全部选择
    fields = ('name','leader','tester','developer','publish_app')
    #指定要列出的字段
    list_display = ['id','name','leader','tester']

# admin.site.register(Project)
#定制化注册要改变注册方式
admin.site.register(Project,ProjectAdmin)