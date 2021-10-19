# Generated by Django 3.2.8 on 2021-10-19 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='项目名称', max_length=30, unique=True, verbose_name='项目名称')),
                ('leader', models.CharField(help_text='负责人', max_length=50, verbose_name='负责人')),
                ('tester', models.CharField(help_text='测试人员', max_length=30, verbose_name='测试人员')),
                ('developer', models.CharField(help_text='开发人员', max_length=50, verbose_name='开发人员')),
                ('publish_app', models.CharField(help_text='发布应用', max_length=100, verbose_name='发布应用')),
                ('desc', models.TextField(blank=True, default='', help_text='紧要描述', null=True, verbose_name='描述')),
            ],
        ),
    ]
