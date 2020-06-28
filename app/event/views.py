# from django.shortcuts import render
#
# from django.contrib.auth.models import User, Group
# from rest_framework import generics
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
#
# from app.utils.permissions import OwnerPermission, BlackUserPermission, IsOwnerOrReadOnly, DocketUserPermission
#
# from .models import Event
# from .serializers import EventSerializer, EventSerializerDept
#
# from app.workflow.models import FlowLog, Docket, WorkflowAboutPeople
#
# import json
#
# # Create your views here.
#
#
# class EventViewSet(ModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#     # permission_classes = (IsAuthenticated, BlackUserPermission)
#     # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
#     permission_classes = (IsAuthenticated, DocketUserPermission)
#
#     def perform_create(self, serializer):
#         print(self.request.data)
#         # req_date = self.request.data
#         # assigner_id = req_date['assigner']
#         # print(assigner_id)
#         # print(type(assigner_id))
#         # assigner = User.objects.get(id=assigner_id)
#         #
#         # print(assigner)
#         # print(type(assigner))
#         distribute_type = '个人'
#
#         obj = serializer.save(last_reviser=self.request.user)
#
#         info = "受理人：{a},  主题：{t},  详情：{d},  解决方案: {s}".format(a=obj.assigner, t=obj.title, d=obj.description, s=obj.solution)
#         FlowLog.objects.create(operator=self.request.user, option_name=self.request.data['option_name'],
#                                description=info, uuid=obj.uuid)
#
#         Docket.objects.create(docket_state='启用', workflow_type='事件流程', distribute_type=distribute_type,
#                               docket_user=obj.assigner, docket_group=obj.approver_group, title=obj.title, request_id=obj.request_id,
#                               request_state=obj.state, uuid=obj.uuid, workflow_id=obj.id, description=obj.description)
#
#         WorkflowAboutPeople.objects.create(request_id=obj.request_id, workflow_type='事件流程', uuid=obj.uuid, about_user=self.request.user.id)
#
#     def perform_update(self, serializer):
#         print('-------perform_update---------')
#         print(self.request.data)
#         obj = serializer.save(last_reviser=self.request.user)
#
#         # about_users = obj.about_users
#         # about_users_list = about_users.split(';')
#         #
#         # about_users_set = set(about_users_list)
#         # obj.about_users = about_users_set
#
#         info = "受理人：{a},  主题：{t},  详情：{d},  解决方案: {s}".format(a=obj.assigner, t=obj.title, d=obj.description, s=obj.solution)
#         # 更新日志记录
#         FlowLog.objects.create(operator=self.request.user, option_name=self.request.data['option_name'],
#                                description=info, uuid=obj.uuid)
#
#         distribute_type = '个人'
#         docket_state = '启用'
#
#         if obj.state == '处理中':
#             distribute_type = '个人'
#         elif (obj.state == '已关闭') | (obj.state == '已取消'):
#             docket_state = obj.state
#
#         Docket.objects.filter(workflow_id=obj.id).update(docket_state=docket_state, workflow_type='事件流程', distribute_type=distribute_type,
#                                                              docket_user=obj.assigner, docket_group=obj.approver_group, title=obj.title,
#                                                              request_id=obj.request_id, request_state=obj.state, uuid=obj.uuid,
#                                                              workflow_id=obj.id, description=obj.description)
#
#         # about_users = obj.about_users
#         # print(type(about_users))
#         # about_users_str = about_users + str(obj.assigner.id) + ';'
#         # about_users_str = about_users_str[:-1]
#         # print('about_users_str------', about_users_str)
#         # about_users_list = about_users_str.split(';')
#         # print(about_users_list)
#         # about_users_set = set(about_users_list)
#         # print(about_users_set)
#         # obj.about_users = about_users_set
#         # obj.save()
#         # print(type(obj.about_users))
#
#         WorkflowAboutPeople.objects.create(request_id=obj.request_id, workflow_type='事件流程', uuid=obj.uuid,
#                                            about_user=self.request.user.id)
#
#     def get_serializer_class(self):
#         serializer_class = self.serializer_class
#         if self.request.method == 'GET':
#             serializer_class = EventSerializerDept
#         return serializer_class
#
#     def get_queryset(self):
#         queryset = self.queryset
#         search_map = self.request.query_params.get('searchMap', None)
#         if search_map:
#             # 将json格式字符串转化为dict
#             search_map_dict = json.loads(search_map)
#             # 查看是否有某个字段，有点话并进行过滤
#             request_id = search_map_dict.get('request_id', None)
#             if (request_id is not None) & (request_id != ''):
#                 queryset = queryset.filter(request_id__icontains=request_id)
#
#             title = search_map_dict.get('title', None)
#             if (title is not None) & (title != ''):
#                 queryset = queryset.filter(title__icontains=title)
#
#             description = search_map_dict.get('description', None)
#             if (description is not None) & (description != ''):
#                 queryset = queryset.filter(description__icontains=description)
#
#             assigner_group = search_map_dict.get('assigner_group', None)
#             if (assigner_group is not None) & (assigner_group != ''):
#                 queryset = queryset.filter(assigner_group=assigner_group)
#
#             assigner = search_map_dict.get('assigner', None)
#             if (assigner is not None) & (assigner != ''):
#                 queryset = queryset.filter(assigner=assigner)
#
#             state = search_map_dict.get('state', None)
#             if (state is not None) & (state != ''):
#                 queryset = queryset.filter(state=state)
#
#             create_time = search_map_dict.get('create_time', None)
#             if (create_time is not None) & (create_time != ''):
#                 queryset = queryset.filter(create_time__gte=create_time)
#
#             create_time_end = search_map_dict.get('create_time_end', None)
#             if (create_time_end is not None) & (create_time_end != ''):
#                 queryset = queryset.filter(create_time__lte=create_time_end)
#
#         return queryset
#
#
#
#
#
#
