# Generated by Django 2.2.12 on 2020-06-28 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(blank=True, help_text='菜单是哪种类型，功能的还是某个模型上的', max_length=100, null=True)),
                ('field_name', models.CharField(blank=True, help_text='对应的字段名', max_length=100, null=True)),
                ('oneMenu', models.CharField(blank=True, help_text='一级菜单名', max_length=100, null=True)),
                ('twoMenu', models.CharField(blank=True, help_text='二级菜单名，没有可以为空', max_length=100, null=True)),
                ('is_delete', models.CharField(default=False, help_text='是否删除，其实就是是否可用', max_length=100)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('value', models.CharField(blank=True, help_text='真正的值', max_length=100, null=True)),
                ('order_num', models.PositiveIntegerField(default=100, help_text='查询的时候排序')),
                ('author', models.ForeignKey(blank=True, help_text='创建人', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='createName', to=settings.AUTH_USER_MODEL)),
                ('lastModifyBy', models.ForeignKey(blank=True, help_text='最后修改人', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='changeName', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-order_num'],
            },
        ),
        migrations.CreateModel(
            name='FileForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_type', models.CharField(max_length=100)),
                ('name', models.CharField(help_text='附件的名称', max_length=100)),
                ('size', models.PositiveIntegerField()),
                ('url', models.CharField(help_text='文件存放路径', max_length=500)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='file_form_create_user', to=settings.AUTH_USER_MODEL)),
                ('modify_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='file_form_modify_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-create_time'],
            },
        ),
    ]