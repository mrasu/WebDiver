from django.conf.urls import patterns, include, url
from scraper import views

urlpatterns = patterns('',
    url(r'^$', views.yodobashi),

)
