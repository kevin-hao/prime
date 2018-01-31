#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from . import views




app_name = 'falcon'

urlpatterns = [
    url(r'^serverslist/$', views.GetServer, name='serverlist'),
    url(r'^businessadd/$', views.BusinessAdd, name='addbusiness'),
    url(r'^businesslist/$', views.BusinessList, name='listbusiness'),
    url(r'^businessupdate/(?P<business_id>[0-9]+)/$', views.BusinessUpdate, name='updatebusiness'),
]