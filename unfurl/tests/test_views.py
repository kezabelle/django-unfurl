# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import django

from unfurl.views import urls_list


def test_view_load_all(rf):
    request = rf.get('/')
    response = urls_list(request)
    urls = tuple(response.context_data['urlconf'])
    if django.VERSION[0:2] > (1, 8):
        assert len(urls) == 36
    else:
        # newer Djangos have redirect views in the admin
        assert len(urls) == 33


def test_view_load_some(rf):
    request = rf.get('/', data={'text': 'auth'})
    response = urls_list(request)
    urls = tuple(response.context_data['urlconf'])
    if django.VERSION[0:2] > (1, 8):
        assert len(urls) == 21
    else:
        # newer Djangos have redirect views in the admin
        assert len(urls) == 19
