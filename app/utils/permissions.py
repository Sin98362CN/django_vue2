from rest_framework import permissions
from django.contrib.auth.models import User, Group
from app.workflow.models import Docket


# 待办人的认证
class DocketUserPermission(permissions.BasePermission):
    message = '这不是您的待办'

    def has_object_permission(self, request, view, obj):

        print('request.method-----------', request.method)
        if request.method == 'GET':
            return True
        user = request.user
        groups = user.groups.all()
        print('groups-------', groups)
        print(type(groups))

        request_id = obj.request_id
        print('request_id--------', request_id)

        docket = Docket.objects.filter(request_id=request_id).first()
        print('docket----------', docket)
        if docket:
            if docket.distribute_type == '组':
                print('组')
                return docket.docket_group in groups
            elif docket.distribute_type == '个人':
                print('个人')
                return docket.docket_user == user
            else:
                return False


class BlackUserPermission(permissions.BasePermission):
    message = '你是黑名单中的用户'

    def has_permission(self, request, view):
        # print(request.META)
        # print(type(request.user))
        # print('email----------', request.user.email)
        # username = request
        # return not request.user.username == 'jake'
        # print(User.objects.get(pk=4))
        # print(type(User.objects.get(pk=4)))
        return not request.user == User.objects.get(pk=1)

    # def has_object_permission(self, request, view, obj):
    #     print('obj.user----', obj.user)
    #     print('request.user----', request.user)
    #     return obj.user == request.user


class OwnerPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        print('111111111111111111-----------')
        print(self)
        print(request)
        print(view)
        print(obj)
        print('111111111111111111----------------------')
        print('obj.assigner----', obj.assigner)
        print('request.user----', request.user)
        return obj.assigner == request.user


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        # return obj.owner == request.user
        print('-------has_object_permission--------')
        print(self)
        print(request)
        print(view)
        print(obj)
        print('--------has_object_permission-------')
        print(request.user)
        ip_addr = request.META['REMOTE_ADDR']  # 获取请求方的ip
        print(ip_addr)
        # 获取请求过来的一个字段的内容
        print(request.data)
        return True
