django-unfurl
================================

:author: Keryn Knight
:version: 0.1.1

.. |travis_stable| image:: https://travis-ci.org/kezabelle/django-unfurl.svg?branch=0.1.1
  :target: https://travis-ci.org/kezabelle/django-unfurl

.. |travis_master| image:: https://travis-ci.org/kezabelle/django-unfurl.svg?branch=master
  :target: https://travis-ci.org/kezabelle/django-unfurl

==============  ======
Release         Status
==============  ======
stable (0.1.1)  |travis_stable|
master          |travis_master|
==============  ======

What it is
----------
A small re-usable app for `Django`_ to output all the URLs used in a project,
both via a view and a management command. Internally re-uses functionality of
`admindocs`_

Rationale
---------

Ever come onto a project for the first time, or after a long period of time away
from it, and can't remember all the URLs being used? This is a quick and dirty
way to find out what's going on, if you're not using `admindocs`_ (which I
never do) ...

Getting started
---------------

You'll need to get the package onto your python path. For now, that's something like::

    pip install git+https://github.com/kezabelle/django-unfurl.git#egg=django-unfurl

You'll also need to ensure it's part of your ``INSTALLED_APPS``::

    INSTALLED_APPS += (
      'unfurl',
    )

Setting up the view
^^^^^^^^^^^^^^^^^^^

Then, in your root ``URLCONF`` (usually ``projectname/urls.py``), add::

  urlpatterns = [
    # ...
    url(r'^urls/', include('unfurl.urls')),
    # ...
  ]

Using the management command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Simply call ``python manage.py urls_list`` to have a list of all URLs output
to your console. If possible, it will output them in the ``less`` pager, unless
you're redirecting output (ie: ``python manage.py urls_list > all_urls.txt``


Tests
-----

There aren't many. This was just an experiment which I've refined a touch.
Trust it or don't.

The license
-----------

It's the `FreeBSD`_. There's should be a ``LICENSE`` file in the root of the repository, and in any archives.

.. _FreeBSD: http://en.wikipedia.org/wiki/BSD_licenses#2-clause_license_.28.22Simplified_BSD_License.22_or_.22FreeBSD_License.22.29
.. _Django: https://www.djangoproject.com/
.. _admindocs: https://docs.djangoproject.com/en/stable/ref/contrib/admin/admindocs/
