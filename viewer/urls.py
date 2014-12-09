from django.conf.urls import patterns, include, url
from django.contrib import admin
from viewer import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^discover/(?P<discover_id>\d+)$', views.discover, name='viewer.discover'),

)
