# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from unfurl import urls as unfurl_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include(auth_urls)),
    url(r'^urls/', include(unfurl_urls)),
]

