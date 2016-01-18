"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from dashboard.views import Dashboard
from graph.views import Graph
from graph.views import get_graph_data
from brand.views import get_all_brands
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', Dashboard.as_view()),
	url(r'^graph/', Graph.as_view()),
	url(r'^admin/', include(admin.site.urls)),
    url(r'^get_graph_data/(?P<brand>\d{6})/(?P<type>\w+)/(?P<statType>\w+)/(?P<date>\d{4}-\d{2}-\d{2})/$', get_graph_data, name='get_graph_data'),
    url(r'^get_all_brands', get_all_brands, name='get_all_brands'),
)