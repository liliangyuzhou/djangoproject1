from django.shortcuts import render
from django.http import JsonResponse
from polls.models import Project

# Create your views here.
from django.views import View
class ProjectList(View):
    def get(self,request):
        #1.从数据库中获取所有的项目信息
        obj_list=Project.objects.all()
        #将数据库模型实例转化为字典类型（嵌套字典的列表）
        project_list=[]
        for i in obj_list:
            one_project={
                "name":i.name,
                "leader":i.leader,
                "tester":i.tester,
                "developer":i.developer
            }
            project_list.append(one_project)
        return JsonResponse(project_list)