from django.db import models


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Person(models.Model):
    """创建person类"""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Project(models.Model):
    """创建项目类
    max_length=30 为字段的最大长度
    unique代表设置该字段是否为一，默认为False
    verbose_name用来设置更人性化的字段名称
    help_text主要用于api文档中的中文名称
    """
    name = models.CharField(verbose_name="项目名称", max_length=30, unique=True,
                            help_text="项目名称")

    leader = models.CharField(verbose_name="负责人", max_length=50,
                              help_text="负责人")
    tester = models.CharField(verbose_name="测试人员", max_length=30,
                              help_text="测试人员")
    developer = models.CharField(verbose_name="开发人员", max_length=50,
                                 help_text="开发人员")
    publish_app = models.CharField(verbose_name="发布应用", max_length=100,
                                   help_text="发布应用")
    # 10.null设置数据库此字段允许为空
    # 11.blank用于设置前端可以不传递
    # 12. default用于设置默认值
    desc = models.TextField(verbose_name="描述", help_text="紧要描述", blank=True,
                            default="", null=True)

    #定义子类Meta，名称是固定的，用于设置当前数据模型的元数据信息
    class Meta:
        db_table='tb_projects'

        #会在admin站点中，显示一个更人性化的姓名
        verbose_name='项目'
        #复数样式，一般和verbose_name保持一致，不然会看到 名称为项目s
        verbose_name_plural='项目'

