from django.urls import path, include

from rest_framework.routers import DefaultRouter
from . import views

app_name = 'ticket'

router = DefaultRouter()
router.register(r'event', views.EventViewSet, basename='event')


urlpatterns = [

]

urlpatterns += router.urls
