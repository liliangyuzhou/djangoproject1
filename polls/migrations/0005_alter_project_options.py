# Generated by Django 3.2.8 on 2021-10-19 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_project_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': '项目', 'verbose_name_plural': '项目'},
        ),
    ]
