from django.urls import path, include

from rest_framework.routers import DefaultRouter
from . import views

app_name = 'common'

router = DefaultRouter()
router.register(r'menu', views.MenuViewSet, basename='menu')
router.register(r'group', views.GroupViewSet, basename='group')
router.register(r'user', views.UserViewSet, basename='user')


urlpatterns = [
    path('token_user/', views.UserTokenDetail.as_view(), name='token_user'),
    path('file_upload/', views.FileUploadView.as_view(), name='file_upload'),
    path('down_attachment/', views.down_attachment, name='down_attachment'),

]

urlpatterns += router.urls