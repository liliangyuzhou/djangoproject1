from django.db import models

# Create your models here.
#一个项目有多个接口，那么要在"多的一侧"创建外健
class Interfaces(models.Model):
    name = models.CharField(verbose_name="接口名称", max_length=30, unique=True,
                            help_text="接口名称",null=True)
    tester = models.CharField(verbose_name="测试人员", max_length=30)
    desc = models.TextField(verbose_name="描述", help_text="紧要描述", blank=True,
                            default="", null=True)
    #外键，第一个参数为关联表的模型路径：应用名.模型类。或者导入，然后直接写模型类的名称
    #第二个参数是，当父表删除之后，改字段的处理方式
        #CASCADE--》字表也会被删除
        #SET_NULL-->当前外健值会被设置为None
        #PROTECT-->会报错
        #SET_DEFAULT--》父表被删除后，字表该条数据可以设置默认值，同时要指定默认值，null=True

    # project=models.ForeignKey('polls.Project',on_delete=models.CASCADE,
    #                           verbose_name="所属项目",help_text="所属项目",related_name="interfaces")

    project = models.ForeignKey('polls.Project', on_delete=models.CASCADE,
                                verbose_name="所属项目", help_text="所属项目")

    # 定义子类Meta，名称是固定的，用于设置当前数据模型的元数据信息
    class Meta:
        db_table = 'tb_interfaces'

        # 会在admin站点中，显示一个更人性化的姓名
        verbose_name = '接口'
        # 复数样式，一般和verbose_name保持一致，不然会看到 名称为项目s
        verbose_name_plural = '接口'

    # 在打印该模型类对象的时候，可以展示名称
    def __str__(self):
        return self.name

