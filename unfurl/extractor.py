# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import re
import django
from django.contrib.admindocs.views import (simplify_regex, named_group_matcher,
                                            non_named_group_matcher)
try:
    from importlib import import_module
except ImportError:
    from django.utils.importlib import import_module
from django.utils.translation import ugettext as _

if django.VERSION[0:2] > (1, 7):
    from django.contrib.admindocs.views import extract_views_from_urlpatterns
else:  # Django <=1.7
    from django.core.exceptions import ViewDoesNotExist
    def extract_views_from_urlpatterns(urlpatterns, base='', namespace=None):
        # taken from 16a842b3795ca78a5918538ab6b9f1afbd718f72
        views = []
        for p in urlpatterns:
            if hasattr(p, 'url_patterns'):
                try:
                    patterns = p.url_patterns
                except ImportError:
                    continue
                views.extend(extract_views_from_urlpatterns(
                    patterns,
                    base + p.regex.pattern,
                    (namespace or []) + (p.namespace and [p.namespace] or [])
                ))
            elif hasattr(p, 'callback'):
                try:
                    views.append((p.callback, base + p.regex.pattern,
                                  namespace, p.name))
                except ViewDoesNotExist:
                    continue
            else:
                raise TypeError(_("%s does not appear to be a urlpattern object") % p)
        return views


all_params_re = re.compile(r'<\w+>')


def replace_simple_regex(value, offset):
    if value == "<var>":
        return "<arg:{}>".format(offset)
    else:
        just_value = value.strip('<').strip('>')
        return "<kwarg:{}>".format(just_value)


def get_urls(urlconf_name):
    urlconf = import_module(urlconf_name)
    all_urls = extract_views_from_urlpatterns(urlconf.urlpatterns)
    for mounted_url in all_urls:
        viewfunc = mounted_url[0]
        regex = mounted_url[1]
        try:
            namespace = mounted_url[2]
        except IndexError:
            namespace = None
        if namespace is None:
            namespace = []
        try:
            name = mounted_url[3]
        except IndexError:
            name = None
        modname = viewfunc.__module__
        viewname = getattr(viewfunc, '__name__', viewfunc.__class__.__name__)
        simple_url = simplify_regex(regex)
        named_groups = all_params_re.findall(simple_url)
        all_groups = (replace_simple_regex(var, index)
                      for index, var in enumerate(named_groups, start=1))
        textsearch = set()
        textsearch.update(modname.lower().split('.'))
        textsearch.add(viewname.lower())
        if name:
            textsearch.add(name.lower())
        textsearch.update(x.lower() for x in simple_url.split('/') if "<" not in x and x.strip() != '')
        yield {
            'textsearch': " ".join(textsearch),
            'textdata': textsearch,
            'module': modname,
            'view': viewname,
            'url': simple_url,
            'namespace': namespace,
            'namespace_string': ":".join(namespace),
            'name': name,
            'named_url_kwargs': tuple(all_groups),
        }
