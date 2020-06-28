"""django_vue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.schemas import get_schema_view
schema_view = get_schema_view(title='pastebin API')


admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api-auth/', include('rest_framework.urls')),

    path('workflow/', include('app.workflow.urls', namespace='workflow')),
    # path('event/', include('app.event.urls', namespace='event')),
    path('common/', include('app.common.urls', namespace='common')),
    path('ticket/', include('app.ticket.urls', namespace='ticket')),




    # path('schema/', schema_view),
    # path('accounts/', include('django.contrib.auth.urls')),
]
