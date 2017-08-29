"""OnlineLibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https:docs.djangoproject.comen1.8topicshttpurls
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog', include(blog_urls))
"""
#! usrbinpython #coding=utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    url(r'^hello/$', views.hello),
    url(r'^admin', include(admin.site.urls)),
    url(r'^display/$', views.display),
    url(r'^add/$', views.add),
    url(r'^back/$', views.back),
    url(r'^addbook/$', views.addbook),
    url(r'^submit/$', views.submit),
    url(r'^submitbook/$', views.submitbook),
    url(r'^search_form/$', views.search_form),
    url(r'^searchbook_form_bo/$', views.searchbook_form_bo),
    url(r'^search/$', views.search),
    url(r'^booksearch_bo/$', views.booksearch_bo),
    url(r'^pack_modify/$', views.pack_modify),
    url(r'^pack_modify_bo/$', views.pack_modify_bo),
    url(r'^modify/$', views.modify),
    url(r'changebook/$', views.changebook),
    url(r'^seebook/$', views.seebook),
    url(r'au_delete/$', views.delByauthor),
    url(r'bo_delete/$', views.delBybook),
    url(r'seeallbook/$', views.seeallbook),
)
