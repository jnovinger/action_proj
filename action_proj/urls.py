"""action_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from actions.views import (
    ActionCreateView, ActionDeleteView, ActionDetailView, ActionDoneView,
    ActionEditView, ActionListView
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', ActionListView.as_view(), name='action-list'),
    url(r'^(?P<pk>\d+)/$', ActionDetailView.as_view(), name='action-detail'),
    url(r'^(?P<pk>\d+)/edit/$', ActionEditView.as_view(), name='action-edit'),
    url(r'^(?P<pk>\d+)/done/$', ActionDoneView.as_view(), name='action-done'),
    url(r'^(?P<pk>\d+)/delete/$', ActionDeleteView.as_view(), name='action-delete'),
    url(r'^add/$', ActionCreateView.as_view(), name='action-create'),
]
