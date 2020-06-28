from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .models import State, Transition, Docket, FlowLog
from .serializers import StateSerializer, TransitionSerializer, DocketSerializer, FlowLogSerializer
import json


# Create your views here.


# 状态管理
class StateViewSet(ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = self.queryset

        # print(self.request.query_params)
        search_map = self.request.query_params.get('searchMap', None)
        if search_map:
            # 将json格式字符串转化为dict
            search_map_dict = json.loads(search_map)
            # 查看是否有某个字段，有点话并进行过滤
            name = search_map_dict.get('name', None)
            if (name is not None) & (name != ''):
                queryset = queryset.filter(name__icontains=name)

            workflow_id = search_map_dict.get('workflow_id', None)
            if (workflow_id is not None) & (workflow_id != ''):
                queryset = queryset.filter(workflow_id=workflow_id)

            create_date = search_map_dict.get('create_date', None)
            if (create_date is not None) & (create_date != ''):
                queryset = queryset.filter(create_date__gte=create_date)

            type_id = search_map_dict.get('type_id', None)
            if (type_id is not None) & (type_id != ''):
                queryset = queryset.filter(type_id=type_id)

        return queryset


# 流转管理
class TransitionViewSet(ModelViewSet):
    queryset = Transition.objects.all()
    serializer_class = TransitionSerializer

    def get_queryset(self):
        queryset = self.queryset

        search_map = self.request.query_params.get('searchMap', None)
        if search_map:
            # 将json格式字符串转化为dict
            search_map_dict = json.loads(search_map)
            # 查看是否有某个字段，有点话并进行过滤
            workflow_id = search_map_dict.get('workflow_id', None)
            if (workflow_id is not None) & (workflow_id != ''):
                queryset = queryset.filter(workflow_id=workflow_id)

            name = search_map_dict.get('name', None)
            if (name is not None) & (name != ''):
                queryset = queryset.filter(name__icontains=name)

            transition_type_id = search_map_dict.get('transition_type_id', None)
            if (transition_type_id is not None) & (transition_type_id != ''):
                queryset = queryset.filter(transition_type_id=transition_type_id)

            source_state_id = search_map_dict.get('source_state_id', None)
            if (source_state_id is not None) & (source_state_id != ''):
                queryset = queryset.filter(source_state_id=source_state_id)

            destination_state_id = search_map_dict.get('destination_state_id', None)
            if (destination_state_id is not None) & (destination_state_id != ''):
                queryset = queryset.filter(destination_state_id=destination_state_id)

            create_date = search_map_dict.get('create_date', None)
            if (create_date is not None) & (create_date != ''):
                queryset = queryset.filter(create_date__gte=create_date)

            create_date_end = search_map_dict.get('create_date_end', None)
            if (create_date_end is not None) & (create_date_end != ''):
                queryset = queryset.filter(create_date__lte=create_date_end)

        return queryset


# 待办数据
class DocketViewSet(ModelViewSet):
    queryset = Docket.objects.all()
    serializer_class = DocketSerializer
    lookup_field = 'request_id'

    def get_queryset(self):
        queryset = self.queryset
        search_map = self.request.query_params.get('searchMap', None)
        if search_map:
            search_map_dict = json.loads(search_map)

            docket_state = search_map_dict.get('docket_state', None)
            if (docket_state is not None) & (docket_state != ''):
                queryset = queryset.filter(docket_state=docket_state)
            if self.request.user.is_superuser != 1:
                queryset = queryset.filter(docket_user=self.request.user)

            request_id = search_map_dict.get('request_id', None)
            if (request_id is not None) & (request_id != ''):
                queryset = queryset.filter(request_id__icontains=request_id)
            title = search_map_dict.get('title', None)
            if (title is not None) & (title != ''):
                queryset = queryset.filter(title__icontains=title)
            workflow_type = search_map_dict.get('workflow_type', None)
            if (workflow_type is not None) & (workflow_type != ''):
                queryset = queryset.filter(workflow_type=workflow_type)
            request_state = search_map_dict.get('request_state', None)
            if (request_state is not None) & (request_state != ''):
                queryset = queryset.filter(request_state=request_state)
            description = search_map_dict.get('description', None)
            if (description is not None) & (description != ''):
                queryset = queryset.filter(description__icontains=description)
            modify_time = search_map_dict.get('modify_time', None)
            if (modify_time is not None) & (modify_time != ''):
                queryset = queryset.filter(modify_time__gte=modify_time)
            modify_time_end = search_map_dict.get('modify_time_end', None)
            if (modify_time_end is not None) & (modify_time_end != ''):
                queryset = queryset.filter(modify_time__lte=modify_time_end)

        return queryset


# 日志数据
class FlowLogViewSet(ModelViewSet):
    queryset = FlowLog.objects.all()
    serializer_class = FlowLogSerializer
    # lookup_field = 'uuid'

    def get_queryset(self):
        queryset = self.queryset
        uuid = self.request.query_params.get('uuid', None)
        print('uuid----------', uuid)
        if (uuid is not None) & (uuid != ''):
            queryset = queryset.filter(uuid=uuid)
        return queryset





