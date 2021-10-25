# Generated by Django 3.2.8 on 2021-10-19 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('polls', '0005_alter_project_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interfaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tester', models.CharField(max_length=30, verbose_name='测试人员')),
                ('desc', models.TextField(blank=True, default='', help_text='紧要描述', null=True, verbose_name='描述')),
                ('project', models.ForeignKey(help_text='所属项目', on_delete=django.db.models.deletion.CASCADE, to='polls.project', verbose_name='所属项目')),
            ],
            options={
                'verbose_name': '接口',
                'verbose_name_plural': '接口',
                'db_table': 'tb_interfaces',
            },
        ),
    ]