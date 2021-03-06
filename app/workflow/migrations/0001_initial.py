# Generated by Django 2.2.12 on 2020-06-28 08:27

import app.workflow.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuidfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workflow_id', models.CharField(help_text='对应的流程', max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False, help_text='相当于删除不使用')),
                ('order_id', models.PositiveIntegerField(help_text='用来排序的')),
                ('type_id', models.CharField(help_text='初始状态、普通状态、结束状态', max_length=100)),
                ('distribute_type_id', models.CharField(blank=True, help_text='处理的类型: 直接处理、主动接单、随机分配、全部处理', max_length=100, null=True)),
                ('state_field_str', models.TextField(blank=True, help_text='字段显示，暂时不用', null=True)),
                ('uuid', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-create_date',),
            },
        ),
        migrations.CreateModel(
            name='Transition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workflow_id', models.CharField(help_text='对应的流程', max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('transition_type_id', models.CharField(help_text='流转方式：常规流转、定时器流转', max_length=100)),
                ('source_state_id', models.CharField(help_text='源状态', max_length=100)),
                ('destination_state_id', models.CharField(help_text='目标状态', max_length=100)),
                ('attribute_type_id', models.CharField(help_text='操作类型：同意、拒绝、其他', max_length=100)),
                ('alert_text', models.CharField(blank=True, help_text='弹出内容：操作成功的提示', max_length=100)),
                ('condition_expression', models.CharField(blank=True, help_text='条件表达式', max_length=100, null=True)),
                ('timer', models.CharField(blank=True, help_text='定时器：定时流转，多少秒后流转', max_length=100, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('uuid', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22)),
            ],
            options={
                'ordering': ('-create_date',),
            },
        ),
        migrations.CreateModel(
            name='WorkflowAboutPeople',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.CharField(blank=True, help_text='流程编号：流程传入request_id', max_length=100, null=True)),
                ('workflow_id', models.CharField(blank=True, help_text='流程的id：流程传入 id', max_length=100, null=True)),
                ('workflow_type', models.CharField(blank=True, help_text='流程类型', max_length=100, null=True)),
                ('uuid', models.CharField(blank=True, help_text='流程uuid：流程传入 uuid', max_length=100, null=True)),
                ('about_group', models.CharField(blank=True, help_text='相关组：流程传入 about_group', max_length=100, null=True)),
                ('about_user', models.CharField(blank=True, help_text='相关人：流程传入 about_user', max_length=100, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='FlowLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_name', models.CharField(blank=True, max_length=100, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('uuid', models.CharField(max_length=100)),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='flow_log_operator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Docket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docket_id', models.CharField(default=app.workflow.models.setRequestID, max_length=100)),
                ('docket_state', models.CharField(blank=True, help_text='待办表的状态，启用和已关闭', max_length=100, null=True)),
                ('workflow_type', models.CharField(help_text='流程类型', max_length=100)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('distribute_type', models.CharField(help_text='待办分配方式：是个人还是组来分配', max_length=100)),
                ('title', models.CharField(help_text='主题', max_length=254)),
                ('request_id', models.CharField(help_text='流程编号', max_length=100)),
                ('request_state', models.CharField(help_text='流程状态', max_length=100)),
                ('uuid', models.CharField(max_length=100)),
                ('workflow_id', models.IntegerField()),
                ('description', models.TextField(blank=True, help_text='流程详情', null=True)),
                ('docket_group', models.ForeignKey(blank=True, help_text='待办组', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='docket_docket_group', to='auth.Group')),
                ('docket_user', models.ForeignKey(blank=True, help_text='待办人', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='docket_docket_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-create_time'],
            },
        ),
    ]
