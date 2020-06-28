from django.urls import path, include

from rest_framework.routers import DefaultRouter
from . import views

app_name = 'workflow'

router = DefaultRouter()
router.register(r'state', views.StateViewSet, basename='state')
router.register(r'transition', views.TransitionViewSet, basename='transition')
router.register(r'docket', views.DocketViewSet, basename='docket')
router.register(r'flowLog', views.FlowLogViewSet, basename='flowLog')


urlpatterns = [
    # path('state/', views.StateList.as_view())
]

urlpatterns += router.urls
