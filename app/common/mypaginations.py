from rest_framework import pagination
from rest_framework.response import Response


class MyPagination2(pagination.PageNumberPagination):
    page_size = 30   # 默认分页数
    page_query_param = 'page'   # 分页查询名
    page_size_query_param = 'ps'    # 每页数据大小查询名
    max_page_size = 100     # 最大分页数据数

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'data': data
        })


class MyPagination(pagination.PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    page_size_query_param = 'ps'
    max_page_size = 50

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'data': data
        })


