from django.db import models
from app.ticket.models import Event
from shortuuidfield import ShortUUIDField

from django.contrib.auth.models import User, Group
from django.conf import settings
import uuid, hashlib
from datetime import datetime


# Create your models here.


def setRequestID():
    dt = datetime.now()
    id_str = str(Docket.objects.first().id + 1)
    print(id)
    num_str = '000000'
    str_id = num_str[len(id_str):] + id_str
    return "Eve{y}{m}{d}{str_id}".format(y=dt.strftime('%Y'), m=dt.strftime('%m'), d=dt.strftime('%d'), str_id=str_id)


# 流程状态
class State(models.Model):
    # workflow_id = models.ForeignKey(Event, related_name='state_event', on_delete=models.DO_NOTHING)
    workflow_id = models.CharField(max_length=100, help_text='对应的流程')
    name = models.CharField(max_length=100)
    is_hidden = models.BooleanField(default=False, help_text='相当于删除不使用')
    order_id = models.PositiveIntegerField(help_text='用来排序的')
    type_id = models.CharField(max_length=100, help_text='初始状态、普通状态、结束状态')
    distribute_type_id = models.CharField(max_length=100, help_text='处理的类型: 直接处理、主动接单、随机分配、全部处理',
                                          null=True, blank=True)
    state_field_str = models.TextField(help_text='字段显示，暂时不用', null=True, blank=True)
    uuid = ShortUUIDField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-create_date',)


# 流程跳转
class Transition(models.Model):
    # workflow_id = models.ForeignKey(Event, related_name='transition_event', on_delete=models.DO_NOTHING)
    workflow_id = models.CharField(max_length=100, help_text='对应的流程')
    name = models.CharField(max_length=100)
    transition_type_id = models.CharField(max_length=100, help_text='流转方式：常规流转、定时器流转')
    source_state_id = models.CharField(max_length=100, help_text='源状态')
    destination_state_id = models.CharField(max_length=100, help_text='目标状态')
    attribute_type_id = models.CharField(max_length=100, help_text='操作类型：同意、拒绝、其他')
    alert_text = models.CharField(max_length=100, help_text='弹出内容：操作成功的提示', blank=True)
    condition_expression = models.CharField(max_length=100, null=True, blank=True, help_text='条件表达式')
    timer = models.CharField(max_length=100, null=True, blank=True, help_text='定时器：定时流转，多少秒后流转')
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    uuid = ShortUUIDField()

    class Meta:
        ordering = ('-create_date',)


class FlowLog(models.Model):
    operator = models.ForeignKey(User, related_name='flow_log_operator', on_delete=models.DO_NOTHING)
    option_name = models.CharField(max_length=100, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    uuid = models.CharField(max_length=100)


# 待办表
class Docket(models.Model):
    docket_id = models.CharField(max_length=100, default=setRequestID)
    docket_state = models.CharField(max_length=100, null=True, blank=True, help_text='待办表的状态，启用和已关闭')
    workflow_type = models.CharField(max_length=100, help_text='流程类型')
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    distribute_type = models.CharField(max_length=100, help_text='待办分配方式：是个人还是组来分配')
    docket_group = models.ForeignKey(Group, on_delete=models.DO_NOTHING, related_name='docket_docket_group',
                                     help_text='待办组', null=True, blank=True)
    docket_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='docket_docket_user',
                                    help_text='待办人', null=True, blank=True)
    title = models.CharField(max_length=254, help_text='主题')
    request_id = models.CharField(max_length=100, help_text='流程编号')
    request_state = models.CharField(max_length=100, help_text='流程状态')
    uuid = models.CharField(max_length=100)
    workflow_id = models.IntegerField()
    description = models.TextField(null=True, blank=True, help_text='流程详情')

    class Meta:
        ordering = ['-create_time']


# 流程相关人员
class WorkflowAboutPeople(models.Model):
    request_id = models.CharField(max_length=100, help_text='流程编号：流程传入request_id', null=True, blank=True)
    workflow_id = models.CharField(max_length=100, help_text='流程的id：流程传入 id', null=True, blank=True)
    workflow_type = models.CharField(max_length=100, help_text='流程类型', null=True, blank=True)
    uuid = models.CharField(max_length=100, help_text='流程uuid：流程传入 uuid', null=True, blank=True)
    about_group = models.CharField(max_length=100, help_text='相关组：流程传入 about_group', null=True, blank=True)
    about_user = models.CharField(max_length=100, help_text='相关人：流程传入 about_user', null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_time']

