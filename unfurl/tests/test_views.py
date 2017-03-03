# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from unfurl.views import urls_list


def test_view_load_all(rf):
    request = rf.get('/')
    response = urls_list(request)
    urls = tuple(response.context_data['urlconf'])
    assert len(urls) == 36


def test_view_load_some(rf):
    request = rf.get('/', data={'text': 'auth'})
    response = urls_list(request)
    urls = tuple(response.context_data['urlconf'])
    assert len(urls) == 21
