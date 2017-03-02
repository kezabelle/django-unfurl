# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required
from unfurl.views import urls_list

unfurl_url_list = url('^$', staff_member_required(urls_list), name="unfurl_url_list")

urlpatterns = [
    unfurl_url_list,
]
