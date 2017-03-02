# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.template.response import TemplateResponse

from unfurl.extractor import get_urls


def urls_list(request):
    urls = get_urls(settings.ROOT_URLCONF)
    viewname_template = request.resolver_match.view_name.replace(':', '/')
    template = (
        '{}.html'.format(viewname_template),
        "unfurl/urls_list.html",
    )
    context = {
        'urlconf': urls,
    }
    return TemplateResponse(request=request, template=template, context=context)
