
from django.shortcuts import render
import json
import os
import codecs

from django.conf import settings


from datetime import datetime

from django.contrib.auth.models import User, Group

from .serializers import UserSerializer, UserSerializerDepth, GroupSerializer, GroupSerializerDepth

from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, permissions, pagination, views
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser

from .models import Menu, FileForm
from .serializers import MenuSerializer
from app.common.mypaginations import MyPagination2


# 根据token获取用户信息
class UserTokenDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        print(user)
        return user


# 获取group信息
class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'GET':
            serializer_class = GroupSerializerDepth
        return serializer_class

    def get_queryset(self):
        queryset = self.queryset

        search_map = self.request.query_params.get('searchMap', None)
        if search_map:
            # 将json格式字符串转化为dict
            search_map_dict = json.loads(search_map)
            # 查看是否有某个字段，有点话并进行过滤
            name = search_map_dict.get('name', None)
            if (name is not None) & (name != ''):
                queryset = queryset.filter(name__icontains=name)
        return queryset


# 用户管理
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = self.queryset
        search_map = self.request.query_params.get('searchMap', None)
        if search_map:
            search_map_dict = json.loads(search_map)
            group_id = search_map_dict.get('group_id', None)

            if (group_id is not None) & (group_id != ''):
                group = Group.objects.get(id=group_id)
                print('group.name-------', group.name)
                # if group:
                #     queryset = group.user_set.all()
                queryset = queryset.filter(groups__name=group.name)

            return  queryset


# 获取菜单数据
class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    pagination_class = MyPagination2

    def perform_create(self, serializer):
        # 要一次性保存，不然只会执行最后一个好像
        serializer.save(lastModifyBy=self.request.user, author=self.request.user)

    def get_queryset(self):
        queryset = self.queryset

        search_map = self.request.query_params.get('searchMap', None)

        if search_map:
            # 将json格式字符串转化为dict
            search_map_dict = json.loads(search_map)

            # 查看是否有某个字段，有点话并进行过滤
            type_name = search_map_dict.get('typeName', None)
            if (type_name is not None) & (type_name != ''):
                queryset = queryset.filter(type_name=type_name)

            field_name = search_map_dict.get('field_name', None)
            if (field_name is not None) & (field_name != ''):
                queryset = queryset.filter(field_name=field_name)

            is_delete = search_map_dict.get('is_delete', None)
            if (is_delete is not None) & (is_delete != ''):
                queryset = queryset.filter(is_delete=is_delete)

        return queryset


# 文件上传
class FileUploadView(views.APIView):
    # parser_classes = (MultiPartParser, )

    def post(self, request):
        dt = datetime.now()
        year = dt.strftime('%Y')
        month = dt.strftime('%m')
        day = dt.strftime('%d')

        user = self.request.user
        user_id = str(user.id)

        file = request.data.get('file')
        name = file.name
        size = file.size
        # url = file.url
        # source_type = request.data.get('source_type')


        print(self.request.user)
        print(request.data)
        # print(request.data.FILES)
        print(request.FILES)

        print('name---', request.data['file'].name)
        # print(type(request.data['file']))

        print(request.FILES['file'])

        path_dir = os.path.join(settings.MEDIA_ROOT, year, month, day, user_id)
        os.makedirs(path_dir, exist_ok=True)
        print(path_dir)
        path = os.path.join(settings.MEDIA_ROOT, year, month, day, user_id, name)

        # 写入文件
        with open(path, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)

        file_form = FileForm.objects.create(source_type='Eve', name=name, size=size, url=path, create_user=user, modify_user=user)
        print(file_form)
        return Response(status=status.HTTP_200_OK, data={'id': file_form.id, 'url': path})


# 下载附件
from django.http import FileResponse, Http404


def down_attachment(request):

    # attachmentChecks = request.GET.getlist('attachmentChecks')
    # print(attachmentChecks)

    file_id = int(request.GET.get('file_id'))
    print(file_id)

    file_form = FileForm.objects.filter(id=file_id).first()
    print(file_form)
    # print(file_form.attach)
    # print(type(file_form.attach))
    # print(settings.MEDIA_ROOT)
    # url = "http://127.0.0.1:8000/media/"+ "attachment/2020/03/24/itop-duty_1hDeghf.zip"
    url = file_form.url
    print(url)
    file = open(url, 'rb')
    response = FileResponse(file)

    # file_end = url.split('.')[-1]
    # if not file_end:
    #     raise Http404('文档路径出错')
    # else:
    #     file_end = file_end.lower()
    # if file_end == "pdf":
    #     response["Content-type"] = "application/pdf"
    # elif file_end == "zip":
    #     response["Content-type"] = "application/zip"
    # elif file_end == "doc":
    #     response["Content-type"] = "application/msword"
    # elif file_end == "xls":
    #     response["Content-type"] = "application/vnd.ms-excel"
    # elif file_end == "xlsx":
    #     response["Content-type"] = "application/vnd.ms-excel"
    # elif file_end == "docx":
    #     response["Content-type"] = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    # elif file_end == "ppt":
    #     response["Content-type"] = "application/vnd.ms-powerpoint"
    # elif file_end == "pptx":
    #     response["Content-type"] = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    #
    # elif file_end == "png" or file_end == 'jpeg':
    #     response["Content-type"] = "application/octet-stream"

    # response = HttpResponse(content_type='text/csv')
    # response.write(codecs.BOM_UTF8)

    # response.setCharacterEncoding("UTF-8")

    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="aaa.zip"'
    print(response)
    return response



