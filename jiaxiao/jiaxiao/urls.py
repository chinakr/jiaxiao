#-*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from home.url_dispatch import URLDispatchView
from home.rss import RSSView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jiaxiao.views.home', name='home'),
    # url(r'^jiaxiao/', include('jiaxiao.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', URLDispatchView.as_view(), name='index'),
    url(r'^rss/$', RSSView.as_view(), name='rss_feed'),
    url(r'^(?P<page_name>\w+)/$', URLDispatchView.as_view(), name='channels'),
)
