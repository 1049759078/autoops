# Generated by Django 2.0 on 2017-12-30 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20171230_1817'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='toolsscript',
            options={'permissions': {('read_toolsscript', '只读工具')}, 'verbose_name': '工具', 'verbose_name_plural': '工具'},
        ),
    ]