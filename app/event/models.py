from django.db import models
from shortuuidfield import ShortUUIDField

from django.contrib.auth.models import User, Group

from datetime import datetime

from app.ticket.models import Ticket

# from app.workflow.models import FlowLog


# def setRequestID():
#     dt = datetime.now()
#     id_str = str(Event.objects.first().id + 1)
#     print(id)
#     num_str = '000000'
#
#     str_id = num_str[len(id_str):] + id_str
#
#     return "Eve{y}{m}{d}{str_id}".format(y=dt.strftime('%Y'), m=dt.strftime('%m'), d=dt.strftime('%d'), str_id=str_id)


# class Event(Ticket):
# class Event(models.Model):
#     pass
    # # title = models.CharField(max_length=100, help_text='标题')
    # open_time = models.DateTimeField()
    # # description = models.TextField()
    # assigner_group = models.ForeignKey(Group, on_delete=models.DO_NOTHING, help_text='受理组')
    # assigner = models.ForeignKey(User, on_delete=models.DO_NOTHING, help_text='受理人', blank=True, null=True)
    # approver_group = models.ForeignKey(Group,  on_delete=models.DO_NOTHING,
    #                                    help_text='审批组', null=True, blank=True)
    # approver = models.ForeignKey(User,  on_delete=models.DO_NOTHING, help_text='审批人', blank=True, null=True)
    # # state = models.CharField(max_length=100, help_text='当前状态')
    # next_state = models.CharField(max_length=100, help_text='下一状态', blank=True)
    # # last_reviser = models.ForeignKey(User, related_name='event_last_reviser', on_delete=models.DO_NOTHING, blank=True)
    # # create_time = models.DateTimeField(auto_now_add=True)
    # # modify_time = models.DateTimeField(auto_now=True)
    # # uuid = ShortUUIDField()
    # # request_id = models.CharField(max_length=100, default=setRequestID)
    # solution = models.TextField(null=True, blank=True, help_text='解决方案')
    # WorkflowAboutPeople = models.ForeignKey('workflow.WorkflowAboutPeople',
    #                                         on_delete=models.DO_NOTHING, help_text='相关人', null=True, blank=True)
    # # about_users = models.CharField(max_length=254,blank=True,null=True)
    #
    # # flow_log = models.ForeignKey(FlowLog, related_name='event_flow_log', on_delete=models.DO_NOTHING, help_text='关联日志表', blank=True, null=True)
    #
    # # class Meta:
    #     # ordering = ['-create_time']



