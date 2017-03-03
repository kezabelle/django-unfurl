# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.forms import CharField
from django.forms import Form
from django.template.response import TemplateResponse

from unfurl.extractor import get_urls


class SearchForm(Form):
    text = CharField()

    def __init__(self, urls, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.urls = urls

    def clean_text(self):
        text = self.cleaned_data['text']
        parts = text.split(" ")
        return tuple(part for part in parts if part.strip() != '')

    def filter(self):
        if self.is_valid():
            for url in self.urls:
                for user_filter in self.cleaned_data['text']:
                    # look for character or partial or full match somewhere in the
                    # string of the set()
                    if user_filter in url['textsearch']:
                        yield url
        else:
            for url in self.urls:
                yield url


def urls_list(request):
    all_urls = get_urls(settings.ROOT_URLCONF)
    form = SearchForm(data=request.GET or None, initial=None, urls=all_urls)
    urls = form.filter()
    template = "unfurl/urls_list.html"
    context = {
        'urlconf': urls,
        'form': form,
    }
    return TemplateResponse(request=request, template=template, context=context)
