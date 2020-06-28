from django.db import models

from shortuuidfield import ShortUUIDField
from datetime import datetime
from django.contrib.auth.models import User, Group


# Create your models here.

def setRequestID(instance, filename):
    dt = datetime.now()
    # id_str = str(Ticket.objects.first().id + 1)
    id_str = str(Ticket.objects.first().id + 1)
    print(id)
    # print(instance.ticket_type)
    num_str = '000000'

    str_id = num_str[len(id_str):] + id_str

    return "TIC{y}{m}{d}{str_id}".format(y=dt.strftime('%Y'), m=dt.strftime('%m'), d=dt.strftime('%d'), str_id=str_id)


class Ticket(models.Model):
    title = models.CharField(max_length=100, help_text='标题')
    description = models.TextField()
    sponsor = models.ForeignKey(User, related_name='ticket_sponsor', on_delete=models.DO_NOTHING,
                                help_text='发起人：工单的发起人', blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    ticket_uuid = ShortUUIDField()
    sole_uuid = models.CharField(max_length=100, blank=True, null=True, help_text='唯一id，一般由前端传入')
    about_users = models.CharField(max_length=254, blank=True, null=True)
    state = models.CharField(max_length=100, help_text='当前状态')
    ticket_type = models.CharField(max_length=100, help_text='工单类型')
    request_id = models.CharField(max_length=100, default=setRequestID)
    last_reviser = models.ForeignKey(User, related_name='ticket_last_reviser', on_delete=models.DO_NOTHING, blank=True)
    create_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='ticket_create_user')

    class Meta:
        ordering = ['-create_time']


# 事件管理
class Event(Ticket):
    open_time = models.DateTimeField()
    assigner_group = models.ForeignKey(Group, related_name='event_assigner_group', on_delete=models.DO_NOTHING, help_text='受理组')
    assigner = models.ForeignKey(User, related_name='event_assigner', on_delete=models.DO_NOTHING, help_text='受理人', blank=True, null=True)
    approver_group = models.ForeignKey(Group, related_name='event_approver_group', on_delete=models.DO_NOTHING,
                                       help_text='审批组', null=True, blank=True)
    approver = models.ForeignKey(User, related_name='even_approver', on_delete=models.DO_NOTHING, help_text='审批人', blank=True, null=True)
    solution = models.TextField(null=True, blank=True, help_text='解决方案')
    WorkflowAboutPeople = models.ForeignKey('workflow.WorkflowAboutPeople', related_name='event_Workflow_about_people',
                                            on_delete=models.DO_NOTHING, help_text='相关人', null=True, blank=True)


